{
    const checkoutBtns = document.querySelectorAll(".checkout-buttons");
    let shippingBox = document.getElementById("shipping-form");
    let paymentBox = document.getElementById("payment-form");

    checkoutBtns.forEach(btn => btn.addEventListener("click", function(e){
        if(e.target.dataset.action === "continue"){
            shippingBox.style.height = "0px";
            paymentBox.style.height = "480px";
        } else if(e.target.dataset.action === "back"){
            paymentBox.style.height = "0px";
            shippingBox.style.height = "410px";
        }
    })
    );
    
    
}