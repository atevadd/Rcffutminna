const TOGGLER = document.getElementById('toggler'); //hamburger menu
var navLink = document.getElementById('links'); //navigatiion links

TOGGLER.addEventListener("click", function(){
    navLink.classList.toggle('active');
})

var date = new Date();
