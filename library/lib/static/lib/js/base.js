$(document).ready(function () {

    $('.txt-p1').click(function (event) {
        $('.txt1, .txt-p1').toggleClass('active')
    })
    $('.txt-p2').click(function (event) {
        $('.txt2, .txt-p2').toggleClass('active')
    })
    $('.txt-p3').click(function (event) {
        $('.txt3, .txt-p3').toggleClass('active')
    })
    $('.txt-p4').click(function (event) {
        $('.txt4, .txt-p4').toggleClass('active')
    })
    $('.txt-p5').click(function (event) {
        $('.txt5, .txt-p5').toggleClass('active')
    })

    $('.buy, .buuy').click(function (event) {
        $('.zam').toggleClass('active')
        $('body').toggleClass('lock')
    })
    $('.add-c-bu, .send-btn').click(function (event) {
        $('.zam').removeClass('active')
        $('body').removeClass('lock')
    })
        $('.ma-li').click(function (event) {
        $('.za').toggleClass('active')
        $('body').toggleClass('lock')
    })
    $('.add-z-bu').click(function (event) {
        $('.za').removeClass('active')
        $('body').removeClass('lock')
    })
    $('#id_name').attr('placeholder', "Ім'я")
    $('#id_phone').attr('placeholder', 'Номер телефону')


    var form = $('#form_product');
    $('.kls, #inp-nam').on('input', function () {
            var quantity = $('.kls').val();
            var price = parseFloat($('#pri').data('price'));
            var totalPrice = quantity * price;
            $('#total_price').text(totalPrice + ' грн');
    form.on('submit', function (e) {
        e.preventDefault();
        var submit_btn = $('#buuy');
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        var data = {};
        data.product_name = product_name;
        data.product_price = product_price;
        data.quantity = quantity;
        data.client_name = $('#in').val();
        data.client_phone = $('#it').val();
        data.all = totalPrice;
         var csrf_token = $('#form_product [name="csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        console.log(data);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
        })

    });
    });
})