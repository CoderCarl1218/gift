frappe.ready(function () {
  document.addEventListener("DOMContentLoaded", function () {
    // Change the color of all input fields when focused
    const inputs = document.querySelectorAll("input, textarea");
    inputs.forEach((input) => {
      input.addEventListener("focus", function () {
        input.style.backgroundColor = "yellow"; // Light blue on focus
      });
      input.addEventListener("blur", function () {
        input.style.backgroundColor = "green"; // Reset to light grey
      });
    });
  });
});
