#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Cryptodome.Hash import MD5
class ListNode:
    def __init__(self, data):
        self.data = data
        self.link = None
class MyHashSet:
    def __init__(self, storage=200):
        self.storage = storage
        self.contents = [None] * storage
    def add(self, key):
        hashtable = MD5.new()
        hashtable.update(key.encode("utf-8"))
        hashtable = hashtable.hexdigest()
        bucket = int(hashtable , 16)%self.storage
        if self.contents[bucket] == None:
            self.contents[bucket] = ListNode(hashtable)
        else:
            new = ListNode(hashtable)
            now = self.contents[bucket]
            while now.link != None:
                now = now.link
            now.link = new
    def remove(self, key):
        hashtable = MD5.new()
        hashtable.update(key.encode("utf-8"))
        hashtable = hashtable.hexdigest()
        bucket = int(hashtable , 16)%self.storage
        deletebucket = self.contents[bucket]
        if deletebucket != None:
            if deletebucket.link != None:
                if deletebucket.data == hashtable:
                    self.contents[bucket] = deletebucket.link
                else:
                    while deletebucket.link:
                        if deletebucket.data == hashtable:
                            prev.link = deletebucket.link
                            deletebucket = deletebucket.link
                        else:
                            prev = deletebucket
                            deletebucket = deletebucket.link
                    if deletebucket.link == None:
                        if deletebucket.data == hashtable:
                            prev.link = deletebucket.link
            else:
                if deletebucket.data == hashtable:
                    self.contents[bucket] = None
        if self.contains(key) == True:
            self.remove(key)
    def contains(self, key):
        hashtable = MD5.new()
        hashtable.update(key.encode("utf-8"))
        hashtable = hashtable.hexdigest()
        bucket = int(hashtable, 16)%self.storage
        if self.contents[bucket] != None:
            node = self.contents[bucket]
            if node.data == hashtable:
                return True
            else:
                while node.link != None:
                    node = node.link
                    if node.data == hashtable:
                        break
                if node.data == hashtable:
                    return True
                else:
                    return False
        else:
            return False

def main():
    test_list_1 = ['pig', 'dog']
    test_list_2 = ['pig', 'dog', 'cat', 'bird']

    hashSet = MyHashSet()
    for i in range(len(test_list_1)):
        hashSet.add(test_list_1[i])
    for j in range(len(test_list_2)):
        rel = hashSet.contains(test_list_2[j])
        print(rel)
    hashSet.remove('pig')
    rel = hashSet.contains('pig')
    print(rel)

main()

