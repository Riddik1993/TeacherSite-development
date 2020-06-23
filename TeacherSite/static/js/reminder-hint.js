
$(document).ready(function() {

$('.article_list > a > li').mousemove(function(e) {

                  var obj=document.getElementById('article-block');
                  var coords = obj.getBoundingClientRect();
                  var desc=$('.article_description',this).text();

                  if (desc!="") {
                  $('#hint').css({'left':e.clientX-coords.left+25,'top':e.clientY-coords.top+55,'background-color':'rgb(247, 225, 168)'});
                  $('#hint').show(200).text(desc);
                  }
                              }
                  ).mouseout(function() {
                                $('#hint').hide(200);

                  });


});
