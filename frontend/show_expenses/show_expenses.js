function goToMenu() {
    window.location.href = "../menu.html";
}
const expensesContainer =
    document.getElementById("expenses");


fetch("/expenses")
    .then(response => response.json())
    .then(data => {

        data.forEach(expense => {

            const expenseDiv =
                document.createElement("div");

            expenseDiv.classList.add("expense");

            expenseDiv.innerHTML = `
                <div class="expense-header">

                    <span class="expense-id">
                        #${expense[0]}
                    </span>

                    <span class="expense-tag">
                        ${expense[2]}
                    </span>

                </div>

                <div class="expense-amount">
                    ${expense[1].toLocaleString()}
                </div>

                <div class="expense-date">
                    ${expense[3]}
                </div>
            `;

            expensesContainer.appendChild(expenseDiv);
        });

    });


function goToMenu() {
    window.location.href = "../menu.html";
}