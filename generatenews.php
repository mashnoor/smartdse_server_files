<?php

require_once("table2arr.php");
function grab_src($link)
{
$ch = curl_init($link);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_BINARYTRANSFER, true);
$h = curl_exec($ch);
curl_close($ch);
return $h;
}

//Write File
function mwrite($file_name, $text)
{
$file = fopen($file_name,"w");
	fwrite($file,$text);
	fclose($file);
}

$h=grab_src("http://dsebd.org/display_news.php");


$g= new table2arr($h);
$cnt=$g->tablecount;


 $newsarray = array();
 for($i=0;$i<$cnt;$i++)
 {
 if (!$g->table[$i]["parent"])
 // if not parent, not she has child table
    {
 $g->getcells($i);
    $z = var_export($g->cells, true);
    $z = eval("return $z;");
    if ($z[0][0] == "Trading Code:" && $z[1][0] == "News Title:") {
    	$temparray = array();
    	$temparray['tradingcode'] = $z[0][1];
    	$temparray['news'] = $z[2][1];
    	array_push($newsarray, $temparray);
		//echo "Trading Code: " . $z[0][1] . "<br>";
    	//echo "News: " . $z[1][1] . "<br><br>";
    	
    }

    }
 }
 $file = "/var/www/html/dev/smartdsefiles/newsgrab.txt";
 $finalstring = strip_tags(json_encode($newsarray));
 mwrite($file, $finalstring);




//print "--- display properties of all table -------\n";
//print_r($g->table);
//print "</pre>";

?>
