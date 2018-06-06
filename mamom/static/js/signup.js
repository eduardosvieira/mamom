$(document).ready(function(){
  $('.sidenav').sidenav();

  $("#newPassword2").on("change", function(event) {
    var $p1 = $("#newPassword");

    if($p1.val() == $(this).val()) {
      $(this).css("border-bottom", "2px solid green");
      $("#password-error").css("font-weight", "bold").css("display", "block").css("color", "green").text("Tudo bem. Senhas combinam!")

    } else {
      $(this).css("border-bottom", "2px solid red");
      $("#password-error").css("font-weight", "bold").css("display", "block").css("color", "red").text("Ops! Senhas não combinam!")

    }
  });

});
