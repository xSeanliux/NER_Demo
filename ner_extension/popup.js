$(function(){

	$("#reset_button").click(function() {
		$("#keyword").val('')
		$("#tagged_text").text('');
		$("#legend").hide();
	});
    
    $('#keywordsubmit').click(function(){
		
		$("#tagged_text").text('Loading...');
		$("#keywordsubmit").prop('disabled', true);
		$("#reset_button").prop('disabled', true);
		

		var search_topic = $('#keyword').val();
				
		if (search_topic){
                chrome.runtime.sendMessage(
					{topic: search_topic},
					function(response) {
						result = response.farewell;	
						
						$("#tagged_text").html(result.summary);
						$("#legend").show();
					});
		}
			
		$("#keywordsubmit").prop('disabled', false);
		$("#reset_button").prop('disabled', false);
		$('#keyword').val('');
		
    });
});