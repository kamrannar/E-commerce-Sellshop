(function ($) {
    "use strict";
    // jQuery MeanMenu
    jQuery('nav#dropdown').meanmenu();
    //menu a active jquery
    var pgurl = window.location.href.substr(window.location.href
        .lastIndexOf("/") + 1);
    $("ul li a").each(function () {
        if ($(this).attr("href") == pgurl || $(this).attr("href") == '')
            $(this).addClass("active");
        $('header ul li ul li a.active').parent('li').addClass('parent-li');
        $('header ul li ul li.parent-li').parent('ul').addClass('parent-ul');
        $('header ul li ul.parent-ul').parent('li').addClass('parent-active');
    })
    //search bar exprnd
    $('.header-top-two .right button').on('click', function () {
        $('.header-top-two .right').toggleClass('widthfull');
    });
    //search bar border color
    $('.middel-top .center').on('click', function () {
        $('.middel-top .center').toggleClass('bordercolor');
    });
    //color select jquery
    $('.color-select > span').on('click', function () {
        $('.color-select > span').toggleClass('outline');
        $(this).addClass("outline").siblings().removeClass("outline");
    });
    /*----------------------------
     nivoSlider active
    ------------------------------ */
    $('#mainSlider').nivoSlider({
        directionNav: true,
        animSpeed: 500,
        effect: 'random',
        slices: 18,
        pauseTime: 10000,
        pauseOnHover: false,
        controlNav: true,
        prevText: '<i class="mdi mdi-chevron-left"></i>',
        nextText: '<i class="mdi mdi-chevron-right"></i>'
    });
    /*----------------------------
     plus-minus-button
    ------------------------------ */
    $(".qtybutton").on("click", function () {
        var $button = $(this);
        var oldValue = $button.parent().find("input").val();
        if ($button.text() == "+") {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        $button.parent().find("input").val(newVal);
    });
    /*----------------------------
     price-slider active
    ------------------------------ */
    $("#slider-range").slider({
        range: true,
        min: 40,
        max: 600,
        values: [150, 399],
        slide: function (event, ui) {
            $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        }
    });
    $("#amount").val("$" + $("#slider-range").slider("values", 0) +
        " - $" + $("#slider-range").slider("values", 1));
    /*--------------------------
     scrollUp
    ---------------------------- */
    $.scrollUp({
        scrollText: '<i class="mdi mdi-chevron-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
    /*--------------------------
     // simpleLens
     ---------------------------- */
    $('.simpleLens-image').simpleLens({

    });

})(jQuery);

let updateBtns = $('.update-cart')
var sum_and_item = document.getElementById('sum and item')
var wishlist = $('.wishlist')
let cartMenu = document.getElementById('cartdrop')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
access = window.localStorage.getItem('access')
async function postData() {
    await fetch('http://127.0.0.1:8000/api/cart_items/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            // 'X-CSRFToken': csrftoken,
            // 'Authorization': `Bearer ${access}`
        },
    })
        .then((response) => response.json())
        .then((data) => {
            let sum = 0
            let priceSum = 0
            cartMenu.innerHTML = ``
            data.forEach((element) => {
                if (element.cart_id.user_id.id == cart_idd) {
                    if (document.getElementById(element.product_version_id.name)) {
                        document.getElementById(element.product_version_id.name).remove()
                        cartMenu.innerHTML += `
            <div  id='${element.product_version_id.name}' class=" sin-itme clearfix ">
            <a data-cart_item="${element.id}"  class="remove-cart"><i  class="mdi  mdi-close "></i></a>

            <a class="cart-img" href="/${element.product_version_id.slug}/"><img
                    src="${element.product_version_id.cover_image_version}" alt="" />
            
            </a>
            <div class="menu-cart-text">
                <a href="/${element.product_version_id.slug}/">
                    <h5>${element.product_version_id.name}</h5>
                </a>
                <span>Color : ${element.product_version_id.color_id.colors}</span>
                <span>Size : ${element.product_version_id.size_id.sizes} Qty : ${element.quantity}</span>
                <strong>${element.product_version_id.discount_price} $</strong>
            </div>
        </div>`
                        element.quantity++
                        priceSum += parseFloat(element.product_version_id.discount_price)
                        sum += 1
                    }
                    else {

                        cartMenu.innerHTML += `
            <div id='${element.product_version_id.name}'   class="sin-itme clearfix ">
            <a data-cart_item="${element.id}"  class="remove-cart"><i  class="mdi  mdi-close "></i></a>

            <a class="cart-img" href="/${element.product_version_id.slug}/"><img
                    src="${element.product_version_id.cover_image_version}" alt="" />
            
            </a>
            <div class="menu-cart-text">
                <a href="/${element.product_version_id.slug}/">
                    <h5>${element.product_version_id.name}</h5>
                </a>
                <span>Color : ${element.product_version_id.color_id.colors}</span>
                <span id='1'>Size : ${element.product_version_id.size_id.sizes} Qty : ${element.quantity}</span>
                <strong>${element.product_version_id.discount_price} $</strong>
            </div>
        </div>`
                        element.quantity++

                        priceSum += parseFloat(element.product_version_id.discount_price)
                        sum += 1
                    }
                }
            });
            cartMenu.innerHTML += `<div class="total">
        <span>total <strong>= ${priceSum} $</strong></span>
    </div><a class="goto" href="/accounts/cart/">go to cart</a>
        <a class="out-menu" href="/accounts/checkout/">Check out</a>`

            sum_and_item.innerHTML = `
        <i class="mdi mdi-cart"></i>
        ${sum} items : <strong> ${priceSum} $</strong>
    `
    if (document.getElementById('subtotal')){
            document.getElementById('subtotal').innerHTML=`$ ${priceSum}`
    document.getElementById('shipping').innerHTML=`$ ${priceSum*0.01}`
    document.getElementById('vat').innerHTML=`$ ${parseInt(priceSum*0.18)}`
    document.getElementById('order_total').innerHTML=`$ ${priceSum*1.01}`
    }

        })
}

// async function postData() {
//     let response = await fetch('http://localhost:8000/api/cart_items/');
//     let cart_items = await response.json();
//     let priceSum = 0
//     var sum = 0

//     cartMenu.innerHTML = ``

    
// }

for (var i = 0; i < wishlist.length; i++) {

    wishlist[i].addEventListener('click', function () {
        product_version_id = parseInt(this.dataset.product_version_id)
        updateWishlist(user, product_version_id)
    })
}

for (var i = 0; i < updateBtns.length; i++) {

        updateBtns[i].addEventListener('click', function () {
            var action=this.dataset.action
            if (!isNaN(this.dataset.product_version_id)){
                product_version_id = parseInt(this.dataset.product_version_id)

            }
            cart_items_quantity = 1
            updateUserOrder(cart_id, product_version_id, cart_items_quantity,action)
        })
    }

async function updateUserOrder(cart_id, product_version_id, cart_items_quantity,action) {
    response = await fetch('http://127.0.0.1:8000/api/cartitems_post/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${access}`

            },
            body: JSON.stringify({ 'cart_id': cart_id, 'product_version_id': product_version_id, 'quantity': cart_items_quantity,'action':action })
        })
        .then((response) => {
        })
        .then((data) => {
            postData()
        })
}


async function updateWishlist(user, product_version_id) {


    response = await fetch('http://127.0.0.1:8000/api/wishlist/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // 'X-CSRFToken': csrftoken,
                // 'Authorization': `Bearer ${access_token}`
            },
            body: JSON.stringify({ 'user_id_wishlist': user, 'product_version_id': product_version_id })
        })
        .then((response) => {
        })
        .then((data) => {

        })
}

postData()

const form = document.getElementById('subscription-form')
form.addEventListener('submit', function (event) {
    event.preventDefault()
    var email = document.getElementById('subscription-email')
    const data = { email: email.value };

    fetch('http://localhost:8000/api/subscribe/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if (response.ok) {

                alert('Successfully subscribed')
            }
            else {

                alert('Error')
            }
        })
        .then((data) => {

            console.log('Success:', data);
        })
        .catch((error) => {

            console.error('Error:', error);
        });
})

