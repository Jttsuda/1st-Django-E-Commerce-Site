{
    const categories = document.querySelectorAll(".shop-nav-buttons");
    let products = document.querySelectorAll(".product-margin");
    let productCategory = document.querySelectorAll(".product-category");


    // Shop Categories Filter -----
    categories.forEach(x=> x.addEventListener("click", shopFilter));
    function shopFilter(e){
        categories.forEach(x=> x.classList.remove("clear-background"));
        e.target.classList.add("clear-background");

        // Looking for matching Products based on Tags
        products.forEach(x=> x.style.display = "inline-block");
        for(let i=0; i<productCategory.length; i++){
            let searchCategory = e.target.textContent.toLowerCase();
            let match = productCategory[i].innerText.toLowerCase().includes(searchCategory);
            if(e.target.textContent === "All") {
                products.forEach(x=> x.style.display = "inline-block");
            } else if(!match){
                products[i].style.display = "none";  
            } 
            
        }
        // Displaying Current Category Being Searched
        document.getElementById("search-category").innerHTML = e.target.innerText;
    }
    
    


    // Shop Search Box -----
    const productName = document.querySelectorAll(".product-name");
    let productNameArr = Array.from(productName);
    let searchBox = document.getElementById("product-search-box");

    searchBox.addEventListener("keyup", searchProducts);
    function searchProducts(e){
        // Looking for matching Products based on Tags
        products.forEach(x=> x.style.display = "inline-block");
        for(let i=0; i<productCategory.length; i++){
            let searchCategory = document.querySelector(".clear-background").textContent.toLowerCase();
            let match = productCategory[i].innerText.toLowerCase().includes(searchCategory);
            if(searchCategory === "all") {
                products.forEach(x=> x.style.display = "inline-block");
            } else if(!match){
                products[i].style.display = "none";  
            }     
        }
        // Looking for matching Products based on Search Box
        let newSearch = document.getElementById("product-search-box").value.toLowerCase();
        for(let i=0; i<products.length; i++){
            if(products[i].style.display === "inline-block"){
                if(productNameArr[i].innerHTML.toLowerCase().includes(newSearch)){
                        products[i].style.display = "inline-block";
                    } else {
                        products[i].style.display = "none";
                    }
                }
            }

            // Displaying No Result
        let productsArray = [];
        let noResults = document.getElementById("no-results");
        noResults.style.display = "none";

        for(let i=0; i<products.length; i++){
            productsArray.push(products[i].style.display);
        }
        
        if(productsArray.every(x=> x === "none")){
            noResults.style.display = "inline-block";
        }




    }





}