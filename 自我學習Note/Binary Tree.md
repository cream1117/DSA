## Tree
 - 是由一個或多個節點所組成的有限集合 
 - 存在且只有一個稱為 root(樹根)的節點，且不存在 cycle 
 - 其餘的節點可以分割成任意正整數個(包含零個)互斥的集合:T1、...、Tn，其中每一個集合也都滿足樹的定義，這些集合又稱subtree(子樹)。 
 - 在樹中若要從 root 尋找特定 node，一定只存在一條路徑(path) 
 - Tree 不可為空 
 - 子樹間沒有交集 

![](https://imgur.com/undefined.jpg)

 - Degree of a node(節點分支度)：節點的子樹個數 Degree of A=3,B=2,E=0… 
 - Degree of a tree(樹分支度):樹中所有節點分支度最大者，即 max 
 - leaf(葉子)：分支度為 0 的節點 
 - Non-leaf Node/Non-terminal Node/Internal Node:樹中所有非葉子或是 degree>=1 的節點 
 - Parent Node(父節點):一個節點有後繼節點(successor node) 
 - Child Node(子節點):有前輩節點(Precessor node) 
 - Sibling(兄弟):同一個父節點所有的子節點可互稱 
 - Ancestor(祖先):某一個節點的祖先，乃是從樹根到該節點，所經過所有路徑的子節點 
 - 通常為集合，Ancestors C:{A,B} 
 - Level(階度):指自樹根到該節點的距離 
 - Depth/Height(高度):一顆樹各 level 值中的最大值 
 - Forest(森林):n 個互斥樹所形成的集合(n>=0)，可以為 0 
 
![](https://imgur.com/Tv1r8IC.jpg)

## Binary Tree
![](https://imgur.com/Rf5aZHp.jpg)

Tree V.S Binary Tree

![](https://imgur.com/undefined.jpg)

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

## 參考資料

https://www.youtube.com/watch?v=ikPPdBDZnz4&feature=emb_title
