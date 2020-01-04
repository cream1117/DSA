#!/usr/bin/env python
# coding: utf-8

# In[3]:


def find(self, item):
    if item != self[item]:
        self[item] = find(self, self[self[item]])
    return self[item]

def unionset(self, item1, item, item2):
    item2 = find(self, u)
    item2 = find(self, item2)
    if R[item] > R[item2]:
        self[item2] = item
    else:
        self[item] = item2
    if item1[item] == item1[item2]:
        item1[item2] += 1

def kruskal(g):
    E = [(G[item][item2], item, item2) for u in G for item2 in G[u]]
    T = set()
    self, item1 = {u:u for u in G}, {u:0 for item in G}
    for _, item, item2 in sorted(G):
        if find(self, item) != find(self, item2):
            T.add(set(item, item2))
            unionset(C, item1, item, item2)
    return T


# In[ ]:




