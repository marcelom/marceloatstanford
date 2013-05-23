$(document).ready(function(){
	
	// Show Stanford Search Box
	$("#javascript").show();
	
	// Header Stanford Search Box
	$('#header [name=q]').val('Search this site...');
	$('#header [name=q]').focus(function () {
	$('#header [name=q]').val('');
	});
	
	// Drawer Toggle Expand
	$("#menu_expand").click(function (){
		$("#nav ul ul").slideToggle("slow");
		$('#menu_expand').hide();
		$('#menu_hide').show();
	});
	
	// Drawer Toggle Hide
	$("#menu_hide").click(function () {
		$("#nav ul ul").slideToggle("slow");
		$('#menu_expand').show();
		$('#menu_hide').hide();
	});
	
	// Activate CeeBox
	$(".ceebox").ceebox();
	
	// Image Link
	$('a:has(img)').css('border', 'none');
	
});