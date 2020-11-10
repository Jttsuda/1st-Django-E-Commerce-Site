{
    // Displaying Total Price
    const prices = document.querySelectorAll(".product-price");
    let totalPrice = 0;
    for(let i=0; i<prices.length; i++){
        totalPrice += parseFloat(prices[i].innerHTML.slice(1));
    }
    document.getElementById("total-price").innerHTML = totalPrice.toFixed(2);




    // Combining Multiple Products Into Same Stack
    const productNames = document.querySelectorAll(".product-name");
    let count = 0;
    for(let i=count; i<productNames.length; i++){
        let duplicateTest = productNames[i].innerHTML;
        count = 0;
        for(let x=0; x<productNames.length; x++){
            if(duplicateTest === productNames[x].innerHTML){
                count += 1;
                if(count>1){
                    productNames[x].parentElement.parentElement.parentElement.style.display = "none";
                }
            }
        }
        // Displaying Product Quantity
        document.querySelectorAll(".product-qty")[i].value = count;
        
    }



}

