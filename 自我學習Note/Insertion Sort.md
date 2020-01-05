# 插入排序法(Insertion Sort)

![](https://imgur.com/eJcIMkh.jpg)
 
## 做法

分成已排序和未排序兩部分。依序由未排序中的第一筆為基準值(正處理的值)，插入到已排序中的適當位置。

比較後，直到遇到 第一個 < 基準值 的值，停止並插入在該值右邊。

遇到 > or = 基準值 的值，將該值往右移動，基準值繼續往前比較。

## 時間複雜度:
 - Best Case：Ο(n) 
 
當資料的順序恰好為由小到大時，每回合只需比較 1
次 
 - Worst Case：Ο(n2) 

當資料的順序恰好為由大到小時，第 i 回合需比 i 次 
 - Average Case：Ο(n2) 

第 n 筆資料，平均比較 n/2 次 
 
 - 空間複雜度(Space Complexity)：θ(1) 
 
 - 穩定性(Stable/Unstable)：穩定(Stable)

 ## 各種演算法時間複雜度比較表
 
 ![](https://imgur.com/Vy2zCJz.jpg)

## 參考資料

http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php

https://www.junyiacademy.org/science/computer-science/v/insertion-sort-algorithm

https://github.com/pecu/DSA/blob/master/04_InsertionSort/insertion-sort-list.py

https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F
