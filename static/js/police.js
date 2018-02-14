// Get modal element
var modal = document.getElementById('simpleModal');
// Get open modal button
var modalBtn = document.getElementById('modalBtn');
// Get close button
var closeBtn = document.getElementsByClassName('closeBtn')[0];

// Listen for open click
modalBtn.addEventListener('click', openModal);
// Listen for close click
closeBtn.addEventListener('click', closeModal);
// Listen for outside click
window.addEventListener('click', outsideClick);

// Function to open modal
function openModal() {
  modal.style.display = 'block';
}

// Function to close modal
function closeModal() {
  modal.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
}

// Get modal element
var modal_plate = document.getElementById('simpleModal-plate');
// Get open modal button
var modalBtn_plate = document.getElementById('modalBtn-plate');
// Get close button
var closeBtn_plate = document.getElementsByClassName('closeBtn-plate')[0];

// Listen for open click
modalBtn_plate.addEventListener('click', openModal_plate);
// Listen for close click
closeBtn_plate.addEventListener('click', closeModal_plate);
// Listen for outside click
window.addEventListener('click', outsideClick_plate);

// Function to open modal
function openModal_plate() {
  modal_plate.style.display = 'block';
}

// Function to close modal
function closeModal_plate() {
  modal_plate.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick_plate(e) {
  if (e.target == modal_plate) {
    modal_plate.style.display = 'none';
  }
}

// Get modal element
var modal_ticket = document.getElementById('simpleModal-ticket');
// Get open modal button
var modalBtn_ticket = document.getElementById('modalBtn-ticket');
// Get close button
var closeBtn_ticket = document.getElementsByClassName('closeBtn-ticket')[0];

// Listen for open click
modalBtn_ticket.addEventListener('click', openModal_ticket);
// Listen for close click
closeBtn_ticket.addEventListener('click', closeModal_ticket);
// Listen for outside click
window.addEventListener('click', outsideClick_ticket);

// Function to open modal
function openModal_ticket() {
  modal_ticket.style.display = 'block';
}

// Function to close modal
function closeModal_ticket() {
  modal_ticket.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick_ticket(e) {
  if (e.target == modal_ticket) {
    modal_ticket.style.display = 'none';
  }
}

// Get modal element
var modal_unit = document.getElementById('simpleModal-unit');
// Get open modal button
var modalBtn_unit = document.getElementById('modalBtn-unit');
// Get close button
var closeBtn_unit = document.getElementsByClassName('closeBtn-unit')[0];

// Listen for open click
modalBtn_unit.addEventListener('click', openModal_unit);
// Listen for close click
closeBtn_unit.addEventListener('click', closeModal_unit);
// Listen for outside click
window.addEventListener('click', outsideClick_unit);

// Function to open modal
function openModal_unit() {
  modal_unit.style.display = 'block';
}

// Function to close modal
function closeModal_unit() {
  modal_unit.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick_unit(e) {
  if (e.target == modal_unit) {
    modal_ticket.style.display = 'none';
  }
}
