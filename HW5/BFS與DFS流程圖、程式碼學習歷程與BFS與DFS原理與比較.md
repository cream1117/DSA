#流程圖
##BFS
![](https://imgur.com/xrCBIB8.jpg)

設1為起點，而我的目標頂點為6。
使用BFS開始尋找目標頂點。
紅色為現在搜尋到哪個位置。
綠色為下一步可以有哪些選項，而我假設了2為我的搜尋選項。
藍色為搜尋完畢的路線。
走到第七步找到我的目標頂點6，結束搜尋。

##DFS
![](https://imgur.com/Ec4p3Pd.jpg)

設1為起點，而我的目標頂點為9。
使用DFS開始尋找目標頂點。
紅色為現在搜尋到哪個位置。
藍色為下一步有哪些選項。
紫色為搜尋完畢的路線。
走到第十步搜尋到我的目標頂點9，結束搜尋。


#學習歷程
BFS、DFS一開始我先看老師上課教的，把路線圖搞懂之後，
我在上網查詢相關資料，先試著自己設定題目，再把路線用圖畫出來，
像是我的流程圖，後來我就開始研究網路上相關的程式碼，
先學怎麼建立一個圖表，在設定數字及我自己的路線，前面設定其實蠻順暢的，
可是遇到後面需要把路線轉變成程式碼卡很久，參考了很多網路資料，最後才成功。

#BFS原理:廣度優先搜尋法，是一種圖形搜尋演算法。在搜尋頂點的時候，優先搜尋離起點較近的頂點。若是目標頂點離起點很近，搜尋快就會結束。
#DFS原理:深度優先搜尋法，屬於圖形搜尋演算法。在搜尋頂點的時候，先探查單一路徑，直到無法繼續前進的時候，再折返探查下一個選項路徑。
#BFS與DFS比較
兩者演算法差異為搜尋順序的點要設定哪個為起點，BFS是從鄰近的頂點開始搜尋，選擇最早被加入選項的頂點；DFS是一直開發新的路徑不折返，也是選擇最晚被加入的頂點。BFS會把狀態加入佇列，因此通常需要與狀態數成正比的記憶體空間。DFS是與遞迴深度成正比的，DFS更加省記憶體。

#參考資料
http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2
相關書籍
程式碼參考資料
https://www.youtube.com/watch?v=GFlthbUd7LQ&feature=youtu.be
https://www.youtube.com/watch?v=pcKY4hjDrxk
https://www.youtube.com/watch?v=97poC-xlLbA
https://www.youtube.com/watch?v=QVcsSaGeSH0
https://www.programiz.com/dsa/graph-dfs
https://www.youtube.com/watch?v=zaBhtODEL0w


