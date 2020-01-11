from collections import defaultdict

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        import sys
        
        self.graph_dict = defaultdict(list)
        self.weight_dict = {} # 存放依照權重排序後的所有邊的dict
        self.node_pair = [] # 存放邊所連結的點的list，方便用來拉出邊上的元素
        self.node_list = [] # 存放所有圖中的點的list
        self.node_set = [] # 一開始預設每個節點都是只有自己一個元素的list，用來確認有無可能形成環
        
    def find_minima(self, last, uv):
        idx = 0
        mini = sys.maxsize
        cur_mini = mini

        for i in last:
            if idx in uv:
                if i < mini:
                    cur_mini = idx
                    mini = i
                    idx += 1
                else:
                    idx += 1
            else:
                idx += 1
                
        return cur_mini
    
    def cn(self, start, add_point, uv):
        for num in range(self.V):
            if self.graph[add_point][num] !=0 and self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                if self.graph_matrix[start][num] == sys.maxsize:
                    self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
                elif self.graph_matrix[start][num] != sys.maxsize:
                    if self.graph_matrix[start][add_point] + self.graph[add_point][num] < self.graph_matrix[start][num]:
                        self.graph_matrix[start][num] = self.graph_matrix[start][add_point] + self.graph[add_point][num]
        return self.graph_matrix[start]
        
    def Dijkstra(self, s): 
        if s > self.V-1:
            return {}
        
        uv = []
        
        for vertex in range(self.V):
            uv.append(vertex)
        
        start = uv.pop(s)
        
        for v in range(len(self.graph_matrix[start])):
            self.graph_matrix[start][v] = sys.maxsize
        
        self.graph_matrix[start][start] = 0
        
        add_point = start
        self.graph_matrix[start] = self.cn(start, add_point, uv)
        
        while uv != []:
            idx = self.find_minima(self.graph_matrix[start], uv)

            uv.remove(idx)
            self.graph_matrix[start] = self.cn(start, idx, uv)
        
        str_list = []
        for n in range(self.V):
            str_list.append(str(n))
        Dijkstra_dict = {k:v for k, v in zip(str_list, self.graph_matrix[start])}
        
        return Dijkstra_dict
    
    def transform(self, MST):
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_set_idx(self, node):
        for node_set_idx in range(len(self.node_set)):
            if node in self.node_set[node_set_idx]:
                return node_set_idx
    
    def sort_weight_set(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight_dict.setdefault(key, value)
        
        return self.weight_dict

    def add_edge(self, u, v, w): 
        # 把權重加到defaultdict格式的圖裡
        self.graph_dict[u,v].append(w)
        
        # 把邊的兩點紀錄起來
        self.node_pair.append([u,v])
        
        # 把點更新到所有點的集合
        if u not in self.node_list:
            self.node_list.append(u)
            self.node_set.append([u])
        if v not in self.node_list:
            self.node_list.append(v)
            self.node_set.append([v])
        
    def Kruskal(self):
        # 按權重排序
        MST = {}
        for node in range(len(self.node_pair)):
            self.weight_dict = self.sort_weight_set(self.node_pair[node][0], self.node_pair[node][1])
        
        for edge in range(len(list(self.weight_dict.keys()))):
            node_one = list(self.weight_dict.keys())[edge][0]
            node_two = list(self.weight_dict.keys())[edge][1]

            node_one_set_idx = self.find_set_idx(node_one)
            node_two_set_idx = self.find_set_idx(node_two)
            
            len_node_one_set = len(self.node_set[node_one_set_idx])
            len_node_two_set = len(self.node_set[node_two_set_idx])
            
            if len_node_one_set >= len_node_two_set:
                if node_two not in self.node_set[node_one_set_idx]:
                    self.node_set[node_one_set_idx] += self.node_set[node_two_set_idx]
                    self.node_set[node_two_set_idx] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
            else:
                if node_one not in self.node_set[node_two_set_idx]:
                    self.node_set[node_two_set_idx] += self.node_set[node_one_set_idx]
                    self.node_set[node_one_set_idx] = []
                    MST.setdefault(list(self.weight_dict.keys())[edge], list(self.weight_dict.values())[edge])
                    
        Kruskal_dict = self.transform(MST)
        return Kruskal_dict