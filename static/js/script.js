

// Updates item quantity form field on item page
$('.item__plus').click(function(){
    value = Number($('#item-quantity').val())
    value++
    $('#item-quantity').val(value)
    // Manually trigger change event
    let event = new Event('change');
    $('#item-quantity')[0].dispatchEvent(event);
})
$('.item__minus').click(function(){
    value = Number($('#item-quantity').val())
    if (value === 1) {
        $('#item-quantity').val(1)
    } else {
        value--
        $('#item-quantity').val(value)
    }
    // Manually trigger change event
    let event = new Event('change');
    $('#item-quantity')[0].dispatchEvent(event);
})

// Toggles textarea on item page
$('.comment__add').click(function(){
    $('.comment__new').toggle()
})

// Back button
$(".js-back").click(function () {
    window.location.href = document.referrer;
});



// Calculates total price on item page
let defaultItemPrice = Number($("#item-price").text());
let itemPrice;

$("#item-size").change(calculateTotalItem)
$("#item-quantity").change(calculateTotalItem)

function calculateTotalItem(){
    itemSize = $("#item-size").val();
    itemQuantity = Number($("#item-quantity").val());
    itemPrice = defaultItemPrice
    if(itemSize === "small"){
        itemPrice = (itemPrice - 2) * itemQuantity
    } else if(itemSize === "large") {
        itemPrice = (itemPrice + 2) * itemQuantity
    } else {
        itemPrice = itemPrice * itemQuantity
    }
    $("#item-price").text(`${itemPrice.toFixed(2)}`)
}

// Hides checkout popup
$(".checkout-popup__close").click(function(){
    $(".checkout-popup").hide()
})

// Hides flash message
$(".flash__close").click(function(){
    $(".flash").hide();
})

// Adds event listener to nav toggle button on mobile
$(".navbar__button").click(function () {
    $(".navbar__mobile-menu").toggle("slide");
})