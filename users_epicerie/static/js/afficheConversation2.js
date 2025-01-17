$(document).ready(function () {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Vérifiez si le cookie commence par le nom recherché
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    const csrftoken = getCookie('csrftoken');  // Récupère le jeton CSRF

    setInterval(function () {
        let id_recepteur = $("#id_recepteur").val();
        $.ajax({
            type: "POST",
            url: "./../../affiche_conversation_admin/",
            headers: {
                "X-CSRFToken": csrftoken  // Ajoutez le jeton CSRF ici
            },
            data: { id_recepteur: id_recepteur },
            success: function (response) {
                $("#retourMessage").html(response);
            }
        });
    }, 500);
});