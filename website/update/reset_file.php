<?php

include("../layout/constants.php");

//get the file's name and its absolute path
$fileName = htmlentities($_GET['doc']);
$filePath = $path . $dir_name . $fileName;

//get the absolute path of the backup file
$bakPath = $path . "jarvis_backup/" . $fileName;


//delete the file and copy the original file 
//from the backup directory to the main jarvis directory
copy($bakPath, $filePath);

//redirect to the code editor page
header("Location: /document.php?doc=".$fileName);

?>