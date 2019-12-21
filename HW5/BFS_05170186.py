#!/usr/bin/env python
# coding: utf-8

# In[8]:


from collections import defaultdict 
class Graph: 
  
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def add_new_edge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, stack): 
        visited_before = [False] * (len(self.graph)) 
        queue = [] 
        queue.append(stack) 
        visited_before[stack] = True
  
        while queue: 
            stack = queue.pop(0) 
            print(stack, end = " ") 
            for index in self.graph[stack]: 
                if visited_before[index] == False: 
                    queue.append(index) 

                    visited_before[index] = True
                    
                    
#參考資料https://www.youtube.com/watch?v=A0qe6AufMcI
#https://www.youtube.com/watch?v=97poC-xlLbA
#https://www.youtube.com/watch?v=pcKY4hjDrxk
  


# In[ ]:




