# My DSA Note
 - 我的個人介紹
 
我是一名轉系生，目前是在巨資系四年級A班
我是陳韻涵，可以叫我Cream

# week1
 - github 

# week2
## 為什麼要有Linked List?
 
   1.從儲存的角度

   2.從操作的角度

   3.Block Chain

## 什麼是Linked List
 
連結串列（Linked list）是一種常見的基礎資料結構，是一種線性表，但是並不會按線性的順序儲存資料，而是在每一個節點裡存到下一個節點的指標(Pointer)。使用連結串列結構可以克服陣列連結串列需要預先知道資料大小的缺點，連結串列結構可以充分利用電腦記憶體空間，實現靈活的記憶體動態管理。

# week3
## Stack & Queue
 
   1.編譯器(word、sublime)的 undo 。

   2.網頁瀏覽器中回到上一頁功能。

   3.任何遞迴(recursion)形式的演算法都可以用 Stack 改寫，例如 Depth-First Search(DFS,深度優先搜尋)
   
## Stack必須要有的功能有哪些?
 - Push(Data): 把資料放到最上面(最新)。
 - Pop: 把資料從最上面(最新)移除。
 - Top: 回傳最上面(最新)的資料。
 - IsEmpty: 確認stack 裡面是否有資料。
 - getSize: 回傳stack 裡的資料個數。
## 為什麼要有Queue
 - 應用在其他演算法
  - Bread-First Search | 廣度優先搜尋
  - Tree 的 Level-Order Traversal | 二元樹走訪
  -作業係統被多個程式共享資源時(例如CPU、應表機、網站伺服器)，一次只能執行一個需求，所以需要用 Queue 來安排執行順序。
## Queue必須要有的功能有哪些?
 - Push(Data): 把資料放到 Queue 的後面，並更新成新的 back。
 - Pop(dequeue): 把 front 所指向的資料從 Queue 中移除，並更新front。
 - getFront: 回傳 front 所指向的資料。
 - getBack: 回傳 Back 所指向的資料。
 - IsEmpty: 確認 Queue 裡是否有資料。
 - getSize: 確認 Queue 裡的資料個數。
操作方法
 - Add 添加：如果隊列未滿，則在隊列後面插入項目 
 - Delete 刪除：如果隊列不為空，則刪除並返回隊列前面的元素 
 - IsFull（Queue）：返回 True/False(Full/Not Full) 
 - IsEmpty(Queue）：返回 True/False(Empty/Not Empty) 

# week4
 - 插入排序法(Insertion Sort)
 - 時間複雜度(Time Complexity)
 
 ![](https://imgur.com/Vy2zCJz.jpg)
 
 - 空間複雜度(Space Complexity)
 - 穩定性(Stable/Unstable)

## 插入排序做法
分成已排序和未排序兩部分。依序由未排序中的第一筆為基準值(正處理的值)，插入到已排序中的適當位置。

比較後，直到遇到 第一個 < 基準值 的值，停止並插入在該值右邊。

遇到 > or = 基準值 的值，將該值往右移動，基準值繼續往前比較。

# week5
## Quick Sort
首先，快速排序法會從所有資料中選擇一個支點(pivot)(程式中選擇最右邊)，支點的挑選往往決定了快速排序法的執行效率。

然後，假設我們需要將資料由小排到大，我們需要把所有小於支點的資料移動到支點之前、並把所有大於支點的資料移動到支點之後。

# week6
## Heap Sort
分成Min Heap 跟Max Heap。

將Max-Heap Sort的結果push到stack，最後在pop。使用Min-Heap Sort輸出。

初等排序法
 - Selection sort
 - Insertion sort
 - Bubble sort
 
高等排序法
 - Heap sort
 - Quick sort
 - Merge sort
# week7
## Merge Sort
屬於 Divide and Conquer 演算法，把問題先拆解(divide)成子問
題，並在逐一處理子問題後，將子問題的結果合併(conquer)，如
此便解決了原先的問題。

運算方法: 
 - 將陣列分割直到只有一個元素 
 - 開始兩兩合併，每次合併同時進行排序，合併出排序過的陣列 
 - 重複 2 的動作直接全部合併完成 
 
可分兩種類型: 
 - 遞迴 Recursive 
 - 迴圈 Iterative 
# week8
## Binary Tree
![](https://imgur.com/Rf5aZHp.jpg)

二元樹 
 - 可以為空的樹 
 - 不為空則具有 Root，左、右子樹 
 - 各節點與分支度介於 0 與 2 之間 
 - 左、右子樹具有次序之分(order tree) 

二元樹的種類 
 - 偏斜二元樹 Skewed Binary Tree:可分左、右偏斜樹 
 - 完滿二元樹 Full Binary Tree 
 - 完整二元樹 Complete Binary Tree 
## Binary Search Tree
可應用於資料的排序跟搜尋。

如何建立BST:輸入的資料皆與樹根比，比樹根跟小的放至左子樹，比樹根大的放至右子樹。
# week9
## Red Black Tree
紅黑樹是一種自平衡二元搜尋樹，是在電腦科學中用到的一種資料結構，典型的用途是實現關聯陣列。

紅黑樹的結構複雜，但它的操作有著良好的最壞情況執行時間，並且在實踐中高效。

特點:

(1)	每一條由root到任一個leaf的path上面，其black edges的數目是相同的。

(2)	由root到任何的leaf的path上，不可以有兩個連續的red edges。
# week10
## Hash Table
通過雜湊函式/演算法將要檢索的項與用來檢索的稱為雜湊(值）。

關聯起來，生成雜湊表。希望能將存放資料的 Table 大小降到「真正會存放進 Table 的資料的數量」，也就是「有用到的 Key 的數量」。

 雜湊的優點:
 
 不須經過事前排序、保密性高、時間複雜度O(1)
# week11
## Breadth-First Search
稱作廣度優先搜尋法，是以某一節點為出發點，先拜訪所有相鄰的節點。

BFS利用Queue作為儲存將要探索的點的資料結構。
# week12
## Depth-First Search
稱作深度優先搜尋法，同樣用於搜尋圖形G中，所有自點s開始出發，有路徑可以到達的點。

DFS利用Stack作為儲存已經開始探索但尚未結束的點的資料結構。
# week13
## Minimum Spanning Tree
最小生成樹擁有最小權重的生成樹，所有路徑相加權重為最小的。

特性:不可以造成Cycle。
# week14
## Shortest Path
找出起點到圖上各點的最短路徑，即是找出其中一棵最短路徑樹。

可以順便偵測起點是否會到達負環，然後找出其中一只負環。
