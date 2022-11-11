let quantity = document.getElementById('orderQty').value;
console.log(quantity);

function addQty(){
    if(quantity < 5){
        document.getElementById('subQty').style.pointerEvents = 'auto';
        quantity++;
        console.log(quantity);
        document.getElementById('orderQty').value = quantity;
    }else{
        document.getElementById('addQty').style.pointerEvents = 'none';
        console.log('You connot order more than 5 items.')
        return;
    }
};

function subQty(){
    if(quantity > 1){
        document.getElementById('addQty').style.pointerEvents = 'auto';
        quantity--;
        console.log(quantity);
        document.getElementById('orderQty').value = quantity;
    }else{
        document.getElementById('subQty').style.pointerEvents = 'none';
        console.log('You cannot order less than 1 item.')
        return;
    }
};
    
const addToCartBtn = document.getElementById("addToCart")
addToCartBtn.addEventListener('click', function(e){
    e.preventDefault()
    productId = this.dataset.product
    console.log(productId)
    url = "{% url 'Myapp:cart' %}"
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId':productId})
    })
    .then((response) => response.text())
    .then((data) => {
        console.log(data)
    })
});