const guessBtn = document.getElementById("guessBtn");
const result = document.getElementById("result");

guessBtn.addEventListener("click", async function () {

    result.innerText = "Generating number...";

    try {
        const response = await fetch("/guess");

        const data = await response.json();

        result.innerText = "Your Number: " + data.number;

    } catch (error) {
        result.innerText = "Error connecting to server!";
        console.error(error);
    }

})
