function myFunction() {
    var element = document.getElementById("menu-main");
    if(element.classList.length == 0){
        element.classList.add("menu-open");
    }
    else{
        element.classList.remove("menu-open");
    }
}