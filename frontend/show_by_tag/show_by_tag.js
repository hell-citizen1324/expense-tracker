const tagInput =
    document.getElementById("tag");

const searchButton =
    document.getElementById("search");

const expensesContainer =
    document.getElementById("expenses");


searchButton.addEventListener("click", () => {

    const tag = tagInput.value.trim();

    if (tag === "") {
        expensesContainer.textContent =
            "Please enter a tag.";

        return;
    }

    fetch(`/expenses/tag/${encodeURIComponent(tag)}`)
        .then(response => response.json())
        .then(data => {

            expensesContainer.innerHTML = "";

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

});


function goToMenu() {
    window.location.href = "../menu.html";
}