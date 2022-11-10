<?php

include("layout/constants.php");

//the name of the document being edited
$document_name = htmlentities($_GET["doc"]);

//combine the path and the file name, then 
//store the file's contents to a variable
$document_text = shell_exec("cat " . $path . $dir_name . $document_name);

$backupExists = file_exists($path . "jarvis_backup/" . $document_name);


?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jarvis Code Editor | <?= $document_name ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>

    <?php
    include("layout/navbar.php");
    ?>

    <div class="container">

        <div>
            <form action="update/update_document.php" method="post">
                <div class="input-group mt-3 mb-3">
                    <label class="input-group-text fw-bold" for=""><?= $dir_name ?></label>
                    <input class="form-control" type="text" name="doc_name" value="<?= $document_name ?>" readonly>
                </div>

                <div class="form-floating mb-3">
                    <textarea class="form-control" name="doc_text" id="" style="height: 25rem"><?= $document_text ?></textarea>
                </div>

                <div class="d-flex mb-3">
                    <div class="input-group">
                        <input class="btn btn-outline-primary" type="submit" value="Upload">
                        <input class="btn btn-outline-danger" type="reset" value="Undo">
                    </div>
                </div>
            </form>
            <div class="input-group">

                <?php

                // only show the reset button if the file is in the defaults folder

                if ($backupExists) {
                    echo "<button class='btn btn-outline-danger' data-bs-toggle='modal' data-bs-target='#reset-modal'>";
                    echo "Reset to Default";
                    echo "</button>";
                }
                ?>

                <button class="btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#delete-modal">
                    Delete
                </button>
            </div>
        </div>

        <div class="modal fade" tabindex="-1" id="reset-modal" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header bg-dark text-light">
                        <h3 class="fw-bold">
                            Reset <?= $document_name ?>
                        </h3>
                    </div>
                    <div class="modal-body">
                        <p>
                            Are you sure you would like to reset "<?= $document_name ?>" to its default configuration?
                        </p>
                        <p>
                            This action cannot be undone.
                        </p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">No</button>
                        <a href="update/reset_file.php?doc=<?= $document_name ?>" class="btn btn-danger">Yes</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="modal fade" tabindex="-1" id="delete-modal" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header bg-dark text-light">
                        <h3 class="fw-bold">
                            Delete <?= $document_name ?>
                        </h3>
                    </div>
                    <div class="modal-body">
                        <p>
                            Are you sure you would like to delete "<?= $document_name ?>"?
                        </p>
                        <p>
                            This action cannot be undone.
                        </p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">No</button>
                        <a href="update/delete_document.php?doc=<?= $document_name ?>" class="btn btn-danger">Yes</a>
                    </div>
                </div>
            </div>
        </div>



    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>

</html>