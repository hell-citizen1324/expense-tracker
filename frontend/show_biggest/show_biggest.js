const biggestContainer =
    document.getElementById("biggest");


fetch("/expenses/biggest")
    .then(response => response.json())
    .then(data => {

        if (data === null) {
            biggestContainer.textContent =
                "No expenses found.";
            return;
        }

        biggestContainer.innerHTML = `
        <div class="biggest-card">

            <div class="biggest-header">
    
                <span class="biggest-id">
                    #${data[0]}
                </span>

                <span class="biggest-tag">
                    ${data[2]}
                </span>
    
            </div>

            <div class="biggest-amount">
                ${data[1].toLocaleString()}
            </div>

            <div class="biggest-date">
                ${data[3]}
            </div>
    
        </div>
    `;

    });


function goToMenu() {
    window.location.href = "../menu.html";
}