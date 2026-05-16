function toggleMenu() {
    document.getElementById("navLinks").classList.toggle("show");
}

function filterServices(category) {
    const items = document.querySelectorAll(".service-item, .gallery-card");
    const buttons = document.querySelectorAll(".filter-btn");

    buttons.forEach(button => button.classList.remove("active"));
    const clicked = document.querySelector(`[data-filter="${category}"]`);
    if (clicked) clicked.classList.add("active");

    items.forEach(item => {
        const itemCategory = item.getAttribute("data-category");
        if (category === "all" || itemCategory === category) {
            item.style.display = "grid";
        } else {
            item.style.display = "none";
        }
    });
}

function openImageModal(src, title) {
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("modalImage");
    const modalTitle = document.getElementById("modalTitle");

    if (!modal || !modalImg || !modalTitle) return;

    modalImg.src = src;
    modalTitle.textContent = title;
    modal.classList.add("show");
}

function closeImageModal() {
    const modal = document.getElementById("imageModal");
    if (modal) modal.classList.remove("show");
}

document.addEventListener("click", function(event) {
    if (event.target.classList.contains("modal")) {
        closeImageModal();
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {
        const target = Number(counter.getAttribute("data-target"));
        let current = 0;
        const step = Math.max(1, Math.floor(target / 60));

        const update = () => {
            current += step;
            if (current >= target) {
                counter.textContent = target + "+";
            } else {
                counter.textContent = current + "+";
                requestAnimationFrame(update);
            }
        };

        update();
    });
});
