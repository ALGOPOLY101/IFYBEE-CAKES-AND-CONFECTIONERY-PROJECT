

document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".slide");
    const slideButtons = document.querySelectorAll(".slide-line");

    if (!slides.length) return;

    let currentSlide = 0;
    let slideTimer = null;

    // Function to activate a specific slide background by index
    function showSlide(index) {
        if (index >= slides.length) index = 0;
        if (index < 0) index = slides.length - 1;

        // Deactivate all slides and indicator lines
        for (let i = 0; i < slides.length; i++) {
            slides[i].classList.remove("active");
        }
        for (let i = 0; i < slideButtons.length; i++) {
            slideButtons[i].classList.remove("active");
        }

        // Activate the target slide and corresponding indicator line
        slides[index].classList.add("active");
        if (slideButtons[index]) {
            slideButtons[index].classList.add("active");
        }

        currentSlide = index;
    }

    // Function to advance automatically to the next slide
    function nextSlide() {
        showSlide(currentSlide + 1);
    }

    // Start auto-advancing slideshow every 5 seconds (smooth continuous fade)
    function startSlideTimer() {
        if (slideTimer) clearInterval(slideTimer);
        if (slides.length > 1) {
            slideTimer = setInterval(nextSlide, 5000);
        }
    }

    // Allow clicking indicators to jump to a specific background slide
    slideButtons.forEach(function (button, index) {
        button.addEventListener("click", function () {
            showSlide(index);
            startSlideTimer(); // Reset timer upon manual interaction
        });
    });

    // Start slideshow
    startSlideTimer();
});
