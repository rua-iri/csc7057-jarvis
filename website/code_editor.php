<?php


include("layout/constants.php");
//select an array of the files in the directory
$fileAra = scandir($path . $dir_name);


?>
<!DOCTYPE html>
<html lang="en">

<head>
	<title>Jarvis Code Editor</title>
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
				<?= $dir_name ?>
			</button>

			<?php

			//loop through each file in the array
			foreach ($fileAra as $fileName) {

				//check that file is not hidden and that it is .py format
				if ($fileName[0] != "_" && $fileName[0]!="." && substr($fileName, -3, 3)==".py") {
					echo "<a class='list-group-item list-group-item-action' href='./document.php?doc=${fileName}'>";

					//alter the shape of the line depending on where a file is in the list
					if ($fileName == $fileAra[count($fileAra) - 1]) {
						echo "└── ";
					} else {
						echo "├── ";
					}

					echo $fileName;
					echo "</a>";
				}
			}

			?>
		</div>

		<div class="input-group mb-5">
			<a class="btn btn-outline-primary" href="new_document.php">
				Create new file
			</a>
			<button class="btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#reset-modal">
				Reset
			</button>
		</div>


		<div class="modal fade" tabindex="-1" id="reset-modal" aria-hidden="true">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header bg-dark text-light">
						<h3 class="fw-bold">
							Reset Jarvis
						</h3>
					</div>
					<div class="modal-body">
						<p>
							Are you sure you would like to reset Jarvis to its default configuration?
						</p>
						<p>
							Any new files will be deleted.
						</p>
						<p>
							This action cannot be undone.
						</p>
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-primary" data-bs-dismiss="modal">No</button>
						<a href="update/reset_all_files.php" class="btn btn-danger">Yes</a>
					</div>
				</div>
			</div>
		</div>

	</div>

	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>

</html>