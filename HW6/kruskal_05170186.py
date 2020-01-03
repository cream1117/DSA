class DisjointSet(dict):
    '''不相交集'''

    def __init__(self, dict):
        pass

    def add(self, item):
        self[item] = item

    def find(self, item):
        if self[item] != item:
            self[item] = self.find(self[item])
        return self[item]

    def unionset(self, item1, item2):
        self[item2] = self[item1]

def Kruskal(nodes, edges):
    all_nodes = nodes  # set(nodes)
    used_nodes = set()
    MST = []
    edges = sorted(edges, key=lambda element: element[2], reverse=True)
    # 對所有的邊按權重升序排列
    while used_nodes != all_nodes and edges:
        element = edges.pop(-1)
        if element[0] in used_nodes and element[1] in used_nodes:
            continue
        MST.append(element)
        used_nodes.update(element[:2])
        # print(used_nodes)
    return MST