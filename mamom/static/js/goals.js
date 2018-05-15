var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;


$(document).ready(function(){
  $('.modal').modal();

  /*Quando o usuário clicar no botão para depositar o valor na conta.*/
  $("#btnDepositInGoal").on("click", function(event){
    /*ID da meta*/
    var goalId = $("#goalId").val();

    /*Valor para depositar*/
    var value = $("#modal-deposit-goal-value").val();

    $.ajax({
      url: URL + "/mamom/goals/" + goalId + "/balance/",
      type: "PUT",
      data: {"value": value},
      success: function(data) {
        window.location.replace(URL + "/mamom/");
      },
      error: function(data) {

      }
    });
  });

});
