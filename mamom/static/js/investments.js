
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

window.onload = function () {
  var chart = new CanvasJS.Chart("chartContainer", {

    title:{
      text: "Rendimento"
    },
    data: [//array of dataSeries
      { //dataSeries object

       /*** Change type "column" to "bar", "area", "line" or "pie"***/
       type: "line",
       dataPoints: [
       { label: "Valor inicial", y: 50 },
       { label: "Valor final", y: 560 }
       ]
     }
     ]
   });

  chart.render();
}

$(document).ready(function(event) {
  $("#value").change(function(event) {
    var value = $(this).val();

    $.ajax({
      url: URL + "/mamom/investments/",
      type: "POST",
      data: {
        "value": value
      },
      success: function(data) {
        $("#investments").empty();

        for(index in data) {
          var $investment = $("<div />")
                              .addClass("card")
                              .append($("<div />")
                                .addClass("card-content")
                                .append($("<span />")
                                  .addClass("card-title")
                                  .text(data[index]["name"]))
                                .append($("<span />")
                                  .addClass("card-title")
                                  .text(data[index]["value"])));

          $("#investments").append($investment);
        }
      }
    });
  });
});
