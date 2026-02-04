const messages = document.querySelectorAll(".message");

if (messages.length) {
    setTimeout(() => {
        messages.forEach((message) => {
            message.style.opacity = "0";
        });
    }, 3500);
}