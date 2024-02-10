document.addEventListener("DOMContentLoaded", function() {
    const menuBtn = document.getElementById("menuBtn");
    const navLinks = document.getElementById("navLinks");

    menuBtn.addEventListener("click", function() {
        this.classList.toggle("active");
        navLinks.style.display = this.classList.contains("active") ? "flex" : "none";
    });
});
function toggleMenu() {
    const menu = document.querySelector('nav ul');
    const menuIcon = document.querySelector('.menu');
    
    menu.classList.toggle('show');
    menuIcon.classList.toggle('open');

    window.onscroll = () =>
    {
        menu.classList.remove('show');
        menuIcon.classList.remove('open');
}
}



let hamburger = document.querySelector('.hamburger');
let times = document.querySelector('.times');
let mobileNav = document.querySelector('.mobile-nav');

hamburger.addEventListener('click', function(){
    mobileNav.classList.add('open');
});
times.addEventListener('click', function(){
    mobileNav.classList.remove('open');    
});


function toggleMenu() {
    var menu = document.querySelector('.mobile-nav');
    menu.classList.toggle('open');
}

document.addEventListener("DOMContentLoaded", function () {
    // Add a delay of 2000 milliseconds (2 seconds)
    setTimeout(function () {
        // Hide the preloader
        document.querySelector('.preloader').style.display = 'none';

        // Display the main content
        document.querySelector('.mainSection').style.display = 'flex';
    }, 2300);
});


var countDownDate = new Date("Feb 26, 2024 00:00:00").getTime();
var x = setInterval(function() {
    var now = new Date().getTime();
    var distance = countDownDate - now;

    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("days").innerHTML = days;
    document.getElementById("hours").innerHTML = hours;
    document.getElementById("minutes").innerHTML = minutes;
    document.getElementById("seconds").innerHTML = seconds;
}, 1000);
    const observerOptions = {
    threshold: 0.5, 
  };
  const handleIntersection = (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        document.querySelector('.left-to-right .ball').style.animationPlayState = 'running';
        document.querySelector('.right-to-left .ball').style.animationPlayState = 'running';
      } else {
        document.querySelector('.left-to-right .ball').style.animationPlayState = 'paused';
        document.querySelector('.right-to-left .ball').style.animationPlayState = 'paused';
      }
    });
  };

  const observer = new IntersectionObserver(handleIntersection, observerOptions);

  const targetElement = document.querySelector('.preGallerySection');

  observer.observe(targetElement);