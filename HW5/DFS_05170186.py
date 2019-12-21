#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

#參考資料https://www.youtube.com/watch?v=zaBhtODEL0w
#https://www.programiz.com/dsa/graph-dfs
#https://www.youtube.com/watch?v=QVcsSaGeSH0


# In[ ]:




