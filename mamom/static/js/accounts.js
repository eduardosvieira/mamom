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

function fillModalCreateTransation() {
  $.ajax({
    url: URL + "/mamom/categories/",
    type: "GET",
    success: function(data) {
      $("#category").empty();

      for(index in data) {
        $("#category").append($("<option />").text(data[index]["name"]).attr("value", data[index]["_id"]))
      }

      $('select').formSelect();

    }
  });
}

$(document).ready(function(){
  $('.sidenav').sidenav();

  $('.tabs').tabs();

  $('.modal').modal();

  $('select').formSelect();

  $('.datepicker').datepicker({firstDay: true,
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
  $(".datas").each(function(event) {
      var data = ($(this).text()).split("/");

      $(this).text(data[0] + " de " + getMonth(data[1]) + " de " + data[2]);
  });

  $("#btnDeleteUser").click(function(event) {
    $.ajax({
      url: URL + "/mamom/users/",
      type: "DELETE",
      success: function(data) {
        window.location.replace(URL + "/mamom/");
      }
    });
  });


  $("#btnDeleteTransation").click(function(event) {
    var accountId = $("#accountId").val();
    var transationId = $("#modal-edit-transation-id").val();

    $.ajax({
      url: URL + "/mamom/transations/" + transationId + "/",
      type: "DELETE",
      success: function(data) {
        window.location.replace(URL + "/mamom/accounts/" + accountId + "/");
      }
    });
  });

  $("#btnEditTransation").click(function(event){
    var accountId = $("#accountId").val();
    var transationId = $("#modal-edit-transation-id").val();
    var name = $("#modal-edit-transation-name").val();
    var categoryId = $("#modal-edit-transation-category :checked").val();

    $.ajax({
      url: URL + "/mamom/transations/" + transationId + "/",
      type: "PUT",
      data: {"name": name, "categoryId": categoryId},
      success: function(data) {
        window.location.replace(URL + "/mamom/accounts/" + accountId + "/");
      }
    });
  });


  $(".transation").dblclick(function(event){
    var transationId = $(this).children(".transationId").val();

    $("#modal-edit-transation-id").attr("value", transationId);

    /*carregando categorias*/
    $.ajax({
      url: URL + "/mamom/categories/",
      type: "GET",
      success: function(data) {
        $("#modal-edit-transation-category").empty();

        for(index in data) {
          $("#modal-edit-transation-category").append($("<option />").text(data[index]["name"]).attr("value", data[index]["_id"]))
        }

        $('select').formSelect();
      }
    });

    $("#modal-edit-transation").modal('open');
  });


  $("#btnCreateTransation").click(function(event){
    var accountId = $("#accountId").val();
    var name = $("#name").val();
    var categoryId = $("#category :checked").val();
    var createdAt = $("#createdAt").val();
    var value = $("#value").val();

    $.ajax({
      url: URL + "/mamom/transations/",
      type: "POST",
      data: {"accountId": accountId, "name": name, "categoryId": categoryId, "createdAt": createdAt, "value": value},
      success: function(data) {
        window.location.replace(URL + "/mamom/accounts/" + accountId + "/");
      }
    });


  });
});
