
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;


$(document).ready(function(event) {
  var savings = {
    title: "Cardeneta de Poupança",
    juros: 0.005,

    calcule: function(value, months) {
      return value * Math.pow(1 + this.juros, months);
    }
  };

  var selic = {
    title: "Tesouro SELIC",
    juros: 0.00542,

    calcule: function(value, months) {
      return value * Math.pow(1 + this.juros, months);
    }
  };

  var ipca = {
    title: "Tesouro IPCA+",
    juros: 0.0075,

    calcule: function(value, months) {
      return value * Math.pow(1 + this.juros, months);
    }
  };

  $("#value").change(function(event) {
    var value = $(this).val();

    investments = [savings, selic, ipca];
    console.log(investments);

    $("#investments").empty();

    for(index in investments) {
      var $investment = $("<div />")
                          .addClass("card")
                          .append($("<div />")
                            .addClass("card-content")
                            .append($("<span />")
                              .addClass("card-title")
                              .text(investments[index].title))
                            .append($("<div />")
                              .addClass("row")
                              .append($("<div />")
                                .addClass("col s12 m6 l6")
                                .append($("<label />")
                                  .text("Valor Inicial"))
                                .append($("<span />")
                                  .addClass("card-title")
                                  .text(Math.trunc(value))))
                              .append($("<div />")
                                .addClass("col s12 m6 l6")
                                .append($("<label />")
                                  .text("Valor após 6 meses"))
                                .append($("<span />")
                                  .addClass("card-title")
                                  .text(Math.trunc(investments[index].calcule(value, 6)))))));

      $("#investments").append($investment);
    }

  });
});
