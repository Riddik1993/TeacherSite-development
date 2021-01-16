$(document).ready(function () {
        
        /*ajax на обновление списка достижений*/
		$('.button').click(function () {
              let categ_id=$(this).attr('cat_id');
              $.getJSON('/articles/achievelist/',{cat_id:categ_id},function(data) {
                          $('#ach_block').empty();
                          for (i in data.achs) {
                              let achiev=data.achs[i];
                              $('#ach_block').append(`<p>${achiev}</p>`);
                              
                            }
                          });
                
              });




});









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





