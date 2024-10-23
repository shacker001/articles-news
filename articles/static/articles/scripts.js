function toggleMenu() {
    // console.log("Hamburger clicked!");
    var navLinks = document.getElementById("navLinks");
    navLinks.classList.toggle("show");
}


document.addEventListener("DOMContentLoaded", function () {
    // Set timeout to fade out alert after 5 seconds
    setTimeout(function () {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            alert.classList.add('fade-out');
        });
    }, 7000); // 10 seconds before fade out
});
