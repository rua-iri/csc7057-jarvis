<!DOCTYPE html>
<html lang="en">

<head>
	<title>Jarvis Restart</title>
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

		<div class="list-group mt-5 mb-3">

			<button class="btn btn-success fw-bold btn-lg mx-5" onclick="resetJrvs()" id="rst-btn">Reset Jarvis</button>

			<div class="container-fluid" id="bttm"></div>

		</div>

	</div>

	<script src="script/resetscript.js"></script>

	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>

</html>