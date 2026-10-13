// Main navigation for all webpages
const menuBtn = document.querySelector("#menuBtn");
const menuCloseBtn = document.querySelector("#menuCloseBtn");
const menuOverlay = document.querySelector("#menuOverlay");
const mobileLinks = document.querySelectorAll(".mobile-nav a");

//SIDEBAR MENU INTERACTIVENESS FOR IFYBEES
function openMobileMenu() {
    document.body.classList.add("menu-open");
}
function closeMobileMenu() {
    document.body.classList.remove("menu-open");
}
if (menuBtn) {
    menuBtn.addEventListener("click", openMobileMenu);
}
if (menuCloseBtn) {
    menuCloseBtn.addEventListener("click", closeMobileMenu);
}
if (menuOverlay) {
    menuOverlay.addEventListener("click", closeMobileMenu);
}
mobileLinks.forEach(function (link) {
    link.addEventListener("click", closeMobileMenu);
});

// Close menu when Escape key is pressed
document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && document.body.classList.contains("menu-open")) {
        closeMobileMenu();
    }
});

// NAVBAR SCROLL EFFECT 
const header = document.querySelector(".header");
if (header) {
    window.addEventListener("scroll", function () {
        if (window.scrollY > 60) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    });
}
