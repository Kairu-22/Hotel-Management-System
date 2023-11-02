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