document.addEventListener("DOMContentLoaded", function () {
    // Set timeout to fade out alert after 7 seconds
    setTimeout(function () {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            alert.classList.add('fade-out');
        });
    }, 7000); // 7 seconds before fade out

    // Hamburger menu toggle
    window.toggleMenu = function () {
        const navbar = document.getElementById('navbar');
        navbar.classList.toggle('show');
    };
});
