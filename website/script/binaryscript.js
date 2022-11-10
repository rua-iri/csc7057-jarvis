
//function that animates the binary values like an equalizer 
function equalize() {

    //loop through each column
    for (let x = 0; x < 6; x++) {

        //set all elements as visible
        for (let i = 0; i < 7; i++) {
            const elemId = "col-" + String(i) + "-" + String(x);
            elem = document.getElementById(elemId);
            elem.style = "visibility: visibile";
        }

        //generate a random number between 1 and 6
        const randIndex = Math.floor(Math.random() * 7);

        //set all elements until randIndex hidden
        for (let i = 0; i <= randIndex; i++) {
            const elemId = "col-" + String(i) + "-" + String(x);
            elem = document.getElementById(elemId);
            elem.style = "visibility: hidden";
        }


    }

}


//run function once at the beginning
equalize();

//run function every quarter of a second
setInterval(equalize, 250);