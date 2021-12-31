# Implementation-of-LINE-Bot-by-Integrating-Immediate-Transportation-Open-Data
map部分說明.txt
擁有存取權的使用者
未共用
系統屬性
類型
文字
大小
1 KB
儲存空間使用量
1 KB
位置
code
擁有者
我
上次修改日期
我於 2018年2月8日修改過
上次開啟日期
我於 上午11:30開啟過
建立日期
2018年2月8日 (使用 Google Drive Web)
新增說明
檢視者可以下載

在以下網址開啟
http://ts.thu.edu.tw/map.php
http://vegetible.ithu.tw/map.php

 由於不是https，用chorome開啟會無法自動定位

使用到以下檔案
map.php ( 使用者開啟的網頁 )
sql.php ( 從資料庫撈資料 )
getsnapp.php ( 獲得道路貼齊結果並儲存 )
roadsnapp.txt ( 將上面的貼齊結果整理起來放在這裡 )

使用 Notepad 編輯程式碼，網頁程式的php可以開原始碼(ctrl+U) debug

程式內也含有部分註解


map.php:
 參考 Google Maps API simple polyline
 https://developers.google.com/maps/documentation/javascript/examples/polyline-simple?hl=zh-tw

 yo變數裡存了道路ID、壅塞程度( 在sql.php裡處理及分類 )
 yos變數存了個別道路的繪製方法( 座標群 )

 由於有設透明度，如果把地圖zoom out看，會因道路重疊 顏色也跟著重疊，如果zoom in看就比較OK


sql.php:
 由資料庫抓資料
 ->篩選3小時內有更新的
 ->依車速區間分壅塞程度( 紅橘黃...... )


getsnapp:
 獲取貼齊道路API結果並儲存


roadsnapp.txt:

 由於當初php是在我自己電腦上用，而系統是架在學校的虛擬機上
 所以另外做出這個丟到虛擬機上
 
 格式是javascript的二維陣列:
 [			<-中括號在map.php有加了 ( yos = [ <?php echo ... ?> ] )
  array道路1[ 座標1, 座標2, 座標3...... ],
  array道路2[],
  array道路3[]
  ......
 ]
