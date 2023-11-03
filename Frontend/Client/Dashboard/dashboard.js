

// JavaScript code to add rows to the table
/*function addReservationRow(roomType, numGuests, checkInDate, checkOutDate) {
    // Get a reference to the table's <tbody>
    const tableBody = document.querySelector("#user-table tbody");

    // Create a new row and cells
    const newRow = document.createElement("tr");
    const roomCell = document.createElement("td");
    const guestsCell = document.createElement("td");
    const checkInCell = document.createElement("td");
    const checkOutCell = document.createElement("td");
    const cancelCell = document.createElement("td");

    // Set the cell contents with the provided data
    roomCell.textContent = roomType;
    guestsCell.textContent = numGuests;
    checkInCell.textContent = checkInDate;
    checkOutCell.textContent = checkOutDate;

    // Create a cancel button for the "Cancel" column
    const cancelBtn = document.createElement("button");
    cancelBtn.textContent = "Cancel";
    cancelBtn.addEventListener("click", function() {
        // Add logic to cancel the reservation when the button is clicked
        // You can remove the row from the table or handle the cancellation as needed.
        newRow.remove(); // This example removes the row when the "Cancel" button is clicked.
    });

    // Append the cancel button to the "Cancel" cell
    cancelCell.appendChild(cancelBtn);

    // Append the cells to the row and the row to the table's <tbody>
    newRow.appendChild(roomCell);
    newRow.appendChild(guestsCell);
    newRow.appendChild(checkInCell);
    newRow.appendChild(checkOutCell);
    newRow.appendChild(cancelCell);
    tableBody.appendChild(newRow);
}

// Example usage:
addReservationRow("Standard Room", 2, "2023-11-15", "2023-11-20");
addReservationRow("Deluxe Suite", 3, "2023-12-01", "2023-12-07");
addReservationRow("Standard Room", 2, "2023-11-15", "2023-11-20");
addReservationRow("Deluxe Suite", 3, "2023-12-01", "2023-12-07");
*/

// JavaScript code to add rows to the table
/*function addReservationRow(roomType, numGuests, checkInDate, checkOutDate) {
    // Get a reference to the table's <tbody>
    const tableBody = document.querySelector("#user-table tbody");

    // Create a new row and cells
    const newRow = document.createElement("tr");
    const roomCell = document.createElement("td");
    const guestsCell = document.createElement("td");
    const checkInCell = document.createElement("td");
    const checkOutCell = document.createElement("td");
    const cancelCell = document.createElement("td");

    // Set the cell contents with the provided data
    roomCell.textContent = roomType;
    guestsCell.textContent = numGuests;
    checkInCell.textContent = checkInDate;
    checkOutCell.textContent = checkOutDate;

    // Create a cancel button for the "Cancel" column
    const cancelBtn = document.createElement("button");
    cancelBtn.textContent = "Cancel";
    cancelBtn.addEventListener("click", function() {
        removeRow(newRow);
    });

    // Append the cancel button to the "Cancel" cell
    cancelCell.appendChild(cancelBtn);

    // Append the cells to the row
    newRow.appendChild(roomCell);
    newRow.appendChild(guestsCell);
    newRow.appendChild(checkInCell);
    newRow.appendChild(checkOutCell);
    newRow.appendChild(cancelCell);

    // Append the row to the table's <tbody>
    tableBody.appendChild(newRow);

    // Show the table row
    document.getElementById("empty-message").style.display = "none";
}

// Function to remove a row
function removeRow(row) {
    row.remove();
    
    // Check if there are no rows in the table, and if so, display the message row
    const tableRows = document.querySelectorAll("#user-table tbody tr");
    if (tableRows.length === 0) {
        document.getElementById("empty-message").style.display = "table-row";
    }
}

// Example usage to add rows
addReservationRow("Standard Room", 2, "2023-11-15", "2023-11-20");
addReservationRow("Deluxe Suite", 3, "2023-12-01", "2023-12-07");
addReservationRow("Economy Room", 1, "2023-11-25", "2023-11-27");

// Example usage to remove a row
const cancelButton = document.createElement("button");
cancelButton.textContent = "Cancel";
cancelButton.addEventListener("click", function() {
    removeRow(newRow);
});
*/
// JavaScript code to add rows to the table

