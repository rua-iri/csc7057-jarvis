<?php

include("layout/constants.php");

$dir_path = $path . $dir_name . "notes";

$fileAra = scandir($dir_path);

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Jarvis Notes</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta name="description" content="" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>

<body>
    <?php
    include("layout/navbar.php");
    ?>

    <div class="container">

        <div class="list-group mt-3 mb-3">

            <button class="list-group-item list-group-item-action list-group-item-light text-light fw-bold bg-dark">
                Notes
            </button>

        </div>

        <div class="accordion" id="notes-accordion">

            <?php

            $fileCount = 0;

            //loop through each file in the array
            foreach ($fileAra as $fileName) {

                //check that file is not hidden
                if ($fileName[0] != "_" && $fileName[0] != ".") {
                    echo "<div class='accordion-item'>";
                    echo "<h2 class='accordion-header' id='heading${fileCount}'>";
                    echo "<button class='accordion-button collapsed' type='button' data-bs-toggle='collapse' data-bs-target='#collapse${fileCount}' aria-expanded='false' aria-controls='collapse${fileCount}'>";

                    //alter the shape of the line depending on where a file is in the list
                    if ($fileName == $fileAra[count($fileAra) - 1]) {
                        echo "└── ";
                    } else {
                        echo "├── ";
                    }

                    //convert the timestamp to a date
                    $noteStamp = str_replace("note-", "", $fileName);
                    $noteStamp = str_replace(".txt", "", $noteStamp);
                    
                    $noteDate = date("H:i - j/m/Y", intval($noteStamp));

                    
                    echo $fileName;

                    //add a space between the file name and its date
                    for ($i=0; $i<10; $i++){
                        echo "&nbsp";
                    }

                    echo "(". $noteDate . ")";
                    echo "</button></h2>";

                    $notesFile = fopen($dir_path."/".$fileName, "r");

                    echo "<div id='collapse${fileCount}' class='accordion-collapse collapse' aria-labelledby='heading${fileCount}' data-bs-parent='notes-accordion'>";
                    echo "<div class='accordion-body'>";
                    echo fread($notesFile, filesize($dir_path."/".$fileName));
                    echo "<div class='mt-4'><a class='btn btn-danger' href='update/delete_note.php?note=${fileName}'>Delete</a></div>";
                    echo "</div>";
                    echo "</div>";

                    echo "</div>";

                    fclose($notesFile);
                    $fileCount++;
                }
            }

            ?>

        </div>


    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>

</html>
