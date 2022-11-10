<?php

include("../layout/constants.php");

$document_name = htmlentities($_GET['doc']);

$full_path = $path . $dir_name . $document_name;

echo $document_name;
echo "<br>";
echo $full_path;

//delete the file using the full path
$dlt_file = unlink($full_path);

//redirect to the homepage if the deletion was successful
if ($dlt_file) {
    header("Location: ../code_editor.php");
} else {
    echo "<br><br>Deletion Failed";
}
