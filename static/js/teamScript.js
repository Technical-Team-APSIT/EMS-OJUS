document.addEventListener('DOMContentLoaded', function() {
    const boxes = document.querySelectorAll('.box');
    const meetJamsutkars = document.querySelectorAll('.MeetJamsutkar');
    const defaultElement = document.querySelector('.default');

    boxes.forEach((box, index) => {
        box.addEventListener('mouseover', () => {
            setTimeout(() => {
                meetJamsutkars.forEach(meetJamsutkar => {
                    meetJamsutkar.style.display = 'none';
                });
                meetJamsutkars[index].style.display = 'block';
                defaultElement.style.display = 'none';
            }, 500);
        });
    });

    const container = document.querySelector('.container');

    container.addEventListener('mouseleave', () => {
        meetJamsutkars.forEach(meetJamsutkar => {
            meetJamsutkar.style.display = 'none';
        });
        defaultElement.style.display = 'block';
    });
});



document.addEventListener("DOMContentLoaded", function () {
    // Add a delay of 2000 milliseconds (2 seconds)
    setTimeout(function () {
        // Hide the preloader
        document.querySelector('.preloader').style.display = 'none';

        // Display the main content
        document.querySelector('.mainSection').style.display = 'flex';
    }, 1200);
});