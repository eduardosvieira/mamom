var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

function fillModalCreateTransation() {
  $.ajax({
    url: URL + "/mamom/categories/",
    type: "GET",
    success: function(data) {
      $("#category").empty();

      for(index in data) {
        $("#category").append($("<option />").text(data[index]["name"]).attr("value", data[index]["_id"]))
      }

      $('select').material_select();
    }
  });
}

$(document).ready(function(){
  $(".button-collapse").sideNav();

  $('.tabs').tabs();

  $('.modal').modal();

  $('select').material_select();

  $("#btnCreateAccount").click(function(event){
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
