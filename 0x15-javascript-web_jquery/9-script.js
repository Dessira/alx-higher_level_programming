$('document').ready(function() {
	$.get("https://fourtonfish.cotm/hellosalut/?lang=fr", function(data) {
	$("#hello").text(data.hello);
   });
});
