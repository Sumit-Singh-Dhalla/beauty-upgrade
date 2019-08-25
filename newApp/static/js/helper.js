function getOffers() {
    $.ajax({
        type: "get",
        url: "/offers",
        data: {},
        contentType: "application/json; charset=utf-8",
        timeout: 600000,
        success: function (data) {
            $( ".modal-body" ).html(data);
            $( "#offer-modal" ).modal("show");
        },
        error: function (e) {

            console.log("ERROR : ", e);

        }
    });

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