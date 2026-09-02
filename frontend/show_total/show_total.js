function goToMenu() {
    window.location.href = "../menu.html";
}
const totalContainer =
    document.getElementById("total");


fetch("/expenses/total")
    .then(response => response.json())
    .then(data => {

        const total =
            data.split(":")[1].trim();

        totalContainer.textContent =
            Number(total).toLocaleString();

    });


function goToMenu() {
    window.location.href = "../menu.html";
}