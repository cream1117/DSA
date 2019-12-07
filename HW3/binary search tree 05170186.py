#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TreeNode:
    
    def __init__(me,x):
        me.val = x
        me.left = None
        me.right = None
                    
def insert(me,x):
        if me.x:
            if val < me.x:
                if me.left == None:
                    me.left = TreeNode(val)
                else:
                    me.left.insert(val)
            elif val > me.x:
                if me.right == None:
                    me.right = TreeNode(val)
                else:
                    me.right.insert(val)
        else:
            me.val = name

