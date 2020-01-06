 - Spanning Tree
 
 一棵包含圖上所有點的樹，稱作該圖的生成樹

一張圖的生成樹可能會有很多種

完全連通圖才有生成樹 (不連通時，則稱為生成森林)

生成樹的權重為樹上每條邊的權重總和

## Minimum Spanning Tree

最小生成樹擁有最小權重的生成樹，所有路徑相加權重為最小的。

![](https://imgur.com/ulEQwBO.jpg)

特性:不可以造成Cycle。

## Shortest Path
最短路徑
最短路徑除了不會有cycle，還有以下兩點特徵

一、因為最短路徑不存在cycle，在共有V個vertex之Graph中，從vertex(X)走到vertex(Y)的最短路徑，至多只會包含|V|−1條edge。

而且Shortest-Path Tree退化成Linked list的時候。

二、最短路徑必定是由較小段的最短路徑所連結起來的。

![](https://imgur.com/2LT3zYX.jpg)

找出起點到圖上各點的最短路徑，即是找出其中一棵最短路徑樹。

可以順便偵測起點是否會到達負環，然後找出其中一只負環。

## 參考資料
https://www.youtube.com/watch?v=71UQH7Pr9kU&feature=emb_title

https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

老師講義
