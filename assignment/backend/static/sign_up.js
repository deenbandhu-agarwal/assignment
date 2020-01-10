function sign_up(data) {
	$.ajax({
	    type: "POST",
	    url: "/signup",
	    data: JSON.stringify(data),
	    dataType: "json",
	    success: function (response) {
	    	console.log(response);
        if(!response["status"]){
          alert("some error occured")
        }
        else{
	    	  window.location.replace("/login")
        }
	    },
	    error: function (response) {
	        alert("some error occured")
	    }
	});	
}

function formDataToObject(elForm) {
  if (!elForm instanceof Element) return;
  var fields = elForm.querySelectorAll('input, select, textarea'),
    o = {};
  for (var i=0, imax=fields.length; i<imax; ++i) {
    var field = fields[i],
      sKey = field.name || field.id;
    if (field.type==='button' || field.type==='image' || field.type==='submit' || !sKey) continue;
    switch (field.type) {
      case 'checkbox':
        o[sKey] = +field.checked;
        break;
      case 'radio':
        if (o[sKey]===undefined) o[sKey] = '';
        if (field.checked) o[sKey] = field.value;
        break;
      case 'select-multiple':
        var a = [];
        for (var j=0, jmax=field.options.length; j<jmax; ++j) {
          if (field.options[j].selected) a.push(field.options[j].value);
        }
        o[sKey] = a;
        break;
      default:
        o[sKey] = field.value;
    }
  }
  // alert('Form data:\n\n' + JSON.stringify(o, null, 2));
  return o;
}


$(document).ready(function(){
	// alert("hello world");
	$( "#sign_up" ).submit(function( event ) {
		var data = formDataToObject(this)
		sign_up(data);
		event.preventDefault();
	});	
});