## Breadth-First Search

![](https://imgur.com/Y5mBNiv.jpg)

稱作廣度優先搜尋法，是以某一節點為出發點，先拜訪所有相鄰的節點。

是一種用以搜尋graph的演算法。

graph在程式中所說的並不是指圖片或者圖形，而是一種用來記錄關聯、關係的東西。

一個graph是由數個vertex以及數條edge所構成的。Vertex之間則可以edge來連接，表示Vertex之間有關聯與關係。



BFS利用Queue作為儲存將要探索的點的資料結構。

 - BFS搜尋步驟
- 首先建立一個visit陣列和一個Queue，分別用來判斷該位置是否經過及讓未訪問過的點入隊
- 初始化visit陣列，清空Queue
- 讓起點start入隊，並使該點的visit置1
- 使用while迴圈執行搜尋操作:

1.取出隊頭元素後使隊頭元素出隊，判斷該元素是否為目標到達點

2.如果是目標點，就返回結果（最短時間、最短路徑）

3.如果不是目標點，就繼續訪問與其相鄰的位置點，將可走的相鄰的位置點入隊，並更新visit陣列

## Depth-First Search

![](https://imgur.com/i3ZLsAp.jpg)

稱作深度優先搜尋法。可用樹來表示。先把同一個路線的點採訪完回到原點，再重新走訪其他路線的點。

DFS利用Stack作為儲存已經開始探索但尚未結束的點的資料結構。

![](https://imgur.com/ylFFzId.jpg)

DFS的搜尋路線時的各自選項如上圖。

## 參考資料

https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html

老師講義
