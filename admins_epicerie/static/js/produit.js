$(document).ready(function(){

  $('#types1').change(function() {
    var id = $(this).val();

    $.ajax({
        method: "POST",
        url: "./../affiche_produits_admin/",
        data: { id: id },
        success: function(response) {
            if (response.html) {
                $("#produitAdmin").html(response.html);
            } else if (response.error) {
                console.error(response.error);
            }
        },
        error: function(xhr, status, error) {
            console.error("Erreur lors de la requête AJAX :", error);
        }
    });
});
    
      //Ajout produit
    
      $("#ajoutProduit").on('submit', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: './../ajout_produit/',
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData:false,
            success: function(reponse){
                if(reponse == 0){
                    $("#ajoutProduit")[0].reset();
                    $(".retour").show();
                    $(".retour").html("Produit ajouté avec succès");
                    setTimeout(function(){$(".retour").hide();},5000);
                } else {
                    $(".retour").show();
                    $(".retour").html(reponse);
                    setTimeout(function(){$(".retour").hide();},5000);
                }
            }
        });
    });
    
    
    });