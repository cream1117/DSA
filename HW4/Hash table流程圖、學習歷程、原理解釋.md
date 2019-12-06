# 流程圖
![](https://imgur.com/DAhcjTr.jpg)
查詢jeff喜歡什麼興趣，找出jeff在陣列裡面的第幾個箱子，求出雜湊值，用陣列的箱子個數進行Mod運算，結果是3，對應的興趣是music。
# 學習歷程
![](https://imgur.com/sxQ4z87.jpg)
一開始我先弄懂雜湊表，我查了很久的資料，也有看相關書籍，先是把書面上的雜湊表意思弄懂後我才開始上網查詢code
最一開始我先嘗試運用老師規定的套件，但發現開始定義就開始出了問題。
![](https://imgur.com/0Eeziaz.jpg)
後來中間其實卡了蠻久的，因為我不知道後面要接什麼code，
![](https://imgur.com/QD6HM1B.jpg)
所以我先看了老師提供的影片在自己上網查詢，看懂程式碼就花了蠻久的時間，不過後來完全弄懂後，打程式其實就比較順了。
![](https://imgur.com/gjU1FWr.jpg)
後來測試資料我按照ppt上面的打是可以，但是改成自己的就無法，因此測試程式碼部分還未完全弄好。
# 原理解釋
假如需要存取某資料x，則必須先將hashing function計算，得出hashing address
再到Hash Table對應的Bucket中進行存取X的動作。
## Hash table:稱為雜湊表，也稱為哈希表。為一種資料儲存與搜尋的技術。
由一組Buckets所組成，每個Buckets由一組Slot所組成，而每個Slot都可以存一筆資料紀錄。
優點是資料搜尋時，紀錄不需要事先排序；且可做資料壓縮之用;且保密性高。
## Hash function原理:
雜湊函式，也稱雜湊演算法。
## 主要特徵一:輸出的雜湊碼的數據長度不變。
## 主要特徵二:輸入相同的值必定會產生相同的輸出值。
## 主要特徵三:即使輸入的數據相似，只要有差一個位元的差異輸出值就會差異很大。
## 主要特徵四:輸入完全不同的數據時，即使機率甚低，仍有可能產生相同的雜湊碼，稱為雜湊碰撞。
## 主要特徵五:數據的輸入及輸出都是單一方向。
## 主要特徵六:決定雜湊碼的計算過程比較簡單。
常見的Hash Function有Middle Square、Mod、Folding Addition這三種。
# 參考資料
https://carlos-studio.com/2018/01/21/%E6%BC%94%E7%AE%97%E6%B3%95-%E9%9B%9C%E6%B9%8A%E8%A1%A8hash-table/
https://zh.wikipedia.org/zh-tw/%E5%93%88%E5%B8%8C%E8%A1%A8
https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8
相關書籍
