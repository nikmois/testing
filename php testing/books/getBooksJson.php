<?php
header("Content-Type: application/json");

include("common.php");

$id = -1;
if(isset($_GET["id"])) $id = $_GET["id"];

$books = GetTable("books",($id != -1) ? "id=$id" : "1=1");

echo json_encode($books, JSON_PRETTY_PRINT);
?>