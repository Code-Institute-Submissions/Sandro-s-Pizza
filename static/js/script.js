$(".navbar__button").click(function(){
    $(".navbar__menu").toggle( "slide" );
})


function swipeleftHandler() {
    alert("swiped")
}
$(".pizza-carousel__item").on( "click", swipeleftHandler );