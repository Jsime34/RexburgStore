// scripts.js
document.addEventListener("DOMContentLoaded", function () {
    // Handle form errors
    const errorDataElement = document.getElementById("form-errors-data");

    if (errorDataElement) {
        const errors = JSON.parse(errorDataElement.textContent);

        let message = "";
        for (const [field, fieldErrors] of Object.entries(errors)) {
            fieldErrors.forEach((error) => {
                message += `${field}: ${error}\n`;
            });
        }

        Swal.fire({
            icon: "error",
            title: "Form Error",
            text: message,
            confirmButtonColor: "#003366",
        });
    }

    // Handle success messages
    if (window.listingSuccessMessages && window.listingSuccessMessages.length > 0) {
        Swal.fire({
            icon: "success",
            title: "Success!",
            text: window.listingSuccessMessages.join("\n"),
            confirmButtonColor: "#003366",
        });
    }

    // Show login required popup if redirected with ?next=
    if (window.loginRequired) {
        Swal.fire({
            icon: "warning",
            title: "Login Required",
            text: "Please log in to continue.",
            confirmButtonColor: "#003366",
        });
    }
});
