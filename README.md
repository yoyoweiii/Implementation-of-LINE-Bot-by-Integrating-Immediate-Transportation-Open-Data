1.	先準備一隻Line帳號以及到Line Developer申請LineBot帳號（只要有Line帳號都可以上去辦 ）
2.	在本地端部署Webhook Server也就是python的flask套件用來和Line Sever溝通，可以選擇你熟悉的程式語言像js，python或c等等。 
3.	申請domain(可以跟教授提出協助)
4.	申請ssl 使用LetsEncrypt免費軟體
5.	到伺服器設定檔裡面修改port的連接，使程式碼可以對外連線
6.	在網路上找出欲使用的資料（例如各方面的數據資料或是xx論壇等等）
7.	安裝python的butterflysoup套件跟request套件
8.	使用python爬蟲程式爬下來放上資料庫。
9.	再crontab上設定爬蟲設定美5分鐘執行一次就可以得到一直更新的資料
10.	到Line Developer放上去自己的Webhook URL。
11.	利用LINE Messaging API 實作主動推發與回覆的功能，也就是透過webhook裡面設定關鍵字偵測來決定採取甚麼動作。

高速公路路況部分:
使用者傳的訊息裡只要有highway，webhook就發送橫向式按鈕給使用者選目的地與終點，回傳地點給webhook後就可以撈資料庫裏面的高速公路訊息給使用者(像是平均車速)

高速公路攝影機部分:
同上使用者傳的訊息裡只要有camera，webhook就發送橫向式按鈕給使用者選目的地與終點，回傳地點給webhook後就可以撈資料庫裏面的高速公路訊息給使用者(攝影機的URL)

台中市路況部分:
使用者回傳經緯度後，webhook接收經緯度再去比較資料庫上的路況經緯度資料給予車速回應

台中地圖部分:
將資料庫的資料處理後，配合貼齊道路的結果，繪製於使用Google Maps API的網頁上
