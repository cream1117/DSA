#!/usr/bin/env python
# coding: utf-8

# In[33]:


#作業
num = [1,4,6,2,11,15,23]
class solution(object):
    def heap(self,k,n,i):    #括號裡面的數值?
        large = i
        left = 2*i+1
        right = 2*i+2
        
        if left < n and k[i] < k[left]
        large = left
        
        if right < n and k[large]< k[right]:
            large = right
            
        if large != i:
            k[i],k[large]=k[large],k[i]
    def heapSort(self,k):
        n = len(k)
        
        for i in range(n, -1, -1):
            heap(k,n,i)
            
        for i in range(n-1,0,-1):
            k[i],k[0] = k[0],k[i]
            heap(k,i,0)
        return k
output = solution()
print(output)


# In[26]:


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
        return [heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# In[11]:


def my_heap_sort(sqc):                    
    def heapify(count):                
        start = (count-2)/2            
        while start >= 0:              
            sift_down(start, count-1)  
            start -= 1                 

    def swap(i, j):                    
        sqc[i], sqc[j] = sqc[j], sqc[i]

    def sift_down(start, end):         
        root = start                   

        while (root * 2 + 1) <= end:   
            child = root * 2 + 1       
            temp = root                
            if sqc[temp] < sqc[child]: 
                temp = child+1         
            if temp != root:           
                swap(root, temp)       
                root = temp            
            else:                      
                return                 

    count = len(sqc)                   
    heapify(count)                     

    end = count-1                      

    while end > 0:                     
        swap(end, 0)                   
        end -= 1                       
        sift_down(0, end)       


# In[15]:


def heappushpop(heap,item):
    if heap and heap[0] < item:
        item,heap[0] = heap[0],item
    return item


# In[16]:


def heapreplace(heap,item):
    if item > heap[0]:
        item = heapreplace(heap,item)

    returnitem = heap[0]
    heap[0] = item
    return returnitem


# In[17]:


def heappushpop(heap,item):
    if heap and heap[0] < item:
        item,heap[0] = heap[0],item
        return item
        


# In[24]:


#在線性時間內將 list x 轉為 heap，且過程不會申請額外記憶體。
def heapify(x):
    for i in reversed(range(n//2)):
        _situp(x,i)


# In[21]:


#heap max版本
def _heappop_max(heap):
    lastlist = heap.pop()   #如果是空的，會引發錯誤
    if heap:
        returnitem = heap[0]
        heap[0] = lasttelt
        _siftup_max(heap,0)
        return returnitem
    return lastelt
    


# In[22]:


#自行更改參數

def heapsort(heap,item):
    if heap:
        item = heap[0]
        heap[0] = lastelt
        return item
    return lastelt


# In[27]:


def _heapreplace_max(heap,item):
    returnitem = heap[0]
    heap[0] = item
    _siftup_max(heap,0)
    return returnitem
    


# In[29]:


def _heapify_max(x):
    n = len(x)
    for i in reversed(range//2):
        _siftup_max(x,i)


# In[32]:


def _siftdown(heap,startpos,pos):
    newitem=heap[pos]
    while pos >startpos:
        parentpos = (pos-1) >>1
        parent = heap[parentop]
        if newitem < parent:
            pos = parentops
            continue
        break
    heap[pos] = newitem


# In[39]:


def push(self,item):
    self.heap.append(item)
    self._swim(self.heap,len(self.heap)-1)  
#不懂的部分


# In[40]:


def pop(self):
    self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
    item = self.pop()           #不懂
    self._sink(self.heap,0)     #不懂
    return item


# In[43]:


stack = []
len(stack)
import collections
stack = collections.deque()


# In[44]:


queue = []
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0)
queue[0]


# In[45]:


queue = []
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0)
queue[0]


# In[47]:


stack = []
len(stack)
import collections
stack= collections.deque()


# In[48]:


#stack
class Node:
    def__init__(self,val,nextNode=None):
        self.val = val
        self.temp_min = val
        self.next = nextNode
        
class Minstack:
    def__init__(self):
        self.topNode = None
    def push(self,x:int)→None:
        if self.topNode is None:
            self.topNode = Node(x,None)
        else:
            temp = self.topNode.temp_min
            self.topNode = Node(x,self.topNode)
            if temp < self.topNode.val:
                self.topNode.temp_min = temp
    def pop(self)→None:
        self.topNode = self.topNode.next
    def top(self)→int:
        return self.topNode.val
    def getMin(self)→int:
        return self.topNode.temp_min        


# In[1]:


#queue
class MyQueue(object):
    def __init__(self):
        self.inputStack = []
        self.resStack = []
        
    def push(self,x)
    self.inputStack.append(x)
    
    def pop(self):
        if self.resStack:
            return self.resStack.pop()
        while len(self.inputstack)is not 0:
            self.resStack.append(self.inputStack.pop())
        return self.resStack.pop()
    def peek(self):
        if self.resStack:
            return self.resStack[-1]
        while len(self.inputStack)is not 0:
            self.resStack.append(self.inputStack.pop())
        return self.resStack[-1]
    def empty(self):
        return len(self.inputStack) ==0 and len(self.resStack) ==0


# In[2]:


#linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def count_nodes(head):
        count = 1
        current = head
        while current.next is None:
            count += 1
        return count


# In[7]:


#heap sort
num = [1,4,6,2,11,15,23]
class solution(object):
    def heap(self,k,n,i):
        large = i
        left = 2*i+1
        right = 2*i+2
        if left < n and k[i]< k[left]:
            large = left
        if right < n and k[i]< k[right]:
            large = right
        if large != i:
            k[i],k[large] = k[large],k[i] 
    def heapSort(self,k):
        n = len(k)
        for i in range(n,-1,-1):
            heap(k,n,i)
        for i in range(n-1,0,-1):
            k[i],k[0] = k[0],k[i]
            heap(k,i,0)
        return k
print(num)
output = Solution()
print(output)
        


# In[14]:


#heap sort
def heapify(arr,n,i):
    large = i
    left = 2*i +1
    right = 2*i+2
    
    if left < n and arr[i]< arr[left]:
               large =left
    if right< n and arr[i]< arr[right]:
               large = right
    if large != i:
        arr[i],arr[large]=arr[large],arr[i]
        heapify(arr,n,large)
        
def heapSort(arr):
    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
arr = [4,10,3,5,1]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print(%d,%arr[i]),


# In[2]:


#BST新增
def insert(self,data):
    if self.root:
        return self.root.insert(data)
    else:
        self.root = Node(data)
        return True
    
#搜尋
def find(self,data):
    if self.root:
        return self.root.find(data)
    else:
        return Flase
#修改
def getHight(self): 
    If self.root:
        return self.root.gethight()
    else:
        return-1
#刪除
def remove(self,data):
    if self.root is None:
        return Flase    


# In[16]:


#RBT
class RBT(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
        self.isRed = True
class RBT(object):
    def insert(self,val):
        self.root = self.insertTo(self.root,val)
        self.root.isRed = Flase
    def searchK(self,k,root = None):
        root = root or self.root
        size = self.sizeOf(root.left)+1
        
        
        


# In[ ]:


class Node:
    def __init__(self,val,nextNode=None):
        self.val = val
        self.temp_min = val
        self.next = nextNode
        
class MinStack:
    def__init__(self):
        self.topNode = None
    def push(self,x:int)None
        if self.topNode is None
           self.topNode = Node(x,None)
        else:
            temp = self.topNode = Node
    

