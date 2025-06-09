// JavaScript for SweetAlert2 form error popup
document.addEventListener("DOMContentLoaded", function () {
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

    // ✅ Success message popup after listing creation
    if (window.listingSuccessMessages && window.listingSuccessMessages.length > 0) {
        window.listingSuccessMessages.forEach((msg) => {
            Swal.fire({
                icon: 'success',
                title: msg,
                showConfirmButton: false,
                timer: 2000
            });
        });
    }
});
