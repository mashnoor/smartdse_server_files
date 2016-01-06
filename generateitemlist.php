<?php
ini_set('display_errors', 1); 
error_reporting(E_ALL);
ini_set('precision', 3);
require_once("table2arr.php");

//Get DSEX Items
$ch = curl_init("http://www.dsebd.org/dseX_share.php");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_BINARYTRANSFER, true);
$h = curl_exec($ch);
curl_close($ch);

//Get All Items

$ch = curl_init("http://localhost/dev/smartdsefiles/allitems.txt");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_BINARYTRANSFER, true);
$for_extra_item = curl_exec($ch);
curl_close($ch);
$for_extra_item = var_export(json_decode($for_extra_item, true), true);
$for_extra_item = eval("return $for_extra_item;");


$total_item_size = count($for_extra_item);
$g= new table2arr($h);
$cnt=$g->tablecount;


 
 for($i=0;$i<$cnt;$i++)
 {
 if (!$g->table[$i]["parent"])
 // if not parent, not she has child table
    {
 //print "---cells of table $i----\n";
 $g->getcells($i);
    $z = var_export($g->cells, true);
    $z = eval("return $z;");
    if(isset($z['0']['1']))
    {
    	 if ($z['0']['1'] == "TRADING CODE") {
    	//echo($i);
    	break;
    }
    }
   
    
    }
 }
 function removeElementWithValue($array, $key, $value){
     foreach($array as $subKey => $subArray){
          if($subArray[$key] == $value){
               unset($array[$subKey]);
          }
     }
     return $array;
}


$final_array = array();
$final_array_portfolio=array();
 for ($i=1; $i <=229 ; $i++) { 
 	if (isset($z[$i]['1'])) {
 		
 	
	$temp_array = array();
	$temp_array_portfolio = array();
	$temp_array['company'] = $z[$i]['1'];
	$temp_array_portfolio['company'] = $z[$i]['1'];
	$ltp = str_replace(",", "", $z[$i]['2']);
	$temp_array['value'] = $z[$i]['9'];
	$temp_array['lastTrade'] = $ltp;
	$temp_array_portfolio['lastTrade'] = $ltp;
	$temp_array['changePercent'] = $z[$i]['7'];
	$temp_ycp = str_replace(",", "", $z[$i]['6']);
	$ycp = floatval($temp_ycp);
	$temp_ltp = str_replace(",", "", $z[$i]['2']);
	$ltp = floatval($temp_ltp);
	$temp_array['changeAmount'] = ((string) ($ltp-$ycp));
	array_push($final_array, $temp_array);
	array_push($final_array_portfolio, $temp_array_portfolio);
	$for_extra_item = removeElementWithValue($for_extra_item, "company", $z[$i]['1']);
	
	}
}
	$file_name = "/var/www/html/dev/smartdsefiles/itemvalues.txt";
	//file_put_contents($file, json_encode($final_array));
	$file = fopen($file_name,"w");
	fwrite($file,json_encode($final_array));
	fclose($file);

		
	
	//Parse the extra items
	$for_item_deatil = array();
	for($i = 0; $i <$total_item_size; $i++)
	{
		if (isset($for_extra_item[$i]['company'])) {
			$temp_for_item_detail = array();
			
			$curr_item = $for_extra_item[$i]['company'];
			$temp_for_item_detail['company'] = $curr_item;
			array_push($for_item_deatil, $temp_for_item_detail);
			


			//$curr_data = file_get_contents("http://localhost/dev/smartdsefiles/dsex_items/$curr_item.txt");
			$ch = curl_init("http://localhost/dev/smartdsefiles/dsex_items/$curr_item.txt");
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($ch, CURLOPT_BINARYTRANSFER, true);
			$curr_data = curl_exec($ch);
			curl_close($ch);
			
			
			$curr_data = var_export(json_decode($curr_data, true), true);
			$curr_data = eval("return $curr_data;");
			
			
			$temp_array = array();
			$temp_array_portfolio = array();
			$temp_array['company'] = $curr_item;
			$temp_array_portfolio['company'] = $curr_item;
			$temp_array['value'] = "n-a";
			$tmp_ltrade = str_replace(",", "", $curr_data['0']['data21']);
			
			if($tmp_ltrade=="")
			{
			$temp_array['lastTrade'] = "Not Traded Today";
			$temp_array_portfolio['lastTrade'] = "Not Traded Today";
			}
			else
			{
			$temp_array['lastTrade'] = str_replace(",", "", $curr_data['0']['data21']);
			$temp_array_portfolio['lastTrade'] = str_replace(",", "", $curr_data['0']['data21']);
			}

			
			

			$temp_array['changePercent'] = str_replace("%", "", $curr_data['0']['data23']);
			

			$temp_array['changeAmount'] = $curr_data['0']['data22'];
			
			
			
			array_push($final_array, $temp_array);
			array_push($final_array_portfolio, $temp_array_portfolio);

			/*
			
			echo($curr_item . "<br>")
			
			$curr_data = var_export(json_decode($curr_data, true), true);
			$curr_data = eval("return $curr_data;");

			
			$temp_array = array();
			$temp_array['company'] = $curr_item;
			$temp_array['value'] = "n/a";
			$temp_array['lastTrade'] = $curr_data['data21'];
			$temp_array['changePercent'] = $curr_data['data23'];
			$temp_array['changeAmount'] = $curr_data['data22'];
			array_push($final_array, $temp_array);
			array_push($final_array_portfolio, $temp_array);
			*/
		}
	}
	function array_sort_by_column(&$arr, $col, $dir = SORT_ASC) {
    $sort_col = array();
    foreach ($arr as $key=> $row) {
        $sort_col[$key] = $row[$col];
    }

    array_multisort($sort_col, $dir, $arr);
}

array_sort_by_column($final_array, 'company');
	
	
	
	
	
	
 
 

 //Write All
$file_all = "/var/www/html/dev/smartdsefiles/itemvalues_all.txt";
	//file_put_contents($file, json_encode($final_array));
$file = fopen($file_all,"w");
	fwrite($file,json_encode($final_array));
	fclose($file);

$file_portfolio = "/var/www/html/dev/smartdsefiles/itemvalues_portfolio.txt";
$file_item_detail_extra = "/var/www/html/dev/smartdsefiles/item_values_extra.txt";
//Write Item Detail Extra
//file_put_contents($file_item_detail_extra, json_encode($for_item_deatil));
$file = fopen($file_item_detail_extra,"w");
	fwrite($file,json_encode($for_item_deatil));
	fclose($file);

//Write for portfolio
$file = fopen($file_portfolio,"w");
	fwrite($file,json_encode($final_array_portfolio));
	fclose($file);
//file_put_contents($file_portfolio, json_encode($final_array_portfolio));

 
 


?>
