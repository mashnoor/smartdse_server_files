<?php
ini_set('precision', 3);
require_once("table2arr.php");

$h=file_get_contents("http://dsebd.org/dse30_share.php");

$g= new table2arr($h);
$cnt=$g->tablecount;


for($i=0;$i<$cnt;$i++)
{
if (!$g->table[$i]["parent"])
// if not parent, not she has child table
   {

$g->getcells($i);
   $z = var_export($g->cells, true);
    $z = eval("return $z;");
    if ($z[0][1] == "TRADING CODE") {
    	
    	break;
    }
   }
}


$finalarray = array();
 for ($i=1; $i <=30 ; $i++) { 
 	if (isset($z[$i][2])) {
 	
 	
 	$tmparray = array();
 	$tmparray["itemname"] = $z[$i][1];
 	$tmparray["ltp"] = str_replace(",", "", $z[$i][2]);
 	$tmparray["changepercentage"] = $z[$i][7];
 	$ycp = str_replace(",", "", $z[$i][6]);
 	$cahnge_ammount = (float) $tmparray['ltp']- $ycp;
 	$tmparray["chnageammount"] = $cahnge_ammount;
 	
 	array_push($finalarray, $tmparray);
 }

 }
 $file = "/var/www/html/dev/smartdsefiles/dse30itemgrab.txt";
 file_put_contents($file, json_encode($finalarray));


//print "--- display properties of all table -------\n";
//print_r($g->table);
//print "</pre>";

?>
