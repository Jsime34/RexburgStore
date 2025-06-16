document.addEventListener("DOMContentLoaded", function () {
    // ✅ SweetAlert listing success
    const swalData = document.getElementById("swal-data");
    if (swalData) {
        const type = swalData.getAttribute("data-type");
        const message = swalData.getAttribute("data-message");

        Swal.fire({
            icon: type,
            title: type === "success" ? "Success" : "Info",
            text: message,
            confirmButtonColor: "#003366"
        });
    }

    // ✅ SweetAlert form errors
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

    // ✅ Menu toggle
    const toggleButton = document.getElementById("menu-toggle");
    const menuContent = document.getElementById("menu-content");

    if (toggleButton && menuContent) {
        toggleButton.addEventListener("click", function (e) {
            e.preventDefault();
            if (menuContent.style.display === "none" || menuContent.style.display === "") {
                menuContent.style.display = "block";
            } else {
                menuContent.style.display = "none";
            }
        });
    }
});
