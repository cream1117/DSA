# My DSA Note
## 我的個人介紹
我是一名轉系生，目前是在巨資系四年級A班
我是陳韻涵，可以叫我Cream

# week1
## 

# week2
## 為什麼要有Linked List
1.從儲存的角度
2.從操作的角度
3.Block Chain
## 什麼是Linked List
連結串列（Linked list）是一種常見的基礎資料結構，是一種線性表，但是並不會按線性的順序儲存資料，而是在每一個節點裡存到下一個節點的指標(Pointer)。使用連結串列結構可以克服陣列連結串列需要預先知道資料大小的缺點，連結串列結構可以充分利用電腦記憶體空間，實現靈活的記憶體動態管理。

# week3
## Stack & Queue
- 編譯器(word、sublime)的 undo 。
- 網頁瀏覽器中回到上一頁功能。
- 任何遞迴(recursion)形式的演算法都可以用 Stack 改寫，例如 Depth-First Search(DFS,深度優先搜尋)
## Stack必須要有的功能有哪些?
 - Push(Data): 把資料放到最上面(最新)。
 - Pop: 把資料從最上面(最新)移除。
 - Top: 回傳最上面(最新)的資料。
 - IsEmpty: 確認stack 裡面是否有資料。
 - getSize: 回傳stack 裡的資料個數。
## 為什麼要有Queue
 - 應用在其他演算法:
  - Bread-First Search | 廣度優先搜尋
  - Tree 的 Level-Order Traversal | 二元樹走訪
  -作業係統被多個程式共享資源時(例如CPU、應表機、網站伺服器)，一次只能執行一個需求，所以需要用 Queue 來安排執行順序。
## Queue必須要有的功能有哪些?
 - Push(Data): 把資料放到 Queue 的後面，並更新成新的 back。
 - Pop(dequeue): 把 front 所指向的資料從 Queue 中移除，並更新front。
 - getFront: 回傳 front 所指向的資資料。
 - getBack: 回傳 Back 所指向的資資料。
 - IsEmpty: 確認 Queue 裡是否有資料。
 - getSize: 確認 Queue 裡的資料個數。

# week4
## 插入排序法(Insertion Sort)
 - 將資料分成已排序、未排序兩部份
 - 依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置
   - 插入時由右而左比較，直到遇到第一個比正處理的值小的值，再插入
   - 比較時，若遇到的值比正處理的值大或相等，則將值往右移
