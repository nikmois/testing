<?php
header("Content-Type: application/json");
include("common.php");

$filter = array();

function SetFilter($field)
{
	global $filter;
	if(isset($_GET[$field]) && is_numeric($_GET[$field]))
	{
		$filter[$field] = $_GET[$field];
	}
}

SetFilter("manufacturer");
SetFilter("producttype");
SetFilter("id");

//$p = GetTableWhere("products",array("Manufacturer"=>1, "ProductType"=>1));
$p = GetTableWhere("products",$filter);
echo json_encode($p, JSON_PRETTY_PRINT);
?>