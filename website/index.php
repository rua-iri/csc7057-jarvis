<?php


include("layout/constants.php");
//select an array of the files in the directory
$fileAra = scandir($path . $dir_name);


?>
<!DOCTYPE html>
<html lang="en">

<head>
	<title>Jarvis Voice Assistant</title>
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
		<div class="px-4 py-5 my-5 text-center">
			<h1>
				Jarvis Voice Assistant
			</h1>
			<div class="col-lg-6 mx-auto mb-5">
				<p class="lead mb-4">
					The open source, customisable voice assistant and smart hub.
				</p>
			</div>



			<div class="card bg-dark text-white">

				<div class="container text-center card-body">
					<?php


					//array containing the word jarvis in binary
					$binAra = array("01101010", "01100001", "01110010", "01110110", "01101001", "01101001");


					//loop through each character in each string
					for ($i = 0; $i < 8; $i++) {
						echo "<div class='row'>";

						//use counter to add a unique id to each element
						$colCounter = 0;

						foreach ($binAra as $bin) {
							echo "<div class='col align-self-end binary-rows' ";
							echo "id='col-" . $i . "-" . $colCounter . "'>";
							echo $bin[$i];
							echo "</div>";
							$colCounter++;
						}

						echo "</div>";
					}

					?>
				</div>
			</div>
		</div>

	</div>

	<script src="script/binaryscript.js"></script>

	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>

</html>