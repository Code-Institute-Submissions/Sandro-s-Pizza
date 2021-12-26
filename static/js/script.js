// Adds event listener to nav toggle button on mobile
$(".navbar__button").click(function(){
    $(".navbar__menu").toggle( "slide" );
})

// Adds swipe event to pizza image on index page on mobile phones
// CODE CREDIT: https://stackoverflow.com/a/56663695
let touchstartX = 0
let touchendX = 0
const slider = $(".pizza-carousel__item")[0]
function handleGesture() {
  if (touchendX < touchstartX) alert('swiped left!')
  if (touchendX > touchstartX) alert('swiped right!')
}
slider.addEventListener('touchstart', e => {
  touchstartX = e.changedTouches[0].screenX
})
slider.addEventListener('touchend', e => {
  touchendX = e.changedTouches[0].screenX
  handleGesture()
})