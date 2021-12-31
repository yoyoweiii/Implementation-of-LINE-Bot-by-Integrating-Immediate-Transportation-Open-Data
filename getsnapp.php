<?php

	require "sql.php";
	$fdir='D:\\XAMPP\\htdocs\\snapp\\';// 開啟檔案的位置
	$key='AIzaSyDPpUFIkAkeHbkoPp1bwtua4CPXnpkW0PA'; // key 在  google developer console 申請
	
	set_time_limit(100);
	for($i=0,$c=0;$c<500;$i++){ // 連續做500次
		$errW = fopen('errors.txt','a');
		$snapp=[];
		
	if(!file_exists($fdir.$roads[$i][0].".txt")){ // 沒有 roadID.txt 才執行
		$c+=1; // 成功後計入一次
		$str = "";
		$sx = $roads[$i][2]; $sy = $roads[$i][1]; $ex = $roads[$i][4]; $ey = $roads[$i][3];
		
		$start = $sy.",".$sx; // 起點
		$end = $ey.",".$ex; // 終點
		$location = $start."|".$end;
		$opstr = "https://roads.googleapis.com/v1/snapToRoads?path=".$location.
		"&interpolate=true&key=".$key; // 呼叫貼齊道路API
	
		try{
		$content = file_get_contents($opstr);
		$js = json_decode($content);// 解析Json
		if(property_exists($js,'warningMessage')){ // 若有 warning message 就是貼齊失敗
			fwrite($errW,$i.' '.$js->warningMessage."\r\n");
		}
		else{
		for($ii = count($js->snappedPoints)-1;$ii>=0;$ii-=1){ // 將結果處理後存入 roadID.txt
			$str .=
				"{lat: ".$js->snappedPoints[$ii]->location->latitude.
				", lng: ".$js->snappedPoints[$ii]->location->longitude."}";
			if($ii>0)$str.=",";
				}
				
		$rW = fopen($fdir.$roads[$i][0].".txt","w"); 
		fwrite($rW,$str);
		fclose($rW);
		}
		}catch (Exception $e){
		var_dump($e);
		}
		time_nanosleep(0,10000000); // 這個API有每秒50每天2500次CALL的上限
	} //end if
		fclose($errW);
	}//end loop
	
	
	
?>
