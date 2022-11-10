
//constants to change the colour
const svrOnline = "btn-success";
const svrOffline = "btn-danger";


//function to execute the reset script and restart the device
function resetJrvs() {
    const xhr = new XMLHttpRequest();

    xhr.open("GET", "/sh_exec/reset.php");

    xhr.send();

}


//function to check whether the server
//is online or not
function checkServerOnline() {


    const xhr = new XMLHttpRequest();
    const pgBtn = document.getElementById("rst-btn");


    //use POST to prevent the browser from caching check_server.txt
    xhr.open("POST", "/sh_exec/check_server.txt");

    //if file loads correctly
    xhr.onload = function () {
        pgBtn.classList.remove("btn-danger");
        pgBtn.classList.add("btn-success");

        //only change html once
        if (pgBtn.innerHTML == "Jarvis Offline") {
            pgBtn.innerHTML = "Reset Jarvis";
            pgBtn.disabled = false;
        }
    }

    //if error occurs then pi is rebooting
    xhr.onerror = function () {
        pgBtn.classList.remove("btn-success");
        pgBtn.classList.add("btn-danger");

        if (pgBtn.innerHTML == "Reset Jarvis") {
            //change the button text and disable button function
            pgBtn.innerHTML = "Jarvis Offline";
            pgBtn.disabled = true;
        }
    }

    xhr.send();


}


//check the server every quarter of a second
setInterval(checkServerOnline, 250);




