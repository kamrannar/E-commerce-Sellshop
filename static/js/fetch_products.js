var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var product_version_id = this.dataset.product
        console.log('data',this.dataset.product)
        var action = this.dataset.action
        console.log(product_version_id)
        updateUserOrder(product_version_id,action,1)
    })

}

async function updateUserOrder(product_version_id,action,cart_id){

    fetch('http://127.0.0.1:8000/api/cart_items/',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
          },
        body:JSON.stringify({'product_version_id':product_version_id,'action':action,'cart_id':cart_id})
    })
    .then((response) => {
        return response.json()})
    .then((data)=>{
        console.log('data',data)
    })
    .catch((err) => console.log(err))
}




async function postData(url){
     response = await fetch(url,{
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
    })
        return response.json()}

postData('http://127.0.0.1:8000/api/cart_items/')
    .then((data)=>{
        let cartMenu = document.getElementById('cartdrop')
        let cartitema = document.getElementById('cartitema')
        let sum = 0
        let priceSum = 0
        data.forEach((element) =>{
            if (element.cart_id.user_id.id==user){
            sum+=1
                
                cartMenu.innerHTML+=`
                <div class="sin-itme clearfix">
                <i class="mdi mdi-close"></i>
    
                <a class="cart-img" href=""><img
                        src="${element.product_version_id.cover_image_version}" alt="" />
                
                </a>
                <div class="menu-cart-text">
                    <a href="#">
                        <h5>${element.product_version_id.name}</h5>
                    </a>
                    <span>Color : ${element.product_version_id.color_id.colors}</span>
                    <span>Size : ${element.product_version_id.size_id.sizes}</span>
                    <strong>${element.product_version_id.discount_price} $</strong>
                </div>
            </div>
                `   
                priceSum+=parseFloat(element.product_version_id.discount_price)    
           
            }
            
        });
        cartMenu.innerHTML+=`
        <div class="total">
								<span>total <strong>= ${priceSum} $</strong></span>
							</div>
                            
        `
        cartitema.innerHTML+=`
        <i class="mdi mdi-cart"></i>
        ${sum} items : <strong> ${priceSum} $</strong>
    `
       
    })
