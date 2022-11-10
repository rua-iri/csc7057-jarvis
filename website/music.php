<?php

include("layout/constants.php");

$musicDir = $path . $dir_name . "music";

$musicAra = scandir($musicDir);

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Jarvis Music</title>
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
                Music
            </button>

            <form action="update/upload_music.php" class="input-group mb-3 mt-3" method="post" enctype="multipart/form-data">
                <label for="inputFile" class="input-group-text">Upload New Song</label>
                <input type="file" name="fileUpload" id="inputFile" class="form-control">
                <input type="submit" value="Upload" class="btn btn-dark">
            </form>

            <?php
            //loop through each song in the directory
            foreach ($musicAra as $song) {

                //check that each song is not a hidden file
                if ($song[0] != ".") {
                    echo "<div class='btn-group mb-1'>";
                    echo "<button class='list-group-item list-group-item-action'>$song</button>";
                    echo "<a href='update/delete_music.php?song=${song}' class='btn btn-danger'>Delete</a>";
                    echo "</div>";
                }
            }

            ?>
        </div>


    </div>



    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>