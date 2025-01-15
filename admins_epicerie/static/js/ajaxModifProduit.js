$(document).ready(function(){

          //Modifier produit
      
          $("#modifProduit").on('submit', function(e) {
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: './../../modifier_produit_ajax/', 
                data: new FormData(this),
                dataType: 'json',
                contentType: false,
                cache: false,
                processData: false,
                success: function(reponse) {
                    if (reponse.status === "Succès") {
                        $(".retour").show();
                        $(".retour").html(reponse.message);
                        setTimeout(function() {
                            window.location.href = './../../produits/'; 
                        }, 5000);
                    } else {
                        $(".retour").show();
                        $(".retour").html(reponse.message);
                        setTimeout(function() {
                            $(".retour").hide();
                        }, 5000);
                    }
                },
                error: function(xhr, status, error) {
                    $(".retour").show();
                    $(".retour").html("Une erreur est survenue lors de la modification du produit.");
                    setTimeout(function() {
                        $(".retour").hide();
                    }, 5000);
                }
            });
        });
      
      });