/*function addReservationRow(roomType, numGuests, checkInDate, checkOutDate) {
    // Get a reference to the table's <tbody>
    const tableBody = document.querySelector("#user-table tbody");

    // Create a new row and cells
    const newRow = document.createElement("tr");
    const roomCell = document.createElement("td");
    const guestsCell = document.createElement("td");
    const checkInCell = document.createElement("td");
    const checkOutCell = document.createElement("td");
    const cancelCell = document.createElement("td");

    // Set the cell contents with the provided data
    roomCell.textContent = roomType;
    guestsCell.textContent = numGuests;
    checkInCell.textContent = checkInDate;
    checkOutCell.textContent = checkOutDate;

    // Create a cancel button for the "Cancel" column
    const cancelBtn = document.createElement("button");
    cancelBtn.textContent = "Cancel";
    cancelBtn.addEventListener("click", function() {
        removeRow(newRow);
    });

    // Append the cancel button to the "Cancel" cell
    cancelCell.appendChild(cancelBtn);

    // Append the cells to the row
    newRow.appendChild(roomCell);
    newRow.appendChild(guestsCell);
    newRow.appendChild(checkInCell);
    newRow.appendChild(checkOutCell);
    newRow.appendChild(cancelCell);

    // Append the row to the table's <tbody>
    tableBody.appendChild(newRow);

    // Show the table row
    document.getElementById("empty-message").style.display = "none";
}

// Function to remove a row
function removeRow(row) {
    const tableBody = document.querySelector("#user-table tbody");
    row.remove();

    // Check if there are no rows left in the table after removal
    if (tableBody.rows.length === 0) {
        document.getElementById("empty-message").style.display = "contents";
    }
}

// Example usage to add rows
addReservationRow("Standard Room", 2, "2023-11-15", "2023-11-20");
addReservationRow("Deluxe Suite", 3, "2023-12-01", "2023-12-07");
addReservationRow("Economy Room", 1, "2023-11-25", "2023-11-27");

// Example usage to remove a row
const cancelButton = document.createElement("button");
cancelButton.textContent = "Cancel";
cancelButton.addEventListener("click", function() {
    removeRow(newRow);
});
*/


// JavaScript code to add rows to the table
function addReservationRow(roomType, numGuests, checkInDate, checkOutDate) {
  const tableBody = document.querySelector("#user-table tbody");

  const newRow = document.createElement("tr");
  const roomCell = document.createElement("td");
  const guestsCell = document.createElement("td");
  const checkInCell = document.createElement("td");
  const checkOutCell = document.createElement("td");
  const cancelCell = document.createElement("td");

  roomCell.textContent = roomType;
  guestsCell.textContent = numGuests;
  checkInCell.textContent = checkInDate;
  checkOutCell.textContent = checkOutDate;

  const cancelBtn = document.createElement("button");
  cancelBtn.textContent = "Cancel";
  cancelBtn.addEventListener("click", function() {
    removeRow(this.closest("tr"));
  });

  cancelCell.appendChild(cancelBtn);

  newRow.appendChild(roomCell);
  newRow.appendChild(guestsCell);
  newRow.appendChild(checkInCell);
  newRow.appendChild(checkOutCell);
  newRow.appendChild(cancelCell);

  tableBody.appendChild(newRow);

  document.getElementById("empty-message").style.display = "none";
}

// Function to remove a row
function removeRow(row) {
  const tableBody = row.parentNode;

  // Show a confirmation prompt
  const confirmation = confirm("Are you sure you want to cancel this booking?");

  // If the user clicks "Yes", remove the row
  if (confirmation) {
    tableBody.removeChild(row);
  }
}

// Example usage to add rows
addReservationRow("Standard Room", 2, "2023-11-15", "2023-11-20");
addReservationRow("Deluxe Suite", 3, "2023-12-01", "2023-12-07");
addReservationRow("Economy Room", 1, "2023-11-25", "2023-11-27");




