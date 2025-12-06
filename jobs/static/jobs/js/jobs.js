function toggleBookmark(icon) {
    if (icon.classList.contains("fa-regular")) {
        icon.classList.remove("fa-regular");
        icon.classList.add("fa-solid");
        icon.style.color = "#0d6efd";
    } else {
        icon.classList.remove("fa-solid");
        icon.classList.add("fa-regular");
        icon.style.color = "#444";
    }
}

document.addEventListener("DOMContentLoaded", () => {

    const jobCards = document.querySelectorAll(".job-card");
    
    // NEW: Initialize left-side bookmark icons based on SAVED_JOBS
    jobCards.forEach(card => {
        const jobId = parseInt(card.dataset.id);
        const icon = card.querySelector(".bookmark-icon");

        if (SAVED_JOBS.includes(jobId)) {
            icon.classList.remove("fa-regular");
            icon.classList.add("fa-solid");
            icon.style.color = "#0d6efd";
        } else {
            icon.classList.remove("fa-solid");
            icon.classList.add("fa-regular");
            icon.style.color = "#444";
        }
    });

    // Load FIRST job by default
    if (jobCards.length > 0) {
        jobCards[0].classList.add("active");
        updateDetails(jobCards[0]);
    }

    // Handle clicking job cards
    jobCards.forEach(card => {
        card.addEventListener("click", () => {

            // Remove active from all
            jobCards.forEach(c => c.classList.remove("active"));

            // Add active to clicked one
            card.classList.add("active");

            // Update right-side details
            updateDetails(card);

            // MOBILE — show details only
            if (window.innerWidth < 992) {
                document.querySelector(".job-list-panel").style.display = "none";
                document.querySelector(".job-details-panel").style.display = "block";
            }

            // if (window.innerWidth < 768) {
            //     document.querySelector(".search-panels .col-5").classList.add("hide-list");
            //     document.querySelector(".details-card").classList.add("mobile-active");
            // }

        });
    });

});

// Update right details
function updateDetails(card) {

    const titleEl = document.getElementById("detail-title");
    const companyEl = document.getElementById("detail-company");
    const locationEl = document.getElementById("detail-location");
    const salaryEl = document.getElementById("detail-salary");
    const typeEl = document.getElementById("detail-type");
    const descEl = document.getElementById("detail-description");
    const headerLocation = document.getElementById("detail-header-location");
    const saveBtn = document.getElementById("detail-save-btn");
    const icon = saveBtn.querySelector("i");
    const jobId = card.dataset.id;

    if (SAVED_JOBS.includes(parseInt(jobId))) {
        icon.classList.remove("fa-regular");
        icon.classList.add("fa-solid");
        icon.style.color = "#0d6efd";
    } else {
        icon.classList.remove("fa-solid");
        icon.classList.add("fa-regular");
        icon.style.color = "#444";
    }

    saveBtn.setAttribute("data-job-id", jobId);
    titleEl.textContent = card.dataset.title;
    companyEl.textContent = card.dataset.company;
    locationEl.textContent = card.dataset.location;
    headerLocation.textContent = card.dataset.location;

    salaryEl.textContent = card.dataset.salary || "";
    typeEl.textContent = card.dataset.type || "";

    descEl.textContent = card.dataset.description;

    document.querySelector(".details-body").scrollTop = 0;
    saveBtn.setAttribute("data-job-id", card.dataset.id);
    document.getElementById("detail-apply-btn").href = `/applications/apply/${jobId}/`;
}


function toggleBookmarkButton(btn) {
    btn.classList.toggle("saved");
}

function clearSearch() {
    document.querySelector("input[name='q']").value = "";
    document.querySelector("input[name='loc']").value = "";

    const selects = document.querySelectorAll(".filter-select");
    selects.forEach(select => select.value = "");

    window.location.href = "/jobs/search";
}

// function saveJob(jobId, iconElement) {
//     fetch(`/seeker/save/${jobId}/`)
//         .then(response => response.json())
//         .then(data => {
//             if (data.status === "saved") {
//                 iconElement.classList.remove("fa-regular");
//                 iconElement.classList.add("fa-solid");
//                 iconElement.style.color = "#0d6efd";
//             } 
//             else if (data.status === "removed") {
//                 iconElement.classList.remove("fa-solid");
//                 iconElement.classList.add("fa-regular");
//                 iconElement.style.color = "#444";
//             }
//         })
//         .catch(error => console.error("Error:", error));
// }
function saveJob(event, jobId, icon) {
    event.stopPropagation();

    fetch(`/seeker/save/${jobId}/`)
        .then(response => response.json())
        .then(data => {

            const numericId = parseInt(jobId);

            if (data.status === "saved") {
                icon.classList.remove("fa-regular");
                icon.classList.add("fa-solid");
                icon.style.color = "#0d6efd";

                if (!SAVED_JOBS.includes(numericId)) {
                    SAVED_JOBS.push(numericId);
                }
            } 
            else if (data.status === "removed") {
                icon.classList.remove("fa-solid");
                icon.classList.add("fa-regular");
                icon.style.color = "#444";

                const index = SAVED_JOBS.indexOf(numericId);
                if (index !== -1) {
                    SAVED_JOBS.splice(index, 1);
                }

            }

            const rightBtn = document.getElementById("detail-save-btn");
            if (rightBtn && rightBtn.getAttribute("data-job-id") == jobId) {
                const rightIcon = rightBtn.querySelector("i");

                if (data.status === "saved") {
                    rightIcon.classList.remove("fa-regular");
                    rightIcon.classList.add("fa-solid");
                    rightIcon.style.color = "#0d6efd";
                } else {
                    rightIcon.classList.remove("fa-solid");
                    rightIcon.classList.add("fa-regular");
                    rightIcon.style.color = "#444";
                }
            }
        });
}


function saveJobFromDetails(event, btn) {
    event.stopPropagation();

    const jobId = btn.getAttribute("data-job-id");
    const icon = btn.querySelector("i");
    const numericId = parseInt(jobId);

    fetch(`/seeker/save/${jobId}/`)
        .then(res => res.json())
        .then(data => {

            if (data.status === "saved") {
                icon.classList.remove("fa-regular");
                icon.classList.add("fa-solid");
                icon.style.color = "#0d6efd";

                if (!SAVED_JOBS.includes(numericId)) {
                    SAVED_JOBS.push(numericId);
                }
            } 
            else if (data.status === "removed") {
                icon.classList.remove("fa-solid");
                icon.classList.add("fa-regular");
                icon.style.color = "#444";

                const index = SAVED_JOBS.indexOf(numericId);
                if (index !== -1) {
                    SAVED_JOBS.splice(index, 1);
                }

            }

            const leftIcon = document.querySelector(
                `.job-card[data-id="${jobId}"] .bookmark-icon`
            );

            if (leftIcon) {
                if (data.status === "saved") {
                    leftIcon.classList.remove("fa-regular");
                    leftIcon.classList.add("fa-solid");
                    leftIcon.style.color = "#0d6efd";
                } else {
                    leftIcon.classList.remove("fa-solid");
                    leftIcon.classList.add("fa-regular");
                    leftIcon.style.color = "#444";
                }
            }
        });
}


function showList() {
    document.querySelector(".job-list-panel").style.display = "block";
    document.querySelector(".job-details-panel").style.display = "none";
}
