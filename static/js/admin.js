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
var modal_rej = document.getElementById('simpleModal_rej');
// Get open modal button
var modalBtn_rej = document.getElementById('modalBtn_rej');
// Get close button
var closeBtn_rej = document.getElementsByClassName('closeBtn_rej')[0];

// Listen for open click
modalBtn_rej.addEventListener('click', openModal_rej);
// Listen for close click
closeBtn_rej.addEventListener('click', closeModal_rej);
// Listen for outside click
window.addEventListener('click', outsideClick_rej);

// Function to open modal
function openModal_rej() {
  modal_rej.style.display = 'block';
}

// Function to close modal
function closeModal_rej() {
  modal_rej.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick_rej(e) {
  if (e.target == modal_rej) {
    modal_rej.style.display = 'none';
  }
}
