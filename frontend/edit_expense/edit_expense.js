function goToMenu() {
    window.location.href = "../menu.html";
}
const idInput =
    document.getElementById("expense-id");

const amountInput =
    document.getElementById("amount");

const tagInput =
    document.getElementById("tag");

const editButton =
    document.getElementById("edit-expense");

const message =
    document.getElementById("message");


editButton.addEventListener("click", () => {

    const expenseId = idInput.value;
    const amount = amountInput.value;
    const tag = tagInput.value;

    const expense = {
        amount: Number(amount),
        tag: tag
    };

    fetch(`/expenses/${expenseId}`, {
        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(expense)
    })
        .then(response => response.json())
        .then(data => {

            message.textContent = data;

        });

});


function goToMenu() {
    window.location.href = "../menu.html";
}