// Main navigation and global scripts

// SELECT ELEMENTS FOR MOBILE MENU
const menuBtn = document.querySelector("#menuBtn");
const menuCloseBtn = document.querySelector("#menuCloseBtn");
const menuOverlay = document.querySelector("#menuOverlay");
const mobileLinks = document.querySelectorAll(".mobile-nav a");

// Function to open the mobile menu
function openMobileMenu() {
    document.body.classList.add("menu-open");
}

// Function to close the mobile menu
function closeMobileMenu() {
    document.body.classList.remove("menu-open");
}

// EVENT LISTENERS FOR MOBILE MENU
if (menuBtn) {
    menuBtn.addEventListener("click", openMobileMenu);
}

if (menuCloseBtn) {
    menuCloseBtn.addEventListener("click", closeMobileMenu);
}

if (menuOverlay) {
    menuOverlay.addEventListener("click", closeMobileMenu);
}

// Close menu when any navigation link is clicked
mobileLinks.forEach(function (link) {
    link.addEventListener("click", closeMobileMenu);
});

// Close menu when Escape key is pressed
document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && document.body.classList.contains("menu-open")) {
        closeMobileMenu();
    }
});

// NAVBAR SCROLL EFFECT (transparent at top → solid when scrolled)
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

// SET CURRENT YEAR IN FOOTER
const yearElement = document.querySelector("#currentYear");
if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
}
