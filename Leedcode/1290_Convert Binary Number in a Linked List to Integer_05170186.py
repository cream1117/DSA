#!/usr/bin/env python
# coding: utf-8

# In[9]:


class ListNode:
    def __init__(myself, a):
        myself.val = a
        myself.next == None

class Solution:
    def getDecimalValue(self, myhead):
        if myhead == None:
            return
        numbers += str(myhead.val)
        cur = myhead
        
        while cur.next != None:
            numbers += str(cur.next.val)
            cur = cur.next
        
        return int(numbers, 2)


# In[ ]:




