$(document).ready(function () {
  var i;
  i=2;

  intervalID4=setTimeout(function(e) {
     $('#imgarea').fadeOut(500);
  },4000);

  intervalID=setInterval(function(e) {


    if (i==1) {
    $('#imgarea').fadeIn(500);
    $('#imgarea').html($('#imgtoPaste1').html());
    i+=1;
              }
    else if (i==2) {
        $('#imgarea').fadeIn(500);
      $('#imgarea').html($('#imgtoPaste2').html());
      i+=1;
    }
    else if (i==3) {
        $('#imgarea').fadeIn(500);
      $('#imgarea').html($('#imgtoPaste3').html());
      i+=1;
    }
    else if (i==4) {
        $('#imgarea').fadeIn(500);
      $('#imgarea').html($('#imgtoPaste4').html());
      i+=1;
    }
    else  if (i==5) {
      $('#imgarea').fadeIn(500);
      $('#imgarea').html($('#imgtoPaste5').html());
      i-=4;
    }

  intervalID2=setTimeout(function(e) {
     $('#imgarea').fadeOut(500);
  },4000);

},5000);


});
