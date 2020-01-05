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
 
 ![](https://imgur.com/Gy9qm09.jpg)
 
## 為什麼要有Queue
 - 應用在其他演算法
 - Bread-First Search | 廣度優先搜尋
 - Tree 的 Level-Order Traversal | 二元樹走訪
 - 作業係統被多個程式共享資源時(例如CPU、應表機、網站伺服器)，一次只能執行一個需求，所以需要用 Queue 來安排執行順序。
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

![](https://imgur.com/undefined.jpg)

# code
學習說明
 - Queue

宣告 類別 (參數可以改object123)

定義初始化是因為宣告會有初始化過程(self)

宣告輸入的兩個stack 中括號是空的

定義 放一個元素在queue最後方(self,可以改變參數)

Push的功能

Append是加入的意思

Pop功能

如果restack裡面有元素就回傳

如果沒有元素就跳到while迴圈

語法裡面的Len=長度   

如果inputstack的長度不是0

就把裡面的值加入resstack的值

回傳到restake最前面

Peek要拿到最前面所有元素

判斷restack的-1位置是沒有元素

 - Stack

Val是參數(放資料的地方)

Nextnode(索引到下一個地方)

None是沒有值

temp是暫時的最小值

Self.next 為後面要有其他值

接著初始化

先將箱子假設一開始都是空的

所以箱子都是none

Push功能

Top目的是記最後一個位置

假設top裡面沒東西是none

Topnode= none就是(x，none)

Temp(暫時)的最後一本書位置記起來

Self.topNode = Node(x,self.topNode)把新的書放進去

接著更新最後一本書的位置

Self.topNode = self.topNode.next

若拿最上面那本書，要告訴別人下次拿的是哪一本書

Top功能

最上面那本書是什麼要回傳

getMin功能

取得top裡面最小的值算是什麼

 - Queue
 
![](https://imgur.com/IKyleLj.jpg)

![](https://imgur.com/cvSQGpc.jpg)

![](https://imgur.com/O1xaejr.jpg)

 - Stack
  
 ![](https://imgur.com/ARQQE5F.jpg)
 
 ![](https://imgur.com/61KlSfm.jpg)

## 參考資料
https://www.youtube.com/watch?time_continue=4&v=wjI1WNcIntg&feature=emb_title

https://leetcode.com/problems/min-stack/

https://realpython.com/how-to-implement-python-stack/

https://leetcode.com/problems/implement-queue-using-stacks/

https://github.com/pecu/DSA/tree/master/02_Stack%26Queue

老師講義
