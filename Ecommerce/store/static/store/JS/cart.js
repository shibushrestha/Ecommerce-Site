var addToCartBtns = document.getElementsByClassName('add-to-cart')

for (var i = 0; i < addToCartBtns.length; i++){
    addToCartBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        
        if(User === "AnonymousUser"){
            console.log('You are not authenticeted')
        }else{
            updateUserOrder(productId, action)
            }
    })
}


function updateUserOrder(productId, action){
    var url = '/store/updatecart/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}