$(document).ready(function (e) {

    $(".alert-payement-danger").hide();
    $(".alert-payement-success").hide();

    function load_cart_data() {
        $.ajax({
            url: "./../fetch_cart/",
            method: "POST",
            dataType: "json",
            success: function (data) {
                $('#cart_details').html(data.cart_details);
                $('.total_price').text(data.total_price);
                $('.badge').text(data.total_item);
            }
        });
    }

    //payement

    $("#payer").on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: './../passer_commande/',
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData: false,
            success: function (response) {
                if (response.status == "0") {
                    load_cart_data();
                    $(".alert-payement-success").show();
                    $(".alert-payement-success").html('VOTRE COMMANDE A ETE ENREGISTREE AVEC SUCCES A BIENTOT ! ');
                    setTimeout(function () { $(".alert-payement-success").hide(); }, 5000);
                }

                else if (response.status == "-1") {
                    window.location.href = "./../../gestion_epicerie/connexion/";
                }


                else {
                    $(".alert-payement-danger").show();
                    $(".alert-payement-danger").html(response.message);
                    setTimeout(function () { $(".alert-payement-danger").hide(); }, 5000);
                }

            }

        });
    });

})