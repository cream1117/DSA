 - Binary Tree
 
![](https://imgur.com/BKkAjym.jpg)

## Binary Search Tree

可應用於資料的排序跟搜尋。

如何建立BST:輸入的資料皆與樹根比，比樹根跟小的放至左子樹，比樹根大的放至右子樹。

![](https://imgur.com/4bLCHlG.jpg)

- 新增

![](https://imgur.com/m4d4hcQ.jpg)


![](https://imgur.com/va51l5R.jpg)


![](https://imgur.com/oOsm9me.jpg)


![](https://imgur.com/wAWJNV0.jpg)

- 搜尋成功 or　搜尋失敗

# 補充

若是BST不平衡，會造成搜尋速率變慢。如下圖

![](https://imgur.com/hLXRht6.jpg)

若是BST樹高越矮且生長平衡，會使搜尋速度加快，不管是增加或是減少搜尋速度都會減少許多。

![](https://imgur.com/NVHwwbE.jpg)


## Red Black Tree

![](https://imgur.com/VhO53Bx.jpg)

紅黑樹是一種自平衡二元搜尋樹，是在電腦科學中用到的一種資料結構，典型的用途是實現關聯陣列。

紅黑樹的結構複雜，但它的操作有著良好的最壞情況執行時間，並且在實踐中高效。

特點:

(1)	每一條由root到任一個leaf的path上面，其black edges的數目是相同的。

(2)	由root到任何的leaf的path上，不可以有兩個連續的red edges。


## 參考資料

https://alrightchiu.github.io/SecondRound/red-black-tree-introjian-jie.html

老師講義
