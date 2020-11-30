$(function() {
    $("#signup_btn").click(function(event) {

        event.preventDefault();

        var info = {
            firstname: $("#firstname").val(),
            lastname: $("#lastname").val(),
            email: $("#email").val()
        }

        console.log("button press registered")

        $.ajax({
            type: "POST",
            url: "/save_user_to_cookies",
            data: info
        });     
    });
});