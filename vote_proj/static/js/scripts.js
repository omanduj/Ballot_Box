$("form[name=signup_form]").submit(function(e){     //when form=X, on submit, do this

    var $form = $(this);
    var $error = $form.find(".error");  //checks for errors
    var data = $form.serialize();   //Used to allow info to be malliable

    $.ajax({
        url: "/user/signup", //this refers to url in flask layer to properly connect
        type: "POST",        //Type of operation
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);          //Used to show info on html inspect window
            window.location.href = "/dashboard/"    //redirects on success to dashboard endpoint
        },
        error: function(resp) {
            var txt = 'User with that email already exists';
            $('#response_add').html(txt);
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
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
            window.location.href = "/dashboard/"
        },
        error: function(resp) {
            console.log(resp);
            var txt = 'Invalid Credentials';
            $('#response_add2').html(txt);
            $error.text(resp.responseJSON.error).removeClass('error--hidden');
        }
    })
    e.preventDefault();
});

$("form[name=ballot_name]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/add_ballot",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
            window.location.href = "/ballot_items/"
        },
        error: function(resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass('error--hidden');
        }
    })
    e.preventDefault();
});

$("form[name=ballot_item]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/add_ballot_item", 
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
            var txt = resp['success'] + ' has been added successfuly'
            $('#response_add').html(txt);

        },
        error: function(resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass('error--hidden');       //if error, will show text that is found in return statement

        }
    })
    e.preventDefault();
});


$("form[name=vote]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/voting",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
        },
        error: function(resp) {
            console.log(resp);
        }
    })
    e.preventDefault();
});


$("form[name=delete]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/destroyImage",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
        },
        error: function(resp) {
            console.log(resp);
        }
    })
    e.preventDefault();
});

$("document").ready(function(){

    // $("#show").on("click", function(){
    //     $("#text_box").show();
    // });

    $("#hide").on("click", function(){
        $("#text_box").hide();
    });
});
