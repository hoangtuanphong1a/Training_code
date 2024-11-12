<?php 
$dbname = "mysql:host=localhost;dbname=registration";
$dbuser = "root";
$dbpass = "";

$conn = new PDO($dbname, $dbuser, $dbpass);

if (!$conn){
    echo "Not Connected to database";
} 
// else {
//     echo "Connected to database";
// }
?>