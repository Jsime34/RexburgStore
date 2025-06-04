// javascript for sweetalert2. https://sweetalert2.github.io/ 

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
});

// javascript for sweetalert2. https://sweetalert2.github.io/ 
