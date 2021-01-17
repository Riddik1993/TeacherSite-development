
//Анимация схем (отображение посередине)
$(document).ready(function(){
      $("img").on('click', function() {

          if(!$(this).attr('class').match(/full/)) {
                  var nec_src=$(this).attr('src');
                  $(".fadeBlock>.content>img").attr('src',nec_src);
                  $(".fadeBlock").fadeIn();
          }
          else {
            $(".fadeBlock>.content>img").attr('src',"");
            $(".fadeBlock").fadeOut();
          };

      });
 });
