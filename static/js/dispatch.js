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
var modal_callout = document.getElementById('simpleModal-callout');
// Get open modal button
var modalBtn_callout = document.getElementById('modalBtn-callout');
// Get close button
var closeBtn_callout = document.getElementsByClassName('closeBtn-callout')[0];

// Listen for open click
modalBtn_callout.addEventListener('click', openModal_callout);
// Listen for close click
closeBtn_callout.addEventListener('click', closeModal_callout);
// Listen for outside click
window.addEventListener('click', outsideClick_callout);

// Function to open modal
function openModal_callout() {
  modal_callout.style.display = 'block';
}

// Function to close modal
function closeModal_callout() {
  modal_callout.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick_callout(e) {
  if (e.target == modal_callout) {
    modal_callout.style.display = 'none';
  }
}

// Get modal element
var modal_bolo = document.getElementById('simpleModal-bolo');
// Get open modal button
var modalBtn_bolo = document.getElementById('modalBtn-bolo');
// Get close button
var closeBtn_bolo = document.getElementsByClassName('closeBtn-bolo')[0];

// Listen for open click
modalBtn_bolo.addEventListener('click', openModal_bolo);
// Listen for close click
closeBtn_bolo.addEventListener('click', closeModal_bolo);
// Listen for outside click
window.addEventListener('click', outsideClick_bolo);

// Function to open modal
function openModal_bolo() {
  modal_bolo.style.display = 'block';
}

// Function to close modal
function closeModal_bolo() {
  modal_bolo.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick_bolo(e) {
  if (e.target == modal_bolo) {
    modal_bolo.style.display = 'none';
  }
}

// Get modal element
var modal_warrant = document.getElementById('simpleModal-warrant');
// Get open modal button
var modalBtn_warrant = document.getElementById('modalBtn-warrant');
// Get close button
var closeBtn_warrant = document.getElementsByClassName('closeBtn-warrant')[0];

// Listen for open click
modalBtn_warrant.addEventListener('click', openModal_warrant);
// Listen for close click
closeBtn_warrant.addEventListener('click', closeModal_warrant);
// Listen for outside click
window.addEventListener('click', outsideClick_warrant);

// Function to open modal
function openModal_warrant() {
  modal_warrant.style.display = 'block';
}

// Function to close modal
function closeModal_warrant() {
  modal_warrant.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick_warrant(e) {
  if (e.target == modal_warrant) {
    modal_warrant.style.display = 'none';
  }
}
