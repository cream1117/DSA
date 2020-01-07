#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.Queue = []
        self.Stack = []

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def print_queue(self):
        if self.graph == defaultdict(list):
            print(" No Node in graph !")
        else:
            print("adjacency list:")
            for key,val in self.graph.items():
                print(key, ":", val)
                
    def del_queue(self):
        if len(self.Queue) == 0:
            print("no data in queue !")
        else:
            item = self.Queue[0]
            self.Queue = self.Queue[1:]
            return item
        
    def add_queue(self, item):
        self.Queue = self.Queue+[item]
        
    def pop_stack(self):
        if len(self.Stack) == 0:
            print("no data in stack !")
        else:
            item = self.Stack[-1]
            self.Stack = self.Stack[:-1]
            return item
        
    def push_stack(self, item):
        self.Stack = self.Stack+[item]
        
    def BFS(self, s):
        if len(self.graph.keys()) == 0:
            print("no data in Graph !")
        elif s not in self.graph.keys():
            print("start point isn't exist !")
        else:
            output = [s]
            print('output: ',output,'\n')
            for i in self.graph[s]:
                self.add_queue(i)
            while len(output) < len(self.graph.keys()):
                print('Queue: ',self.Queue)
                item = self.del_queue()
                if item is not None:
                    output.append(item)
                    print('add: ',item)
                    print('output: ',output,'\n')
                if (item is None) or (self.graph[item]==None):
                    continue
                for index in self.graph[item]:
                    if (index not in self.Queue) and (index not in output):
                        self.add_queue(i) 
            return out

    def DFS(self, s):
        if len(self.graph.keys()) == 0:
            print("no data in Graph !")
        elif s not in self.graph.keys():
            print("start point isn't exist !")
        else:
            self.push_stack(s)
            output = []
            while self.Stack:
                print('Stack: ',self.Stack)
                item = self.Stack[-1]
                if item not in output:
                    output.append(item)
                    for index in self.graph[item]:
                        if (index not in output)&(index not in self.Stack):
                            self.push_stack(i)
                else:
                    self.pop_stack()
                print('output: ',out,'\n')
                    
            return out


# In[ ]:




