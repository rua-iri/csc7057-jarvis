<?php

include("../layout/constants.php");

$musicDir = $path . $dir_name . "music";

$musicFile = $_FILES["fileUpload"];

var_dump($_FILES);


//check that file is an mp3
if ($musicFile["type"] == "audio/mpeg") {

    //move file to music directory
    $fileMove = move_uploaded_file($musicFile["tmp_name"], ($musicDir."/".$musicFile["name"]));

    //check that file has been moved successfully
    if ($fileMove) {
        header("Location: ../music.php");
    } else {
        echo "ERROR: Something went wrong with the upload...";
    }
}



?>