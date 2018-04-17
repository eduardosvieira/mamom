var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;


$(document).ready(function(event){
  $("#btnEditPI").click(function(event){
    var userId = $("#userId").val();
    var name = $("#name").val();
    var email = $("#email").val();

    $.ajax({
      url: URL + "/mamom/users/" + userId + "/",
      type: "PUT",
      data: {"name": name, "email": email},
      success: function(data) {
        window.location.replace(URL + "/mamom/");
      }
    });
  });
});
