<?php

include("../layout/constants.php");

$musicDir = $path . $dir_name . "music";

$musicFile = htmlentities($_GET["song"]);

echo $musicFile;

//concatenate the filename and the path to get the full path to be deleted
$fullPath = $musicDir . "/" . $musicFile;

echo "<br>";
echo $fullPath;

$dltFile = unlink($fullPath);

//check that deletion was successful
if ($dltFile) {
    header("Location: ../music.php");
} else {
    echo "ERROR: Something went wrong with the deletion";
}

?>