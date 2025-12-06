// function removeSavedJob(button) {
//     const jobId = button.getAttribute("data-job-id");

//     fetch(`/seeker/save/${jobId}/`)
//         .then(res => res.json())
//         .then(data => {
//             if (data.status === "removed") {
//                 button.closest(".saved-card").remove();
//             }
//         });
// }
