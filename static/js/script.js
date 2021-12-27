// Adds event listener to nav toggle button on mobile
$(".navbar__button").click(function () {
    $(".navbar__menu").toggle("slide");
})

// Updates item quantity form field on item page
$('.item__plus').click(function(){
    value = Number($('#item-quantity').val())
    value++
    $('#item-quantity').val(value)
})
$('.item__minus').click(function(){
    value = Number($('#item-quantity').val())
    if (value === 1) {
        $('#item-quantity').val(1)
    } else {
        value--
        $('#item-quantity').val(value)
    }

})

// Carousel on index page on (refreshes every 5 sec)
// CODE CREDIT: https://github.com/karlhadwen/carousel/blob/master/app.js
let carousel = document.getElementsByClassName("pizza-carousel__item")
let carouselPosition = 0
let carouselLength = carousel.length

setInterval(moveToNextSlide, 5000);

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

function moveToPrevSlide() {
    if (carouselPosition === 0) {
        carouselPosition = carouselLength - 1;
    } else {
        carouselPosition--;
    }
    updateCarouselPosition();
}