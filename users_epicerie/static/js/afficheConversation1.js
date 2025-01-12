$(document).ready(function () {
    setInterval(function () {
        let id_recepteur = $("#id_recepteur").val();
        $.ajax({
            type: "POST",
            url: "./../affiche_conversation_action/",
            data: { id_recepteur: id_recepteur },
            success: function (response) {
                $("#retourMessage").html(response);
            }
        });
    }, 500);
});