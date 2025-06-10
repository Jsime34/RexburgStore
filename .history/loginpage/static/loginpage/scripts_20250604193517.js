// scripts.js

document.addEventListener("DOMContentLoaded", function () {
    // SweetAlert2 for form errors
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

    // SweetAlert2 for listing success
    if (window.listingSuccessMessages && window.listingSuccessMessages.length > 0) {
        Swal.fire({
            icon: "success",
            title: "Success!",
            text: window.listingSuccessMessages.join("\n"),
            confirmButtonColor: "#003366",
        });
    }

    // ----------------------
    // Ably Chat Integration
    // ----------------------

    // Only run if chat container exists
    if (document.getElementById("chat-log")) {
        const ably = new Ably.Realtime("YOUR_ABLY_API_KEY"); // replace with real key
        const channel = ably.channels.get("rexburg-store-chat");

        // Send a chat message
        window.sendMessage = function () {
            const input = document.getElementById("chat-message");
            const message = input.value.trim();
            if (message) {
                channel.publish("message", message);
                input.value = "";
            }
        };

        // Listen for incoming messages
        channel.subscribe("message", function (msg) {
            const log = document.getElementById("chat-log");
            const line = document.createElement("div");
            line.textContent = msg.data;
            log.appendChild(line);
            log.scrollTop = log.scrollHeight;
        });
    }
});
