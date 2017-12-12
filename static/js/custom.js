$(function(){
    $('#btnSignUp').click(function(){
        $.ajax({
           url: '/createUser',
           data: $('form').serialize(),
           type: 'POST',
           success: function(response){
              response = jQuery.parseJSON(response);
              if (response.flag == 0) {
                  $('#msg').removeClass('success');
                  $('#msg').addClass('error');
              } else {
                  $('#msg').removeClass('error');
                  $('#msg').addClass('success');
              }
              $('#msg').html(response.html)
           },
           error: function(error){
               return false;
           }

        });
    });
})
