#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.temp_min = val
        self.next = nextNode

class MinStack:

    def __init__(self):
        self.topNode = None
    def push(self, x: int) :
        if self.topNode is None:
            self.topNode = Node(x, None)
        else:
            temp = self.topNode.temp_min
            self.topNode = Node(x, self.topNode)
            if temp < self.topNode.val:
                self.topNode.temp_min = temp
                
    def pop(self):
        self.topNode = self.topNode.next

    def top(self) :
        return self.topNode.val

    def getMin(self) :
        return self.topNode.temp_min
    
#Val是參數(放資料的地方)

#Nextnode(索引到下一個地方)

#None是沒有值

#temp是暫時的最小值

#Self.next 為後面要有其他值

#接著初始化

#先將箱子假設一開始都是空的

#所以箱子都是none

#Push功能

#Top目的是記最後一個位置

#假設top裡面沒東西是none

#Topnode= none就是(x，none)

#Temp(暫時)的最後一本書位置記起來

#Self.topNode = Node(x,self.topNode)把新的書放進去

#接著更新最後一本書的位置

#Self.topNode = self.topNode.next

#若拿最上面那本書，要告訴別人下次拿的是哪一本書

#Top功能

#最上面那本書是什麼要回傳

#getMin功能

#取得top裡面最小的值算是什麼


# In[ ]:




