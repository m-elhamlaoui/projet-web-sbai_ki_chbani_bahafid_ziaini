$(document).ready(function () {
    setInterval(function () {
        if (!$("#recherche").val()) {
            $.ajax({
                url: "./../utilisateurs_en_ligne/",  
                type: "POST",
                success: function (data) {
                    $("#rechercheContact").html(data);
                }
            });
        } else {
            $("#recherche").on("keyup", function () {
                let recherche = $(this).val();
                $.ajax({
                    url: "./../recherche_utilisateurs/", 
                    type: "POST",
                    data: { recherche: recherche },
                    success: function (data) {
                        $("#rechercheContact").html(data);
                    }
                });
            });
        }
    }, 500);
});