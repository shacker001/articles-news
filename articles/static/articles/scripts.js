document.addEventListener("DOMContentLoaded", function () {
    // Set timeout to fade out alert after 7 seconds
    setTimeout(function () {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            alert.classList.add('fade-out');
        });
    }, 7000); // 7 seconds before fade out

    // Hamburger menu toggle functionality
    document.getElementById("hamburger").addEventListener("click", function () {
        console.log("Hamburger clicked!"); // Debugging log
        document.getElementById("navbar").classList.toggle("active");
        this.classList.toggle("active"); // Toggles the hamburger icon animation if you have it styled
    });
});
