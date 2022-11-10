<?php

include("../layout/constants.php");

$dir_path = $path. $dir_name . "notes";

$fileName = htmlentities($_GET["note"]);
$fullPath = $dir_path."/".$fileName;

echo $fullPath;

$dlt_note = unlink($fullPath);

if ($dlt_note) {
    header("Location: ../notes.php");
} else {
    echo "<br><br>Deletion Failed";
}


?>