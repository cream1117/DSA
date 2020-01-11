## Merge Sort

屬於 Divide and Conquer 演算法，把問題先拆解(divide)成子問題

並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題。

運算方法: 
 分割：以遞迴的方式每次以len(lest)/2把目前序列平分為兩半。
 排序: 在進行倆倆比較後，以排序的方式儲存。
 整合：在保持元素順序的前提下，將子序列進行合併。
 
可分兩種類型: 
 - 遞迴 Recursive 遞迴合併排序
 
 ![](https://imgur.com/u03Ksfh.jpg)

 - 迴圈 Iterative 非遞迴合併排序
 
 ![](https://imgur.com/OboJQEU.jpg)

 - Merge Sort
  
 ![](https://imgur.com/DknXZQA.jpg)

## 參考資料

https://www.c-programming-simple-steps.com/merge-sort.html

https://www.youtube.com/watch?time_continue=64&v=s8kQm8yhZ8U&feature=emb_title

https://www.youtube.com/watch?v=JSceec-wEyw
