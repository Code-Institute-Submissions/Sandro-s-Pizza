// Carousel on index page on (refreshes every 5 sec)
// CODE CREDIT: https://github.com/karlhadwen/carousel/blob/master/app.js
let carousel = document.getElementsByClassName("pizza-carousel__item")
let carouselPosition = 0
let carouselLength = carousel.length

if (carousel.length > 0) {
    setInterval(moveToNextSlide, 5000);
}

function updateCarouselPosition() {
    for (let item of carousel) {
        item.classList.remove('pizza-carousel__item--active');
    }
    carousel[carouselPosition].classList.add('pizza-carousel__item--active');
}

function moveToNextSlide() {
    if (carouselPosition === carouselLength - 1) {
        carouselPosition = 0;
    } else {
        carouselPosition++;
    }
    updateCarouselPosition();
}

// Adds active class to first item in carousel image on load
$(".pizza-carousel__item")[0].classList.add('pizza-carousel__item--active');