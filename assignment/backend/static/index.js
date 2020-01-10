function signOut() {
	$.ajax({
	    type: "GET",
	    url: "/sign_out",
	    success: function (response) {
	    	window.location.replace("/login")	    	
    		// alert("Group is created successfully")
	    },
	    error: function (response) {
	        alert("some error occured")
	    }
	});		
}

