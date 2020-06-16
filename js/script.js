// THE MENU ICON ELEMENT
const MENUICON = document.getElementById('menu');
//THE CLOSE BUTTON ON THE SDIE MENU
const CLOSEBTN = document.getElementById('sidenav');
//THE SIDE MENU ELEMENT
var sideMenu = document.getElementById('side-nav');


//FUNCTION THAT OPEN THE MENU
function openNav(){
    sideMenu.style.width = "75%";
}

MENUICON.addEventListener("click", openNav, false);

//FUNCTION THE CLOSES THE MENU
function closeNav(){
    sideMenu.style.width = "0";
}

CLOSEBTN.addEventListener("click", closeNav, false);