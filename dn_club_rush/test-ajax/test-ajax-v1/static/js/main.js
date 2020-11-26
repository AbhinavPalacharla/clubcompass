$(function() {
    $("#testing-ajax").on("click", function() {
        var info = {
            firstname: "abhinav",
            lastname: "palacharla",
            email: "abhinav.palacharla@gmail.com",
            sheet: "rocketry"
        }

        console.log("button press registered")

        $.ajax({
            type: "POST",
            url: "/add_to_interest",
            data: info
        });     
    });
});