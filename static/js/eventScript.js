const paintBall = document.querySelector('.paintBall');
let lastScrollY = window.scrollY || window.pageYOffset;
window.addEventListener('scroll', function() {
    const scrollY = window.scrollY || window.pageYOffset;
    const deltaY = scrollY - lastScrollY;
    const movementAmount = deltaY / 4;
    const boundingBox = paintBall.getBoundingClientRect();
    const threshold = window.innerHeight + 100;
    if (boundingBox.bottom < -threshold || boundingBox.top > threshold) {
        paintBall.style.top = '0px';
    } else {
        paintBall.style.top = `${parseInt(paintBall.style.top || 0) - movementAmount}px`;
    }
    
    lastScrollY = scrollY;
});





document.addEventListener('DOMContentLoaded', function() {
    const heroContent = document.querySelector('.hero-content');
    heroContent.classList.remove('animate-from-below');
    setTimeout(() => {
        heroContent.classList.add('animate-from-below');
    }, 0);
});
