// Gallery category filtering and lightbox preview

// CATEGORY FILTERING LOGIC
const filterButtons = document.querySelectorAll(".filter-button");
const galleryCards = document.querySelectorAll(".gallery-card");
const emptyNotice = document.querySelector("#galleryEmpty");

filterButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        // Remove active class from all buttons and add to the clicked button
        filterButtons.forEach(function (btn) {
            btn.classList.remove("active");
        });
        button.classList.add("active");

        const selectedCategory = button.getAttribute("data-filter");
        let matchesFound = 0;

        // Show or hide each gallery card based on the category
        galleryCards.forEach(function (card) {
            const cardCategory = card.getAttribute("data-category");

            if (selectedCategory === "all" || cardCategory === selectedCategory) {
                card.style.display = "flex";
                matchesFound++;
            } else {
                card.style.display = "none";
            }
        });

        // Show empty message if no cards match
        if (emptyNotice) {
            if (matchesFound === 0) {
                emptyNotice.style.display = "block";
            } else {
                emptyNotice.style.display = "none";
            }
        }
    });
});

// SIMPLE LIGHTBOX IMAGE PREVIEW
const lightboxModal = document.querySelector("#lightboxModal");
const lightboxImg = document.querySelector("#lightboxImg");
const lightboxTitle = document.querySelector("#lightboxTitle");
const lightboxCategory = document.querySelector("#lightboxCategory");
const lightboxDownload = document.querySelector("#lightboxDownload");
const lightboxClose = document.querySelector("#lightboxClose");

function openLightbox(imageSrc, titleText, categoryText, downloadHref) {
    if (lightboxModal) {
        lightboxImg.src = imageSrc;
        lightboxImg.alt = titleText;
        lightboxTitle.textContent = titleText;
        lightboxCategory.textContent = categoryText;
        lightboxDownload.href = downloadHref;

        lightboxModal.classList.add("active");
        document.body.style.overflow = "hidden"; // Prevent background scroll
    }
}

function closeLightbox() {
    if (lightboxModal) {
        lightboxModal.classList.remove("active");
        document.body.style.overflow = ""; // Restore background scroll
        lightboxImg.src = "";
    }
}

// Attach click listeners to all gallery card preview triggers
galleryCards.forEach(function (card) {
    const imageBox = card.querySelector(".gallery-image-box");
    const previewBtn = card.querySelector(".preview-button");
    const cardImg = card.querySelector("img");
    const cardTitle = card.querySelector(".gallery-card h3");
    const cardCategory = card.querySelector(".gallery-category");
    const downloadBtn = card.querySelector(".download-button");

    function handleCardClick() {
        const src = cardImg ? cardImg.getAttribute("src") : "";
        const title = cardTitle ? cardTitle.textContent : "Gallery Item";
        const category = cardCategory ? cardCategory.textContent : "Confectionery";
        const downloadUrl = downloadBtn ? downloadBtn.getAttribute("href") : src;

        openLightbox(src, title, category, downloadUrl);
    }

    if (imageBox) {
        imageBox.addEventListener("click", handleCardClick);
    }

    if (previewBtn) {
        previewBtn.addEventListener("click", function (event) {
            event.stopPropagation();
            handleCardClick();
        });
    }
});

// Close button click listener
if (lightboxClose) {
    lightboxClose.addEventListener("click", closeLightbox);
}

// Close when clicking directly on the dark overlay background
if (lightboxModal) {
    lightboxModal.addEventListener("click", function (event) {
        if (event.target === lightboxModal) {
            closeLightbox();
        }
    });
}

// Close when pressing Escape key
document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && lightboxModal && lightboxModal.classList.contains("active")) {
        closeLightbox();
    }
});
