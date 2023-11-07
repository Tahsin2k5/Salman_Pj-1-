



$(document).ready(function () {
    value_quant = 0
    price = parseFloat($('.price').text())
    main_price = parseFloat($('.price-strike').text())
    $('.count').text($('.quant-input input').val())
    $('.total-price .value').text(price)

    // alert(price)
    $('.plus').click(function () {
        value_quant = $('.quant-input input').val()
        console.log(value_quant)
        value_quant = parseInt(value_quant) + 1
        if (value_quant > 5) {
            value_quant = 5
            $('.quant-input input').val(5)
            // $('.count').text(5)
        }
        else {
            $('.quant-input input').val(value_quant)
            // $('.count').text(value_quant)
        }
        // price1 = price * value_quant
        // price2 = main_price * value_quant
        // // // alert(price1)
        // $('.total-price .value').text(price1)
        // $('.price-strike').text(price2)


    });

    $('.minus').click(function () {

        value_quant = $('.quant-input input').val()
        value_quant = parseInt(value_quant) - 1
        if (value_quant < 1) {
            value_quant = 1
            $('.quant-input input').val(1)
            // $('.count').text(1)
        }
        else {
            $('.quant-input input').val(value_quant)
            // $('.count').text(value_quant)
        }
        // price1 = price * value_quant
        // price2 = main_price * value_quant
        // // // alert(price1)
        // $('.total-price .value').text(price1)
        // $('.price-strike').text(price2)

    });



    title_local = localStorage.getItem('title')
    if (title_local !== null) {
        title_a = JSON.parse(title_local)
        console.log(title_a)
    }
    else {
        title_a = []
        price_a = []
        quant_a = []
    }


    $('body').on('click', '.add_to_cart', function () {
        console.log("yes")
        value_quant = $('.quant-input input').val()
        $('.count').text(value_quant)
        price1 = price * value_quant
        price2 = main_price * value_quant
        // // alert(price1)
        $('.total-price .value').text(price1)
        title = $('.course_title').text()
        price = $('.price').text()

        if (title_local !== null) {
            title_a.push(title)
            // price_a.push(price)
            // quant_a.push(value_quant)
        }

        // title_a.push(title)
        // price_a.push(price)
        // quant_a.push(value_quant)
        console.log(title_a)

        localStorage.setItem('title', JSON.stringify(title_a))
        // localStorage.setItem('price', JSON.stringify(price_a))
        // localStorage.setItem('value_quant', JSON.stringify(quant_a))

        console.log(localStorage.getItem('title'))

        // $('.price-strike').text(price2)


    });
});