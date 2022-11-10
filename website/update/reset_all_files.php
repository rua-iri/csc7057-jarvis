<?php

include("../layout/constants.php");

//get all files in the main and backup directory
$fileAra = scandir($path . $dir_name);
$bakAra = scandir($path . "jarvis_backup");


//loop through each file in the directory
//and delete them
foreach ($fileAra as $delFile) {
    //check that file is not hidden and that it is .py format
    if ($delFile[0] != "_" && $delFile[0]!="." && substr($delFile, -3, 3)==".py") {
        unlink($path . $dir_name . $delFile);
        echo ($path . $dir_name . $delFile);
        echo "<br>";
    }

}

echo "<br><br>";

//loop through each file in the backup directory
//and copy it to the main jarvis directory
foreach ($bakAra as $bakFile) {
    //check that file is not hidden and that it is .py format
    if ($bakFile[0] != "_" && $bakFile[0] != "." && substr($bakFile, -3, 3) == ".py") {
        copy(($path . "jarvis_backup/" . $bakFile), ($path . $dir_name . $bakFile));
        echo ($path . "jarvis_backup/" . $bakFile);
        echo "<br>";
    }
}

//redirect to the code editor page
header("Location: ../code_editor.php");

?>