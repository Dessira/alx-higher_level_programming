 $.get
	(
	   "https://swapi-api.hbtn.io/api/films/?format=json", 
	  function(data) {
		  let val = data.results
              $.each(val, function(index, val)
		{
		    $("#list_movies").append($("<li>" + val.title + "</li>"));
		});
        });
