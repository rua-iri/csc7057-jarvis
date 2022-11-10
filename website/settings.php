<?php

include("layout/constants.php");

$config_dir = $path . $dir_name . "config";
$config_name = "voiceconfig.csv";

$full_path = $config_dir . "/" . $config_name;

//open the configuration file and read its contents
$configFile = fopen($full_path, "r");
$configContents = fread($configFile, filesize($full_path));

//split the string on each comma
$settingData = explode(",", $configContents);

//array with all possible dialects
$voiceAra = array(
    "english" => "English",
    "en-scottish" => "English (Scottish)", "english-north" => "English (Northern)",
    "english_rp" => "English (Received Pronunciation)", "english_wmids" => "English (West Midlands)",
    "english-us" => "English (United States)", "en-westindies" => "English (West Indies)"
);


//check that array has the right number of elements
if(sizeof($settingData)==6) {
    $vDialect = $settingData[0];
    $vSpeed = $settingData[1];
    $vVolume = $settingData[2];
    $userName = $settingData[3];
    $fanLevel = $settingData[4];
    $lightLevel = $settingData[5];
} else {
    //else set values to default
    $vDialect = $voiceAra["english"];
    $vSpeed = 200;
    $vVolume = 1;
    $userName = "User";
    $fanLevel = 25.0;
    $lightLevel = 10;
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Jarvis Settings</title>
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
                Voice Settings
            </button>

            <form class="mt-3" action="update/update_jarvis_settings.php" method="POST">
                <div class="input-group mb-3">
                    <span class="input-group-text">Dialect</span>
                    <select class="form-select" name="voice-select" id="">


                        <?php

                        foreach ($voiceAra as $vKey => $vValue) {

                            echo "<option ";

                            if ($vKey == $vDialect) {
                                echo " selected";
                            }

                            echo " value='${vKey}'>${vValue}</option>";
                        }

                        ?>

                    </select>
                </div>


                <div class="col-md-4">
                    <div class="input-group mb-3">
                        <span class="input-group-text">Speed</span>
                        <input class="form-control text-center" type="number" value="<?= $vSpeed ?>" min="50" max="300" name="rate-select">
                        <span class="input-group-text">WPM</span>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-3">
                        <div class="input-group mb-3">
                            <span class="input-group-text">Volume</span>
                            <input class="form-control text-center" type="number" value="<?= $vVolume ?>" step="0.1" min="0.0" max="1.0" name="vol-select">
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="input-group mb-3">
                            <span class="input-group-text">User Name</span>
                            <input type="text" class="form-control text-center" value="<?= $userName ?>" name="uname-select">
                        </div>
                    </div>
                </div>

                <button class="list-group-item list-group-item-action list-group-item-light text-light fw-bold bg-dark mt-3">
                    Sensor Settings
                </button>

                <div class="row my-3">
                    <div class="col-md-5">
                        <div class="input-group mb-3">
                            <span class="input-group-text">Fan Activation Temperature</span>
                            <input type="number" class="form-control text-center" value="<?=$fanLevel?>" step="0.1" min="0.0", max="100.0" name="fan-select">
                            <span class="input-group-text">℃</span>
                        </div>
                    </div>
                    <div class="col-md-5">
                        <div class="input-group mb-3">
                            <span class="input-group-text">Light Activation Level</span>
                            <input type="number" class="form-control text-center" value="<?=$lightLevel?>" min="0" max="100" name="light-select">
                            <span class="input-group-text">%</span>
                        </div>
                    </div>
                </div>

                <div class="input-group">
                    <input type="submit" class="btn btn-primary" value="Update">
                </div>


            </form>









        </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>

</body>