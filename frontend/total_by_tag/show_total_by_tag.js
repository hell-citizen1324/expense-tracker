const tagInput =
    document.getElementById("tag");

const searchButton =
    document.getElementById("search");

const totalContainer =
    document.getElementById("total");


searchButton.addEventListener("click", () => {

    const tag = tagInput.value.trim();

    if (tag === "") {

        totalContainer.textContent =
            "Please enter a tag.";

        return;
    }

    fetch(
        `/expenses/tag/${encodeURIComponent(tag)}/total`
    )
        .then(response => {

            if (!response.ok) {
                throw new Error("Failed to get total.");
            }

            return response.json();
        })
        .then(data => {

            totalContainer.textContent =
                Number(data).toLocaleString();

        })
        .catch(error => {

            totalContainer.textContent =
                "Error loading total.";

            console.error(error);
        });

});


function goToMenu() {
    window.location.href = "../menu.html";
}