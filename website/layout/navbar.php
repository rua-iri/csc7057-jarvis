<?php

// This is the navbar to be displayed on every page

//get the current page
$currentPage = $_SERVER["REQUEST_URI"];

//store the possible pages and their urls in an associative array
$pageAra = array(
    "Code" => "/code_editor.php",
    "Notes" => "/notes.php",
    "Music" => "/music.php",
    "Settings" => "/settings.php",
    "Reset" => "/restart_jarvis.php",
);


?>
<nav class="navbar navbar-expand navbar-dark bg-dark">
    <div class="container-fluid">

        <a class="navbar-brand fs-3 fw-normal" href="/">Jarvis Voice Assistant</a>

        <ul class="navbar-nav my-2 my-lg-0">
        <?php
        //give the current page a bolder font weight

        foreach ($pageAra as $pKey => $pValue) {
            echo "<li class='nav-item'>";
            echo "<a href='${pValue}' class='nav-link fs-4 text-white fw-";

            if($pValue==$currentPage) {
                echo "normal";
            } else {
                echo "light";
            }

            echo "'>${pKey}</a>";
            echo "</li>";
        }

        ?>
        </ul>
    </div>
</nav>