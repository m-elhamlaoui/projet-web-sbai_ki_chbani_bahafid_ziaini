$(document).ready(function (e) {

    //commander
  
    $("#commander").on('submit', function (e) {
          e.preventDefault();
          $.ajax({
              type: 'POST',
              url: './../commander/',
              data: new FormData(this),
              dataType: 'json',
              contentType: false,
              cache: false,
              processData: false,
              success: function (reponse) {
                  if (reponse == "0") {
                      load_cart_data();
                      $(".alert-payement-success").show();
                      $(".alert-payement-success").html('VOTRE COMMANDE A ETE ENREGISTREE AVEC SUCCES A BIENTOT ! ');
                      setTimeout(function () { $(".alert-payement-success").hide(); }, 5000);
                  }
  
                  else if (reponse == "-1") {
                      window.location.href = "./../../gestion_epicerie/connexion/";
                  }
  
  
                  else {
                      $(".alert-payement-danger").show();
                      $(".alert-payement-danger").html(reponse);
                      setTimeout(function () { $(".alert-payement-danger").hide(); }, 5000);
                  }
  
              }
  
          });
      });
  })