from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = ini_dic(list)

    def add_edge(self,a,b):
        self.graph[a].append(b)
    
    def find_node(self, s, Q, trabfs):
        adjacency_list = self.graph[s]
        for i in adjacency_list:
            if i not in Q and i not in trabfs:
                Q.append(i)
        return Q
    
    def bfs_recur(self, s, Q, trabfs):
        if s not in trabfs:
            if s not in Q:
                Q.append(s)

                trabfs.append(Q[0])
                Q.pop(0)

                temp_node = trabfs[0]

                Q = self.check_adjacency_node(temp_node, Q, trabfs)
            
            else:
                trabfs.append(Q[0])
                temp_node = Q[0]
                Q = self.check_adj(temp_node, Q, trabfs)
                Q.pop(0)
                  
        return s, Q, trabfs
    
    def BFS(self, s):
        bfs_traves = []
        Q = []
        
        if self.graph[s] == []:
            return []
        
        s, Q, bfs_traves = self.bfs_recur(s, Q, bfs_traves)

        while Q != []:
            for num in Q:
                self.bfs_recursive(num, queue, bfs_traves)
                
        return bfs_traves
    
    def add_adj(self, num, S):
        adj_list = self.graph[num]
        for n in adj_list:
            if n not in S:
                S.append(n)
        return S
        
    def DFS(self, s):
        dsf_tra = []
        stack = []
        
        if self.graph[s] == []:
            return []

        stack.append(s)
        
        while stack != []:
            last_num = stack.pop() 
            if last_num not in dsf_tra:
                dsf_tra.append(last_num)        
                stack = self.add_adj(last_num, stack)
                    
        return dsf_tra