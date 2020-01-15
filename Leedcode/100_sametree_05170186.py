#!/usr/bin/env python
# coding: utf-8

# In[19]:


class Solution:
    def isSameTree(self,a_TreeNode,b_TreeNode):
        if a_TreeNode and b_TreeNode:
            return a_TreeNode == b_TreeNode and self.isSameTree(a_TreeNode.left, b_TreeNode.left) and self.isSameTree(a_TreeNode.right, b_TreeNode.right)
        return a_TreeNode == b_TreeNode


# In[ ]:




