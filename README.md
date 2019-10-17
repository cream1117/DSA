# My DSA Note
## 我的個人介紹
我是一名轉系生，目前是在巨資系四年級A班
我是陳韻涵，可以叫我Cream

# week1
## github 

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
 - 插入排序法(Insertion Sort)
 - 時間複雜度(Time Complexity)
 - 空間複雜度(Space Complexity)
 - 穩定性(Stable/Unstable)

## 插入排序做法
分成已排序和未排序兩部分。依序由未排序中的第一筆為基準值(正處理的值)，插入到已排序中的適當位置。
比較後，直到遇到 第一個 < 基準值 的值，停止並插入在該值右邊。
遇到 > or = 基準值 的值，將該值往右移動，基準值繼續往前比較。

# week5
## Quick Sort
首先，快速排序法會從所有資料中選擇一個支點(pivot)(程式中選擇最右邊)，支點的挑選往往決定了快速排序法的執行效率。然後，假設我們需要將資料由小排到大，我們需要把所有小於支點的資料移動到支點之前、並把所有大於支點的資料移動到支點之後。

# week6
## Heap Sort
