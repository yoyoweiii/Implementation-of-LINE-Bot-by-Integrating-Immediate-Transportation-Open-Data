<?php

	$link = mysqli_connect("localhost", "root", "0000", "data");
	$sql = "SELECT `routeid`, `to_lat`, `to_lng`, `from_lat`, `from_lng`, `value` , `datacollecttime` FROM `data` ";
	$cond = "WHERE abs(`to_lat`- 24.1790108)<0.01 && ABS( `to_lng`- 120.6039384)<0.01";
	$roads = [];
	
	if (mysqli_connect_errno()) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		exit();
	}
	
	$RS = mysqli_query($link, $sql."WHERE 1");
	
	while($row=mysqli_fetch_array($RS)){
		array_push($roads,
		[$row[0],(float)$row[1],(float)$row[2],(float)$row[3],(float)$row[4],relevel($row[5],$row[6])]);
	}
	
	function relevel($speed,$time){
		
	date_default_timezone_set('Asia/Taipei');
	$t = preg_split("/\/|\s|\:/",$time); // turn 2017/12/07 09:11:33 into array
	if($time=="")return 6; // if data collect time is null -> Black
	else if	( 
		(Date('d') - $t[2])*24 + (Date('G') - $t[3]) > 3 || 
		//more than 3 hour & deal passing day 
		$t[1] != Date('m')
		//not this month
		)return 5; // if data collect time isn't today -> Blue
	
	$s = (int)$speed;
		if($s>40)return 0; // green
		//else if($s>30)return 1;
		else if($s>20)return 2; // yellow
		//else if($s>10)return 3;
		else if($s>0)return 4; // red
		else return 7; // pink
	}
	
	function echoLocation($lat,$lng){
		echo "{lat:".$lat.","."lng:".$lng."}";
	}
	
	$RS->close();
	mysqli_close($link);
?>

