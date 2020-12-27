$(document).ready(function(){
  
   if (document.body.clientWidth<=650){
	   $('#authent_panel>a').removeClass('simple_href');
	   $('#authent_panel>a').addClass('button');
    };

  $('#mobile_menu_button').click(function() {
      $('aside').css('display','block');

  });


  $('article, footer').click(function() {
    if (document.body.clientWidth<=650) {
        $('aside').css('display','none');
      }
  });


});
