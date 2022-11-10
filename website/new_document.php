<?php

include("layout/constants.php");


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jarvis Code Editor | New Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>

    <?php
	    include("layout/navbar.php");
	?>

    <div class="container">

        <div>
            <form action="update/update_document.php"  method="post">
                
                <div class="input-group mt-3 mb-3">
                    <label class="input-group-text fw-bold" for=""><?=$dir_name?></label>
                    <input class="form-control" type="text" name="doc_name">
                </div>
                
                <div class="form-floating mb-3">
                    <textarea class="form-control" name="doc_text" id="" style="height: 25rem"></textarea>
                </div>
                
                <div class="input-group">
                    <input class="btn btn-outline-primary" type="submit" value="Upload">
                    <input class="btn btn-outline-danger" type="reset" value="Undo">
                </div>
            </form>
        </div>
    </div>
</body>
</html>