$(document).ready(function() {

  var now=new Date();
  var now_month=now.getMonth()+1;
  var html_num=+$('#calendar').attr("data_month");

 $('td').css('background-color','rgb(242, 189, 198)');
 $('.noday').css('background-color','transparent')

 if (html_num==now_month) {
 $('.expired').parent().css('background-color','rgb(179, 179, 179)');
};
 $(".cal_ev_ex").parent().parent().css('background-color','rgb(143, 232, 135)');
 $(".cal_ev_ex").parent().css('background-color','rgb(143, 232, 135)');

 if (html_num==now_month) {
 $(".today_cal").parent().css('outline','6px solid red');
};

 var obj=document.getElementById('calendar');
 var coords = obj.getBoundingClientRect();








 $('td:not(.noday)').mousemove(function(e) {

                   $(this).css("opacity","0.7");

                   if($(this).find('div').hasClass('expired')==false) {
                          $('#hint').css({'left':e.clientX-coords.left+10,'top':e.clientY-coords.top+10,'background-color':'rgb(235, 155, 175)'});
                          $('#hint').show(200).text('Свободных мест нет');
                     }
                               }
                   ).mouseout(function() {
                                 $('#hint').hide();
                                 $(this).css("opacity","1");
                             }
                   );

 $('td').has('.expired').mousemove(function(e) {
                  $(this).css("opacity","0.7");

                        }).mouseout(function() {
                              $(this).css("opacity","1");
                             }
                   );



 $('td').has('.cal_ev_ex').mousemove(function(e) {
               $(this).css("opacity","0.7");
               var info=$(this).find('.cal_ev_ex').text()
               $('#hint').css({'left':e.clientX-coords.left+10,'top':e.clientY-coords.top+10,'background-color':'rgb(143, 232, 135)',
                  });
                   $('#hint').show().text(info);
                                                 }
                   ).mouseout(function() {
                       $('#hint').hide();
                       $(this).css("opacity","1");
                                             }
                                 );


                                 {
                                     $('#hint').hide();
                                   }

/*обработка кликов на дни*/
                                 $('td').click(function(){
                                  if  ($(this).find('div').hasClass('cal_ev_ex')==true) {
                                    var flag = false;
                                    var cleck_elem=$(this);
                                    timerID=setInterval(function () {

                                           flag ? $(cleck_elem).css("opacity","0.5"):$(cleck_elem).css("opacity","1");
                                           flag ? $('[name="lesson_date"]').css("opacity","0.5"):$('[name="lesson_date"]').css("opacity","1");
                                           flag = !flag;

                                       }, 100);
                                    $(this).css("opacity","1");

                                    setTimeout(StopTimer,700);


                                    var date=$(this).find('span').text();
                                    console.log(date)
                                    $('[name="lesson_date"]').val(value=date);
                                    $('[name="lesson_date"]').css({'outline':'2px solid green','background-color':'rgb(193, 252, 192)'});
                                  }
                                  else {
                                    alert('На эту дату записаться нельзя')
                                  }
                                   });

                                function StopTimer() {
                                  clearInterval(timerID);
                                }


/*меняем местами календарь и форму для мобильных устройств*/
if (document.body.clientWidth<=950) {
$('#calendar').insertBefore('.comments_form');

}
      });
