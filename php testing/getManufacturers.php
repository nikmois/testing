<?php
header("Content-Type: application/json");
include("common.php");

//$p = GetTableWhere("products",array("Manufacturer"=>1, "ProductType"=>1));
$p = GetTableWhere("manufacturers",null);
echo json_encode($p, JSON_PRETTY_PRINT);
?>