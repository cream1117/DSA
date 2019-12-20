#!/usr/bin/env python
# coding: utf-8

# In[1]:


tree = ['red-1', 'gray-2', 'pink-3', 'green-4', 'yellow-5', 'purple-6']
edgeList = [(0,0), (0,1), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (3,5),(4,2) , (4,5), (5,2)]
graphs = [tree, edgeList]

def dfs(graph, s):
    tree, edgeList = graph
    visited = []
    stack = [s]
    adjacencyList = [[] for verteice in tree]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visited:
                stack.append(neighbor)
        visited.append(current)
    return tree

print(dfs(graphs, 0))

#參考資料https://www.youtube.com/watch?v=zaBhtODEL0w
#https://www.programiz.com/dsa/graph-dfs
#https://www.youtube.com/watch?v=QVcsSaGeSH0


# In[ ]:




