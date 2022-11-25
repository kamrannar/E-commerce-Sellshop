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
let cartTable = document.getElementById('cart_table')
let wishlistTable = document.getElementById('wishlist_table')
let wishlistRmv = document.getElementsByClassName('remove-wishlist')
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
    await fetch('/api/cart_items/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',

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
                        priceSum += parseFloat(element.product_version_id.discount_price).toFixed(2)
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

                        priceSum +=element.product_version_id.discount_price
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
            document.getElementById('subtotal').innerHTML=`$ ${parseFloat(priceSum).toFixed(2)}`
    document.getElementById('shipping').innerHTML=`$ ${parseFloat(priceSum*0.01).toFixed(2)}`
    document.getElementById('vat').innerHTML=`$ ${parseInt(priceSum*0.18)}`
    document.getElementById('order_total').innerHTML=`$ ${parseFloat(priceSum*1.01).toFixed(2)}`
    document.getElementById('order_total').value=parseFloat(priceSum*1.01).toFixed(2)
    console.log(document.getElementById('order_total').value)
    }
    for (var i = 0; i < removeBtn.length; i++) {

        removeBtn[i].addEventListener('click', function () {
            var action=this.dataset.action
            var cart_item=this.dataset.cart_item

            deleteCartItem(cart_id, product_version_id, action,cart_item)

        })
      
    }

        })

}
getCart()
async function getCart() {
    await fetch('/api/cart_items/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',

        },
    })
        .then((response) => response.json())
        .then((data) => {
            if (cartTable){
                cartTable.innerHTML = ``
                data.forEach((element) => {
                    if (element.cart_id.user_id.id == cart_idd) {
                            cartTable.innerHTML += `<tr>
                            <td class="td-img text-left">
                                <a href="#"><img src="${element.product_version_id.cover_image_version}"
                                        alt="Add Product" /></a>
                                <div class="items-dsc">
                                    <h5><a href="#">${element.product_version_id.name}</a></h5>
                                    <p class="itemcolor">Color :
                                        <span>${element.product_version_id.color_id.colors}</span></p>
                                    <p class="itemcolor">Size :
                                        <span>${element.product_version_id.size_id.sizes}</span></p>
                                </div>
                            </td>
                            <td>${element.product_version_id.discount_price}</td>
    
                            <td>
                            <input type="number" class="number" data-stocks=${element.product_version_id.stocks} data-cart_item="${element.id}" value="${element.quantity}" min=0 data-product_version_id="${element.product_version_id.id}"/>
                            </td>
    
    
                            <td>
                                <strong>$  ${element.quantity*element.product_version_id.discount_price} </strong>
                            </td>
                            <td><button class="remove-cart" data-cart_item="${element.id}" action="remove" data-product_version_id="${element.product_version_id.id}"><i class="mdi mdi-close" title="Remove this product"></i></button></td>
                        </tr>`
                    }
                    for (var i = 0; i < removeBtn.length; i++) {
                        removeBtn[i].addEventListener('click', function () {
                            var action=this.dataset.action
                            var cart_item=this.dataset.cart_item
                            deleteCartItem(cart_id, product_version_id, action,cart_item)

        
                        })
                    }
                    changeq=document.getElementsByClassName('number')
                    for (var i = 0; i < changeq.length; i++) {

                        changeq[i].addEventListener('click', function () {
                                let e =cart_items_quantity
                                cart_items=this.dataset.cart_item   
                                element.quantity=this.value
                                cart_items_quantity=this.value
                                stocks=this.dataset.stocks
                                let d =cart_items_quantity
                                console.log(e,d)
                                if (e>d){
                                    console.log('plus-before',stocks) 
                                    
                                    stocks++

                                changeQuantity(cart_items,cart_items_quantity,stocks)
                                console.log('plus',stocks) 
                                    getCart()
                                    element.product_version_id.stocks=stocks
                                }
                                else{

                                    if (stocks==1){

                                        alert('No more items left in stock')
                                        location.reload()
                                    }
                                    else{
                                        getCart()

                                        stocks--

                                changeQuantity(cart_items,cart_items_quantity,stocks)
                                element.product_version_id.stocks=stocks
                                    }
                                  
                                }
                                

                                if(this.value==0){    
                                    var action=this.dataset.action
                                    var cart_item=this.dataset.cart_item
                                    deleteCartItem(cart_id, product_version_id, action,cart_item)
                                }
                            if (!isNaN(this.dataset.product_version_id)){
                                product_version_id = parseInt(this.dataset.product_version_id)
                            }
                           

                        })
                    }
                
                })
            }
           ;

        })
}
function changeQuantity(cart_items,cart_items_quantity,stocks){

     fetch('/api/cart_items/'+cart_items+'/', {
        
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',

        },
        body: JSON.stringify({ 'quantity': cart_items_quantity})
    })
        .then((response) => response.json())
        .then((data) => {  
fetch('/api/product_version/'+product_version_id+'/', {
        
    method: 'PATCH',
    headers: {
        'Content-Type': 'application/json',

    },
    body: JSON.stringify({ 'stocks':stocks })
})
    .then((response) => response.json())
    .then((data) => {  
getCart()
    }
    )
        })
}


