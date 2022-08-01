<?php
$db_host = "localhost";
$db_user = "pi";
$db_pass = "c300";
$db_name = "mydb";
$link = mysqli_connect($db_host,$db_user,$db_pass,$db_name) or 
        die(mysqli_connect_error());
?>
