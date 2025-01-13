$(document).ready(function(){

    $(document).on('click', '.recommander', function(){
    var product_id = $(this).attr("id");
    {
        $.ajax({
            url:"./../recommander_produit/",
            method:"POST",
            data:{product_id:product_id,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()  // Inclure le token CSRF
            },
            success:function(response)
            {
                if (response.status === 'success') {
                    $(".alert-recommandation-success" + product_id).show();
                    $(".alert-recommandation-success" + product_id).html('PRODUIT RECOMMANDE !');
                    setTimeout(function() {
                        $(".alert-recommandation-success" + product_id).hide();
                    }, 5000);
                } else if (response.status === 'error') {
                    if (response.message == 'Produit deja recommande !') {
                        $(".alert-recommandation-danger" + product_id).show();
                        $(".alert-recommandation-danger" + product_id).html('PRODUIT DEJA RECOMMANDE !');
                        setTimeout(function() {
                            $(".alert-recommandation-danger" + product_id).hide();
                        }, 5000);
                    } else {
                        window.location.href = "./../../gestion_epicerie/connexion/";  // Rediriger vers la page de connexion
                    }
                }
            },
           
        })
    }

});
});