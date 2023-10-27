var totalcount=5;
var roomCounts = {
    'kingbed_garden': totalcount,
    'superiorbed_garden': totalcount,
    'kingbed_pool': totalcount,
    'Deluxe': totalcount,
    'Executive': totalcount,
    'Luxury': totalcount,
    'Premium': totalcount
};

function toggleDetailsprice(roomType, price) {
    var count = roomCounts[roomType];
    var roomStatusElement = document.querySelector(`.${roomType} .Status`);
var bookingStatus=document.querySelector(`.${roomType} .book-button`);
    if (count > 1) {
        roomCounts[roomType]--;
        alert(`Room Booked With Room Price As ₹${price} Remaining rooms: ${roomCounts[roomType]}`);
    } else {
        if (roomStatusElement) {
            roomStatusElement.innerText = "Unavailable";
            bookingStatus.style.display="none";
            roomStatusElement.style.backgroundColor = "red"; 
        }
    }
}
