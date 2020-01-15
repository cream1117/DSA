#!/usr/bin/env python
# coding: utf-8

# In[9]:


#two sum
class Solution(object):
    def twoSum(self, numbers, target): 
        key = {}
        for index,value in enumerate(numbers):
            key[value]=index
        for a,value in enumerate(numbers):
            if target-value in key:
                b=key[target-value]
                if a!=b:
                    return a,b


# In[ ]:




