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


/*работа со всплывающим окном по достижениям*/


function showAchList(category_id) {
 $.getJSON('/articles/achievements',{cat_id:category_id},function(data) {
                          $('#am_content').empty();
                          for (i in data.achs) {
                              let achiev=data.achs[i];
                              $('#am_content').append(`<p>${achiev}</p>`);
                              
                            }
                          });
}

$('#ach_show').click(function() {
    $('#about_modal').fadeIn();
    $.getJSON('/articles/achievements',{cat_id:'N'},function(data) {
            $('#am_header').empty();

            for (cat in data) {
              
              let cat_name=data[cat];
              let id=cat;
              $('#am_header').append(`<a class="button" style="margin:5px;" cat_id=${id}>${cat_name}</a>`);
              showAchList(1);
            }
      

                /*обработка нажатий на кнопку на всплывающем окне*/
            $('.button').click(function () {
              let categ_id=$(this).attr('cat_id');
              showAchList(categ_id);
                
              });

        });

           
    });





$('.close_btn').click(function() {
    $('#about_modal').fadeOut();
});








});
