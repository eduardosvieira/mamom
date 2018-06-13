
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;


function getMonth(month) {
  switch (month) {
    case "01":
      return "Janeiro";
      break;
    case "02":
      return "Fevereiro";
      break;
    case "03":
      return "Março";
      break;
    case "04":
      return "Abril";
      break;
    case "05":
      return "Maio";
      break;
    case "06":
      return "Junho";
      break;
    case "07":
      return "Julho";
      break;
    case "08":
      return "Agosto";
      break;
    case "09":
      return "Setembro";
      break;
    case "10":
      return "Outubro";
      break;
    case "11":
      return "Novembro";
      break;
    case "12": "Dezembro"
    default:
      return "Mês errado";

  }
}


$(document).ready(function(){
  $('.sidenav').sidenav();

  $('.tabs').tabs();

  $('.modal').modal();

  $('.tooltipped').tooltip();

  $('.datepicker').datepicker({
        firstDay: true,
        format: 'dd/mm/yyyy',
        closeOnSelect: true,
        i18n: {
            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
            monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'],
            weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'],
            weekdaysAbbrev: ["D","S", "T", "Q", "Q", "S", "S"],
            cancel: "Cancelar"
        }});

  /*Formata o prazo para realização da meta*/
  $(".deadlines").each(function(event) {
    var data = ($(this).text()).split("/");

    $(this).text(data[0] + " de " + getMonth(data[1]) + " de " + data[2]);
  });

  function calculeProgress() {
    $(".progressBar").each(function(index, element) {
      var progress = ( $(this).siblings(".goalBalance").val() / $(this).siblings(".goalValue").val() ) * 100;
      progress = "" + progress + "%";

      $(this).css("width", progress);
    });

  }

  calculeProgress();

  $("#btnDeleteUser").click(function(event) {
    $.ajax({
      url: URL + "/mamom/users/",
      type: "DELETE",
      success: function(data) {

        window.location.replace(URL + "/mamom/");
      }
    });
  });

  $("#btnDeleteAccount").click(function(event) {
    var accountId = $("#modal-edit-account-id").val();

    $.ajax({
      url: URL + "/mamom/accounts/" + accountId + "/",
      type: "DELETE",
      success: function(data) {
        window.location.replace(URL + "/mamom/");

      }
    });
  });

  $("#btnDeleteGoal").click(function(event) {
    var goalId = $("#modal-edit-goal-id").val();

    $.ajax({
      url: URL + "/mamom/goals/" + goalId + "/",
      type: "DELETE",
      success: function(data) {
        window.location.replace(URL + "/mamom/");
      }
    });
  });

  $("#btnEditGoal").click(function(event){
    var goalId = $("#modal-edit-goal-id").val();

    var name = $("#modal-edit-goal-name").val();
    var deadline = $("#modal-edit-goal-deadline").val();
    var value = $("#modal-edit-goal-value").val();

    $.ajax({
      url: URL + "/mamom/goals/" + goalId + "/",
      type: "PUT",
      data: {"name": name, "deadline": deadline, "value": value},
      success: function(data) {
        window.location.replace(URL + "/mamom/");
      }
    });
  });

  $(".goal").dblclick(function(event){
    var goalId = $(this).children().children().children().children(".goalId").val();

    $("#modal-edit-goal-id").attr("value", goalId);

    $("#modal-edit-goal").modal("open");

  });

  $("#btnEditAccount").click(function(event){
    var accountId = $("#modal-edit-account-id").val();
    var name = $("#modal-edit-account-name").val();

    $.ajax({
      url: URL + "/mamom/accounts/" + accountId + "/",
      type: "PUT",
      data: {"name": name},
      success: function(data) {
        window.location.replace(URL + "/mamom/");

      }
    });
  });

  $(".account").dblclick(function(event){
    var accountId = $(this).children().children().children().children(".accountId").val();

    $("#modal-edit-account-id").attr("value", accountId);

    $("#modal-edit-account").modal('open');
  });

  $("#btnCreateGoal").click(function(event){
    var name = $("#goal-name").val();
    var value = $("#goal-value").val();
    var deadline = $("#goal-deadline").val();

    if(name) {
      $.ajax({
        url: URL + "/mamom/goals/",
        type: "POST",
        data: {"name": name, "value": value, "deadline": deadline},
        success: function(data) {
          window.location.replace(URL + "/mamom/")
        },
        error: function(data) {
          $("#error").css("display", "block").text("Não foi possível criar uma nova meta agora. Tente mais tarde!");
        }
      });
    } else {
      $("#error").css("display", "block").text("O nome da meta não oode ser vazio!");
    }
  });


  $("#btnCreateAccount").click(function(event){
    var name = $("#name").val();
    var balance = $("#balance").val();

    if(name) {
      $.ajax({
        url: URL + "/mamom/accounts/",
        type: "POST",
        data: {"name": name, "balance": balance},
        success: function(data) {
          window.location.replace(URL + "/mamom/");

        },
        error: function(data) {
          $("#message-account").css("display", "block").text("Houve um problema. Tente mais tarde!");

        }
      });
    } else {
      $("#message-account").css("display", "block").text("O nome da conta não pode ser vazio!");

    }
  });

});
