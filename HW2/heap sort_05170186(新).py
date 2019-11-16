#!/usr/bin/env python
# coding: utf-8

# In[11]:


num = [1,4,6,2,11,15,23]
class Solution(object):
    def heap(self, k, n, i):  #堆積
        large = i  #假設i為最大值的樹根
        left = 2 * i + 1      #分成左右子樹
        right = 2 * i + 2     

        if left < n and k[i] < k[left]:  #如果左子樹比原先假設的樹根(i)大 則讓左子樹代替原樹根i
            large = left 

        if right < n and k[large] < k[right]: #如果右子樹比樹根大 則讓右再替代樹根
            large = right 

        if large != i:  #如果原先假設的i不等於最大值 則交換位置 讓最大值成為樹根
            k[i],k[large] = k[large],k[i]  #換位置
            
    def heapSort(self, k): 
        n = len(k) #n為k字元數

        for i in range(n, -1, -1): #設定範圍從n個開始一個一個處理到0(因python是從0開始數所以end設定-1)
            heap(k, n, i) 

        for i in range(n-1, 0, -1): 
            k[i], k[0] = k[0], k[i]   # 換位置
            heap(k, i, 0)
        return k
print(num)           
output = Solution()
print(output)


# In[ ]:




