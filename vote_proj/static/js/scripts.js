$("form[name=signup_form]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup", //this refers to url in flask layer to properly connect
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
            window.location.href = "/dashboard/"    //redirects on success to dashboard endpoint
        },
        error: function(resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass('error--hidden');       //if error, will show text that is found in return statement
                                                    //of signup class. So it will print out the error whose key is error
        }
    })
    e.preventDefault();
});


$("form[name=login_form]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login", //this refers to url in flask layer to properly connect
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
            window.location.href = "/dashboard/"    //redirects on success to dashboard endpoint
        },
        error: function(resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass('error--hidden');       //if error, will show text that is found in return statement
                                                    //of signup class. So it will print out the error whose key is error
        }
    })
    e.preventDefault();
});

$("form[name=ballot_name]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/add_ballot", //this refers to url in flask layer to properly connect
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
            window.location.href = "/ballot_items/"    //redirects on success to dashboard endpoint
        },
        error: function(resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass('error--hidden');       //if error, will show text that is found in return statement
                                                    //of signup class. So it will print out the error whose key is error
        }
    })
    e.preventDefault();
});

$("form[name=ballot_item]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/add_ballot_item", //this refers to url in flask layer that info will be sent to properly connect
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
            window.location.href = "/ballot_items/" //redirects on success to dashboard endpoint
        },
        error: function(resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass('error--hidden');       //if error, will show text that is found in return statement
                                                    //of signup class. So it will print out the error whose key is error
        }
    })
    e.preventDefault();
});


$("form[name=vote]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/voting", //this refers to url in flask layer that info will be sent to properly connect
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
        },
        error: function(resp) {
            console.log(resp);                                                    //of signup class. So it will print out the error whose key is error
        }
    })
    e.preventDefault();
});
