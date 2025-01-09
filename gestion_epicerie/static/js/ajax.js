$(document).ready(function(e){

    // Inscription
    $("#forminscription").on('submit', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: './../inscription/',  // URL Django
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData:false,
            success: function(reponse){
                if(reponse.status == 0) {
                    $("#forminscription")[0].reset();
                    $(".alert-inscription-success").show();
                    $(".alert-inscription-success").html('VOTRE INSCRIPTION A ETE ENREGISTREE AVEC SUCCES, VEUILLEZ VOUS CONNECTER MAINTENANT !');
                    setTimeout(function(){
                        $(".alert-inscription-success").hide();
                    }, 5000);
                } else {
                    $(".alert-inscription-danger").show();
                    $(".alert-inscription-danger").html(reponse.status);
                    setTimeout(function(){
                        $(".alert-inscription-danger").hide();
                    }, 5000);
                }
            }
        });
    });

    // Connexion
    $("#formconnexion").on('submit', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '',  // URL Django
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData:false,
            success: function(reponse){
                if(reponse['status'] == 0) {
                    window.location.href = reponse['url'];
                } else {
                    $(".alert-warning").show();
                    $(".alert-warning").html(reponse['status']);
                    setTimeout(function(){
                        $(".alert-warning").hide();
                    }, 5000);
                }
            }
        });
    });

    // Ajout avis produit
    $("#formAvisProduit").on('submit', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/ajouter-avis/',  // URL Django
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData:false,
            success: function(reponse){
                if(reponse.status == 0) {
                    $(".alert-inscription-success").show();
                    $(".alert-inscription-success").html('VOTRE AVIS A ETE ENREGISTRE AVEC SUCCES, MERCI!');
                    setTimeout(function(){
                        $(".alert-inscription-success").hide();
                    }, 5000);
                } else {
                    $(".alert-inscription-danger").show();
                    $(".alert-inscription-danger").html(reponse.status);
                    setTimeout(function(){
                        $(".alert-inscription-danger").hide();
                    }, 5000);
                }
            }
        });
    });

});
