$(document).ready(function () {
    $('#action_menu_btn').click(function () {
        $('.action_menu').toggle();
    });

    $("#formMessage").on('submit', function (e) {
        e.preventDefault();

        // Récupérer le jeton CSRF
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');

        // Envoyer les données via AJAX
        $.ajax({
            type: 'POST',
            url: './../../message_action_admin/', 
            headers: {
                "X-CSRFToken": csrftoken  // Inclure le jeton CSRF
            },
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData: false,
            success: function (response) {
                if (response.success) {
                    console.log(response.success);
                    // Faire défiler vers le bas après l'envoi du message
                    $("#retourMessage").animate({ scrollTop: $("#retourMessage")[0].scrollHeight }, 3000);
                    // Effacer le champ de message
                    $('#message').val("");
                } else if (response.error) {
                    console.error(response.error);
                }
            },
            error: function (xhr, status, error) {
                console.error("Erreur AJAX :", error);
            }
        });
    });
});