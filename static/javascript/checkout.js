{
    let checkoutBtns = document.querySelectorAll(".checkout-buttons");
    let shippingBox = document.getElementById("shipping-form");
    let paymentBox = document.getElementById("payment-form");

    checkoutBtns.forEach(btn => btn.addEventListener("click", function(e){
        if(e.target.dataset.action === "continue"){
            shippingBox.style.display = "none";
            paymentBox.style.display = "block";
        } else if(e.target.dataset.action === "back"){
            shippingBox.style.display = "block";
            paymentBox.style.display = "none";
        }
    })
    );
    
    
}