<?php

include("../layout/constants.php");


if ($_SERVER["REQUEST_METHOD"]=="POST") {
    $new_document_text = $_POST['doc_text'];
    $document_name = $_POST['doc_name'];

    //unset the $_POST variables
    unset($_POST['doc_text']);
    unset($_POST['doc_name']);
    
    $full_path = $path.$dir_name.$document_name;
}


if (isset($document_name) && isset($new_document_text)){
    echo $full_path;
    echo "<br>";
    echo $new_document_text;

    //open file
    $file_for_edit = fopen($full_path, "w") or die("can't open file");

    //write text to file
    fwrite($file_for_edit, $new_document_text);

    //close the file
    fclose($file_for_edit);

    //redirect user back to the document editor
    //after document has been updated
    header("Location: ../document.php?doc=$document_name");
}

?>
