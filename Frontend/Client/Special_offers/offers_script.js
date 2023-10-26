const offerCards = document.querySelectorAll('.offer-card');

offerCards.forEach(card => {
    card.addEventListener('click', () => {
        alert('Click for more details or to book this offer!');
    });
});


