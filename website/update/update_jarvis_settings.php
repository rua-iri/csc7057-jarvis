<?php

include("../layout/constants.php");

$config_dir = $path . $dir_name . "config";
$config_name = "voiceconfig.csv";

$full_path = $config_dir."/".$config_name;

$configData = $_POST["voice-select"] . "," . $_POST["rate-select"] . "," . $_POST["vol-select"] . "," . $_POST["uname-select"] . "," . $_POST["fan-select"] . "," . $_POST["light-select"];

echo $configData;

//open the configuration file and write the new data
$configFile = fopen($full_path, "w");

fwrite($configFile, $configData);

fclose($configFile);

//redirect to voice.php
header("Location: ../settings.php");
