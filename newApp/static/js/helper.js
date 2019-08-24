function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function reservation(){
    form = document.forms['reservation-form'];
    payload = {
        "name": form.name.value,
        "email": form.email.value,
        "phone": form.phone.value,
        "date": form.date.value,
        "time": form.time.value,
        "description": form.description.value,
    }
    $.ajax({
        type: "POST",
        url: "/reserve/",
        data: JSON.stringify(payload),
        contentType: "application/json; charset=utf-8",
        timeout: 600000,
        success: function (data) {
            form.reset();
            alert("Reservation Request has been sent");
        },
        error: function (e) {

            console.log("ERROR : ", e);

        }
    });

}