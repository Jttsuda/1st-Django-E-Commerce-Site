{
    const categories = document.querySelectorAll(".shop-nav-buttons");
    for(let i = 0; i < categories.length; i++){
        categories[i].addEventListener("click", testFunc);
    }

    function testFunc(e){
        categories.forEach(x=> x.classList.remove("clear-background"));
        e.target.classList.add("clear-background");
    }



}