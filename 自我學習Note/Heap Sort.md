## Heap Sort
分成Min Heap 跟Max Heap。

將Max-Heap Sort的結果push到stack，最後在pop。使用Min-Heap Sort輸出。

![](https://imgur.com/zYDTsIB.jpg)

![](https://imgur.com/LzJ8hxW.jpg)

## Heap的特點

以陣列表示，但是以完全二元樹的方式理解。

唯一能夠同時最優地利用空間和時間的方法——最壞情況下也能保證使用 2N \log N2NlogN 次比較和恒定的額外空間。

不穩定的排序：排序後，相同鍵值的元素相對位置有可能被改變。

原地排序：不需花費而外的儲存空間來排序。

較差的CPU快取：heap不連續存取位址，所以較不利於的CPU快取。

在索引從0開始的陣列中：

父節點 i 的左子節點在位置(2*i+1)

父節點 i 的右子節點在位置(2*i+2)

子節點 i 的父節點在位置floor((i-1)/2)

## 初等排序法
 - Selection sort
 - Insertion sort
 - Bubble sort
 
## 高等排序法
 - Heap sort
 - Quick sort
 - Merge sort
 
 ## 參考資料
 
 https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort
 
 https://www.youtube.com/watch?time_continue=353&v=H5kAcmGOn4Q&feature=emb_title
 
 相關書籍及簡報
