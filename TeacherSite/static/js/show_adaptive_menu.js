$(document).ready(function(){
  $('#mobile_menu_button').click(function() {
      $('aside').css('display','block');

  });


  $('article, footer').click(function() {
    if (document.body.clientWidth<=650) {
        $('aside').css('display','none');
      }
  });


});
