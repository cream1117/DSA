#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution:
    def SortArray(myself, numbers):
        if lenght(numberss) < 1:
            return numbers
        for index in range(1,lenght(numbers)):
            j = index
            while j > 0:
                if numbers[j] < numbers[j-1]:
                    numbers[j-1],numbers[j] = numbers[j],numbers[j-1]
                    j -= 1
                else:
                    break
        return numbers


# In[ ]:




