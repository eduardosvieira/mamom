
var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;


$(document).ready(function(event) {
  var savings = {
    title: "Cardeneta de Poupança (6,00%)",
    juros: 0.005,
    imposto: 0,

    calcule: function(value, months) {
      return value * Math.pow(1 + this.juros, months);
    },

    calculeImpostos: function(value) {
      return value * this.imposto;
    }
  };

  var selic = {
    title: "Tesouro SELIC (6,50%)",
    juros: 0.00542,
    imposto: 0.22,

    calcule: function(value, months) {
      return value * Math.pow(1 + this.juros, months);
    },

    calculeImpostos: function(value) {
      return value * this.imposto;
    }
  };

  var ipca = {
    title: "Tesouro IPCA+ (4,50% + 3,0%)",
    juros: 0.0075,
    imposto: 0.22,

    calcule: function(value, months) {
      return value * Math.pow(1 + this.juros, months);
    },

    calculeImpostos: function(value) {
      return value * this.imposto;
    }

  };

  $("#value").change(function(event) {
    var value = $(this).val();

    investments = [savings, selic, ipca];

    $("#investments").empty();

    for(index in investments) {
      var lucro = Math.trunc(investments[index].calcule(value, 6));

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
                                .addClass("col s12 m4 l4")
                                .append($("<label />")
                                  .text("Valor Inicial"))
                                .append($("<span />")
                                  .addClass("card-title")
                                  .text(Math.trunc(value))))
                              .append($("<div />")
                                .addClass("col s12 m4 l4")
                                .append($("<label />")
                                  .text("Valor após 6 meses"))
                                .append($("<span />")
                                  .addClass("card-title")
                                  .text(lucro)))
                                .append($("<div />")
                                  .addClass("col s12 m4 l4")
                                  .append($("<label />")
                                    .text("Impostos"))
                                  .append($("<span />")
                                    .addClass("card-title")
                                    .text(investments[index].calculeImpostos(lucro - value))))));

      $("#investments").append($investment);
    }

  });
});
