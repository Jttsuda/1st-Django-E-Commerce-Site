{
    // Combining Multiple Products Into Same Stack
    const productNames = document.querySelectorAll(".product-name");
    const productBoxes = document.querySelectorAll(".product-box-margin");
    let count = 0;
    for(let i=count; i<productNames.length; i++){
        count = 0;
        for(let x=0; x<productNames.length; x++){
            if(productNames[i].innerHTML === productNames[x].innerHTML){
                count += 1;
                if(count>1){
                    productBoxes[x].style.position = "fixed";
                    productBoxes[x].style.display = "none";
                } else {
                    productBoxes[x].style.display = "inline-block";
                }
            }
        }
        // Displaying Product Quantity
        document.querySelectorAll(".product-qty")[i].value = count;
        
    }
    

    
    // Displaying Total Price
    const prices = document.querySelectorAll(".product-price");
    let totalPrice = 0;
    for(let i=0; i<prices.length; i++){
        totalPrice += parseFloat(prices[i].innerHTML.slice(1));
    }
    document.getElementById("total-price").innerHTML = totalPrice.toFixed(2);
    




}

