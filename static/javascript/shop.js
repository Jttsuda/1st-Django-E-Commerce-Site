{
    const categories = document.querySelectorAll(".shop-nav-buttons");
    let products = document.querySelectorAll(".products");
    let productCategory = document.querySelectorAll(".product-category");


    // Shop Filter
    categories.forEach(x=> x.addEventListener("click", shopFilter));
    function shopFilter(e){
        categories.forEach(x=> x.classList.remove("clear-background"));
        e.target.classList.add("clear-background");


        products.forEach(x=> x.style.display = "inline-block");
        // Looking for matching Products based on Tags
        for(let i=0; i<productCategory.length; i++){
            let searchCategory = e.target.textContent.toLowerCase();
            let match = productCategory[i].innerText.toLowerCase().includes(searchCategory);
            if(e.target.textContent === "All") {
                products.forEach(x=> x.style.display = "inline-block");
            } else if(!match){
                products[i].style.display = "none";
            } 

        }

        document.getElementById("search-category").innerHTML = e.target.innerText;

    }




}