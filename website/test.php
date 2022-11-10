<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <h1>hello world</h1>

    <button onclick="showls()">Button</button>

    <div id="feed">

    </div>


    <script>

        function showls() {

            let xhr = new XMLHttpRequest()

            xhr.open('GET', 'https://restcountries.com/v3.1/all', true)

            xhr.onload = function() {

                if(xhr.status==200) {
                    console.log("It worked")
                    let countries = JSON.parse(this.response)

                    countries.forEach(country => {
                        const cntryCard = document.createElement("div")
                        const cntryCardImg = document.createElement("div")
                        cntryCard.innerHTML = country.name.common
                        cntryCardImg.innerHTML = country.flag

                        cntryCard.appendChild(cntryCardImg)

                        document.getElementById("feed").appendChild(cntryCard)

                    })
                }
            }

            xhr.send();
        }


    </script>

</body>

</html>