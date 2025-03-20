// Function to validate email input
function validateEmail() {
  //get value of the email input field
  var email = document.getElementById("email").value;
  //get the error message element for validation
  var emailError = document.getElementById("emailError");
  //regular expression pattern to validate email format
  var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  //check if the email input is empty
  if (email === "") {
    emailError.textContent = "Email is required.";
    return false; // prevent form submission
  } else if (!emailPattern.test(email)) {
    emailError.textContent = "Invalid email format.";
    return false; // allow form submkission if email is valid
  }
  return true;
}
function showSidebar() {
  const sidebar = document.querySelector(".sidebar");
  sidebar.style.display = "flex";
}
function hideSidebar() {
  const sidebar = document.querySelector(".sidebar");
  sidebar.style.display = "none";
}
//function  that redirects to employment.html when the button is clicked
function next() {
  window.location.href = "employment.html";
}
/*calculator*/
