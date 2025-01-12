$(document).ready(function () {
    $('#action_menu_btn').click(function () {
        $('.action_menu').toggle();
    });

    $("#formMessage").on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: './../enregistrer_message/',
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData: false,
            success: function () {

            }

        });
        $("#retourMessage").animate({ scrollTop: $("#retourMessage")[0].scrollHeight }, 3000);
        $('#message').val("");

    });

});