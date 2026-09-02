const idInput =
    document.getElementById("expense-id");

const deleteButton =
    document.getElementById("delete-expense");

const message =
    document.getElementById("message");


deleteButton.addEventListener("click", () => {

    const expenseId = idInput.value.trim();

    if (expenseId === "") {
        message.textContent = "Please enter an expense ID.";
        return;
    }

    fetch(`/expenses/${expenseId}`, {
        method: "DELETE"
    })
        .then(response => response.json())
        .then(data => {

            message.textContent = data;

        })
        .catch(error => {

            console.error(error);

            message.textContent =
                "Error deleting expense.";

        });

});


function goToMenu() {
    window.location.href = "../menu.html";
}