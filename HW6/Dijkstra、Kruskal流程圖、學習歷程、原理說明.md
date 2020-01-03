# Dijkstra、Kruskal流程圖
# 學習歷程
一開始上網尋找Dijkstra跟Kruskal演算法時，發現好像很少見，比其他演算法還少見，網路資訊及相關書籍裡面都沒有這種演算法詳細介紹。
一開始先看懂助教的規定及測資，在開始摸索演算法，在摸索演算法前，我自行畫出流程圖，發現流程圖真的會讓我思緒更加清楚，讓我在參考程式碼時，可以比較快看懂意思，也比較好吸收，最後一步一步才成功打出code。
# 原理說明
##Dijkstra:戴克斯特拉算法，使用了廣度優先搜尋解決賦權有向圖的單源最短路徑問題。最短路徑是圖論演算法中的常見問題，分為有向圖、無向圖，路徑權值也有正值、負值之分， 而針對無向圖與正權值路徑條件，就應該選擇戴克斯特拉算法。
##程式碼: https://www.youtube.com/watch?v=Zd27SysrXUc
https://www.youtube.com/watch?v=IG1QioWSXRI&t=359s
https://www.youtube.com/watch?v=LpJceTbzJFo
##Kruskal:克魯斯克爾演算法是一種用來尋找最小生成樹的演算法。是以增加邊的觀念做為出發點。先將所有的邊按權值大小排序，再來依照最小的邊開始，如果造成cycle時，則必須捨棄，直到增加了n - 1條邊為止，直到圖中所有節點都連通，就找到連通圖的最小生成樹。
##程式碼: https://king39461.pixnet.net/blog/post/345213661
       http://puremonkey2010.blogspot.com/2010/10/kruskal.html
       https://www.itread01.com/content/1545258433.html

# 流程圖及原理參考資料: 
https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95
https://www.itread01.com/content/1546894278.html
https://www.itread01.com/content/1546379676.html
https://ithelp.ithome.com.tw/articles/10209593
https://wiki.mbalib.com/zh-tw/Dijkstra%E7%AE%97%E6%B3%95
https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95
http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/kruskal.html
https://itw01.com/UNFNQEJ.html


