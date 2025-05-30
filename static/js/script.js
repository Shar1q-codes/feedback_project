// script.js

// Confirm script is running
console.log("✅ Feedback form script loaded.");

// Optional: Smooth scroll to form on load
document.addEventListener("DOMContentLoaded", () => {
  const formCard = document.querySelector(".form-section");
  if (formCard) {
    formCard.scrollIntoView({ behavior: "smooth" });
  }
});

// Optional: Basic client-side form validation (can expand later)
const form = document.querySelector("form");
if (form) {
  form.addEventListener("submit", function (e) {
    const name = form.querySelector("input[name='name']");
    const email = form.querySelector("input[name='email']");
    const message = form.querySelector("textarea[name='message']");

    // Basic empty-field check
    if (!name.value.trim() || !email.value.trim() || !message.value.trim()) {
      e.preventDefault();
      alert("Please fill in all required fields.");
    }
  });
}
