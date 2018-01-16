$(document).ready( function() {

});

function preAjax() {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
}

function open_bug_form () {
  bootbox.dialog({
    message:"<form id='bugForm' action='/sendbug' method='post'>"+
      "<b>Subject : </b><input class='col-md-12' type='text' name='subject'><br/>"+
      "<b>Email : </b><input class='col-md-12' type='email' name='email'><br/>"+
      "<b>Content : </b><textarea class='col-md-12' rows='10' name='content'></textarea>"+
      "</form>",
    title:"Report Bug",
    onEscape: true,
    backdrop: true,
    buttons: {
      cancel: {
	label: 'Cancel',
	className: 'btn-danger'
      },
      confirm: {
	label: 'Send',
	className: 'btn-default',
	callback: function () {
	  preAjax();
	  $.ajax({
	    type:'POST',
	    url:'/sendbug',
	    data: $('#bugForm').serializeArray().reduce(function(obj, item) {
	          obj[item.name] = item.value;
		      return obj;
	    }, {}),
	  })
	}
      }
    }
  })
} 
