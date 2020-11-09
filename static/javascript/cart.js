{
    // Displaying Total Price
    const prices = document.querySelectorAll(".product-price");
    let totalPrice = 0;
    for(let i=0; i<prices.length; i++){
        totalPrice += parseFloat(prices[i].innerHTML.slice(1));
    }
    document.getElementById("total-price").innerHTML = totalPrice;



}