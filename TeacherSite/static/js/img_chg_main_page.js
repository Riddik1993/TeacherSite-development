$(document).ready(function () {


  var list_imgs=$('.ind_new');
  img_qty=list_imgs.length;

  var i=0
  $('#area_for_new').html($(".ind_new:eq("+i+")").html());

  setInterval(function() {

              if (i<=img_qty) {
                $('#area_for_new').html($(".ind_new:eq("+i+")").html());
                i+=1;



              }
              else {
                i=0;
                $('#area_for_new').html($(".ind_new:eq("+i+")").html());
                i+=1;
                }
            },

               3000);









});
