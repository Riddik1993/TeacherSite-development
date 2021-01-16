$(document).ready(function () {
        
        /*ajax на обновление списка достижений*/
		$('.button').click(function () {
              let categ_id=$(this).attr('cat_id');
              $.getJSON('/articles/achievelist/',{cat_id:categ_id},function(data) {
                          $('#ach_block').empty();
                          for (i in data.achs) {
                          	  let ach_id=data.achs[i].id;
                              let ach_name=data.achs[i].name;
                              let ach_img=data.achs[i].img
                                                          
                              content=`
                              <div class="scheme_block" id='${ach_id}'>
                              		<div class="scheme_image"> \
                              			<img width=50%  src='${ach_img}'/> <br/> \
                              		</div> \
                              		<div class="sheme_title">${ach_name}</div> \
                              </div>`;
                              $('#ach_block').append(content);

                              
                            }
                          });
                
              });

		/* показ инфо по достижению на всплывающем окне*/
        $('.scheme_block').click(function(){
         	$('#achiev_modal').fadeIn();
        });

        $('.close_btn').click(function() {
          $('#achiev_modal').fadeOut();
        });



});



















