// javascript for sweetalert2. https://sweetalert2.github.io/ 

document.addEventListener("DOMContentLoaded", function () {
    // 🔴 Display form validation errors
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

    // ✅ Show listing success message
    const successData = document.getElementById("listingSuccessMessages");
    if (successData) {
        const messages = JSON.parse(successData.textContent);
        if (messages.length > 0) {
            Swal.fire({
                icon: "success",
                title: "Success!",
                text: messages[0], // Display first message
                confirmButtonColor: "#003366",
            });
        }
    }
});
