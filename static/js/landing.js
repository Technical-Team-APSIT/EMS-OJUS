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

document.addEventListener("DOMContentLoaded", function () {
  setTimeout(function () {
      document.querySelector('.preloader').style.display = 'none';
      document.querySelector('#home-section').style.display = 'block';
  }, 4000);
});