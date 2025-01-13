$(document).ready(function() {
  // Ajout solde
  $("#ajoutSolde").on('submit', function(e) {
      e.preventDefault();
      $.ajax({
          type: 'POST',
          url: "./../ajout_solde_admin/",
          data: new FormData(this),
          dataType: 'json',
          contentType: false,
          cache: false,
          processData: false,
          success: function(response) {
              if (response.success) {
                  $("#ajoutSolde")[0].reset();
                  $(".retour1").show();
                  $(".retour1").html(response.message);
                  setTimeout(function() {
                      $(".retour1").hide();
                  }, 5000);
              } else {
                  $(".retour1").show();
                  $(".retour1").html(response.erreur || "Une erreur s'est produite");
                  setTimeout(function() {
                      $(".retour1").hide();
                  }, 5000);
              }
          },
        
      });
  });
});