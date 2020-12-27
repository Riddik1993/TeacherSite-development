$(document).ready(function(){
  
   if (document.body.clientWidth<=650){
	   $('#authent_panel>div>a').removeClass('simple_href');
	   $('#authent_panel>div>a').addClass('button');
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