async function getWishlist() {
    await fetch('/api/wishlist_detailed/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',

        },
    })
        .then((response) => response.json())
        .then((data) => {

            data.forEach((element) => {
                if (element.user_id_wishlist.id == user.id) {
                    if (wishlistTable){
                        wishlistTable.innerHTML += `<tr>
                        <td class="td-img text-left">
                            <a href="#"><img src="${ element.product_version_id.cover_image_version }"
                                    alt="Add Product" /></a>
                            <div class="items-dsc">
                                <h5><a href="#">${ element.product_version_id.name }</a></h5>
                                <p class="itemcolor">Color : <span>${ element.product_version_id.color_id.colors }</span></p>
                                <p class="itemcolor">Size : <span>${ element.product_version_id.size_id.sizes }</span></p>
                            </div>
                        </td>
                        <td>${ element.product_version_id.discount_price }</td>
                        <td>${element.product_version_id.stocks}</td>
               
                        <td><button class="remove-wishlist" data-product_version_id="${element.product_version_id.id}"><i class="mdi mdi-close" title="Remove this product"></i></button></td>
                    </tr>`
                    }
                    
                        
                }

                for (var i = 0; i < wishlistRmv.length; i++) {

                    wishlistRmv[i].addEventListener('click', function () {
                        product_version_id = parseInt(this.dataset.product_version_id)
                        var wishlist_item=element.id
                        deleteWishlist( product_version_id,user,wishlist_item)
                    })
                }

            });
            
            
    
        })
}
getWishlist()

for (var i = 0; i < wishlist.length; i++) {

    wishlist[i].addEventListener('click', function () {
        product_version_id = parseInt(this.dataset.product_version_id)
        updateWishlist(user, product_version_id)
    })
}


    for (var i = 0; i < document.getElementsByClassName('update-cart').length; i++) {
        document.getElementsByClassName('update-cart')[i].addEventListener('click', function () {
            var action=this.dataset.action
            if (!isNaN(this.dataset.product_version_id)){
                product_version_id = parseInt(this.dataset.product_version_id)

            }
            console.log()
            cart_items_quantity = 1
            updateUserOrder(cart_id, product_version_id, cart_items_quantity,action)
        })
    }


async function updateUserOrder(cart_id, product_version_id, cart_items_quantity,action) {
    response = await fetch('/api/cartitems_post/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',


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


    response = await fetch('/api/wishlist/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify({ 'user_id_wishlist': user, 'product_version_id': product_version_id })
        })
        .then((response) => {
        })
        .then((data) => {
            postData()
            getCart()
            getWishlist()
        })
}
var removeBtn=document.getElementsByClassName('remove-cart')

async function deleteCartItem(cart_id,action, product_version_id,cart_item) {

    response = await fetch('/api/cart_items/'+cart_item+'/',
        {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify({ 'cart_id': cart_id, 'product_version_id': product_version_id, 'action':action,quantity:'0' })
        })
        .then((response) => {
        })
        .then((data) => {
            postData()
            getCart()
        })
}

async function deleteWishlist( product_version_id,user,wishlist_item) {

    response = await fetch('/api/wishlist/'+wishlist_item+'/',
        {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify({'user_id_wishlist': user, 'product_version_id': product_version_id })
        })
        .then((response) => {
        })
        .then((data) => {
            postData()
            getCart()
        })
}
postData()

const form = document.getElementById('subscription-form')
form.addEventListener('submit', function (event) {
    event.preventDefault()
    var email = document.getElementById('subscription-email')
    const data = { email: email.value };

    fetch('/api/subscribe/', {
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

                alert('This Email is already subscribed')
            }
        })
        .then((data) => {

            console.log('Success:', data);
        })
        .catch((error) => {

            console.error('Error:', error);
        });
})
