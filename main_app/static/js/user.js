const TOGGLER = document.getElementById("toggler"); //hamburger menu
var navLink = document.getElementById("links"); //navigatiion links

TOGGLER.addEventListener("click", function () {
  navLink.classList.toggle("active");
});

//FORM VALIDATIION FOR THE CONTACT FORM
var form = document.getElementById("form");

form.addEventListener("submit", function (e) {
 
  var name = document.getElementById("name").value; //name input value
  var email = document.getElementById("email").value; //email inout value
  var message = document.getElementById("message").value; //message input value

  function nameCheck() {
    if (name == "") {
      e.preventDefault();
      document.getElementById("name-error").classList.add("active");
      document.querySelector("small.name-error").classList.add("active");
    }
  }

  nameCheck();

  function emailCheck() {
    if (email == "") {
      e.preventDefault();
      document.getElementById("email-error").classList.add("active");
      document.querySelector("small.email-error").classList.add("active");
    }
  }

  emailCheck();

  function messageCheck() {
    if (message == "") {
      e.preventDefault();
      document.getElementById("message-error").classList.add("active");
      document.querySelector("small.message-error").classList.add("active");
    }
  }
  messageCheck();
});
