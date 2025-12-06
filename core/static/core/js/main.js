document.addEventListener("DOMContentLoaded", function() {
    const clearBtn = document.querySelector(".clear-btn");
    const inputs = document.querySelectorAll(".search-input");

    clearBtn.addEventListener("click", function() {
        inputs.forEach(input => input.value = "");
    });
});