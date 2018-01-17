var timeline;
var timeline_data;
var timeline_data_changed;
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


//---------- Here is function for timeline -----------
// Jump up timeline event edit dialog

// Called when the Visualization API is loaded.
function drawVisualization() {
  var e = document.getElementById('mytimeline');
  var action = e.getAttribute("data-action");
  var ind = e.getAttribute("data-value");
  timeline_data = [];
  timeline_data_changed = [];
  function turnToDate(date) {
    var lst = date.split("-");
    return new Date(lst[0],lst[1]-1,lst[2]);
  };

  var options = {
    "width":  "100%",
    "height": "auto",
    "editable": true,
    "style": "dot", // optional
    "scale": links.Timeline.StepDate.SCALE.YEAR,
    "step": 1,
    "zoomMax": 1000 * 60 * 60 * 24 * 31 * 12 * 20,
    "zoomMin": 1000 * 60 * 60 * 24 * 31 * 12 * 5,
    "start" : new Date(2011,0,1),
    "end" : new Date(2019,0,1),
  };
  timeline = new links.Timeline(e);

  function onEdit() {
    var sel = timeline.getSelection();
    if (sel.length) {
      if (sel[0].row != undefined) {
        var row = sel[0].row;
        var eventSelected = timeline_data[row];
	window.location.href='http://localhost:8000/enzymes/'+eventSelected.enzyme;
      }
    }
  };
  links.events.addListener(timeline,'edit',onEdit);
  $.ajax({
      type:"GET",
      url:"http://localhost:8000/timeline/data",
      data:{},
      success: function(data) {
        var events = data['events'];
        var row;
	var ymax=0;
        for (var i = 0; i<events.length;i++) {
          var event = {};
          event['id'] = events[i].pk;
          event['start'] = new Date(events[i].fields.year,0,1);
          event['content'] = "EC "+events[i].fields.enzyme + " " + events[i].fields.content;
          event['enzyme'] = events[i].fields.enzyme;
          timeline_data.push(event);
          timeline.draw(timeline_data, options);
	  if (event['start'] > ymax) {
	    row = i;
	    ymax=event['start'];
	  }
	}
        timeline.setSelection([{row:row}]);
      }
  });
}
