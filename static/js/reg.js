$(document).ready(function() {
    "use strict";
	
	// Options for Message
	//----------------------------------------------
  var options = {
	  'btn-loading': '<i class="fa fa-spinner fa-pulse"></i>',
	  'btn-success': '<i class="fa fa-check"></i>',
	  'btn-error': '<i class="fa fa-remove"></i>',
	  'msg-success': 'All Good! Redirecting...',
	  'msg-error': 'Wrong login credentials!',
  };






$("#register-form").validate({
    rules: {
    username: "required",
      password1: {
            required: true,
            minlength: 5
        },
         password2: {
            required: true,
            minlength: 5,
            equalTo: "#register-form [name=password1]"
        },
        email: {
        required: true,
            email: true
        },
        first_name:{
          required: true
        },
        last_name:{
          required: true
        },
        reg_agree: "required",
  },
    errorClass: "form-invalid",
    errorPlacement: function( label, element ) {
      if( element.attr( "type" ) === "checkbox" || element.attr( "type" ) === "radio" ) {
          element.parent().append( label ); // this would append the label after all your checkboxes/labels (so the error-label will be the last element in <div class="controls"> )
      }
          else {
          label.insertAfter( element ); // standard behaviour
      }
  }
});



  // Loading
  //----------------------------------------------
function remove_loading($form)
{
    $form.find('[type=submit]').removeClass('error success');
    $form.find('.login-form-main-message').removeClass('show error success').html('');
}

function form_loading($form)
{
  $form.find('[type=submit]').addClass('clicked').html(options['btn-loading']);
}

function form_success($form)
{
    $form.find('[type=submit]').addClass('success').html(options['btn-success']);
    $form.find('.login-form-main-message').addClass('show success').html(options['msg-success']);
}

function form_failed($form)
{
    $form.find('[type=submit]').addClass('error').html(options['btn-error']);
    $form.find('.login-form-main-message').addClass('show error').html(options['msg-error']);
}


  
})