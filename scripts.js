document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const input = document.querySelector('form input');
    const shelvesContainer = document.getElementById('shelves-container');
    const resultsContainer = document.getElementById('results');

    // Function to create shelves and display them
    function createShelves() {
        shelves.forEach((row, rowIndex) => {
            const shelf = document.createElement('div');
            shelf.classList.add('shelf');
            
            row.forEach((cellValue, cellIndex) => {
                const cell = document.createElement('div');
                cell.classList.add('cell');
                cell.textContent = cellValue;
                cell.dataset.index = `${rowIndex}-${cellIndex}`;
                shelf.appendChild(cell);
            });
            
            shelvesContainer.appendChild(shelf);
        });
    }

    // Function to highlight matching cells
    function highlightMatchingCells(upcSuffix) {
        // Clear previous highlights
        const highlightedCells = document.querySelectorAll('.highlight');
        highlightedCells.forEach(cell => {
            cell.classList.remove('highlight');
        });

        // Check each cell for a match and highlight it
        const cells = document.querySelectorAll('.cell');
        cells.forEach(cell => {
            if (cell.textContent.toLowerCase() === upcSuffix.toLowerCase()) {
                cell.classList.add('highlight');
            }
        });
    }

    // Handle form submission
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the page from reloading on form submission
        const upcSuffix = input.value.trim();

        if (upcSuffix) {
            // Highlight matching cells
            highlightMatchingCells(upcSuffix);

            // Display result
            const matchingCells = document.querySelectorAll('.highlight').length;
            if (matchingCells > 0) {
                resultsContainer.innerHTML = `
                    <p>Found ${matchingCells} matching cell(s) with suffix: <strong>${upcSuffix}</strong></p>
                `;
            } else {
                resultsContainer.innerHTML = `
                    <p>No matching cells found for suffix: <strong>${upcSuffix}</strong></p>
                `;
            }
        } else {
            resultsContainer.innerHTML = `<p>Please enter a valid UPC suffix.</p>`;
        }

        // Clear the input field after submission
        input.value = '';
    });

    // Initialize shelves and display them
    createShelves();
});
