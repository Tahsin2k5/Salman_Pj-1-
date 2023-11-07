



$(document).ready(function () {
    title_local = localStorage.getItem('title')
    console.log(title_local)
    title_a = JSON.parse(title_local)
    $('.cart-product-description').text(localStorage.getItem('title'))
    $('.quant').val(localStorage.getItem('value_quant'))
    $('.cart-sub-total-price').text(localStorage.getItem('price'))
});