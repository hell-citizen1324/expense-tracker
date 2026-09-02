function goToMenu() {
    window.location.href = "../menu.html";
}
const amountInput =
    document.getElementById("amount");

const tagInput =
    document.getElementById("tag");

const addButton =
    document.getElementById("add-expense");


addButton.addEventListener("click", () => {

    const amount = amountInput.value;
    const tag = tagInput.value;

    const expense = {
        amount: Number(amount),
        tag: tag
    };

    fetch("/expenses", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(expense)
    })
        .then(response => response.json())
        .then(data => {
            goToMenu();
        });
});
