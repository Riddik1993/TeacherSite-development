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
        $('#ach_block').on ('click','.scheme_block',function(event) {
                                                        $('#achiev_modal').fadeIn();
                                                        let target=event.currentTarget;
                                                                                                                                                                     
                                                        /*вставляем заголовок*/
                                                        let header_el=target.querySelector('.sheme_title');
                                                        $('#am_header h3').empty();
                                                        $('#am_header h3').html(header_el.innerHTML);

                                                        /*вставляем картинку*/
                                                        let image_el=target.querySelector('.scheme_image>img');
                                                        let image_src=image_el.getAttribute('src');
                                                        $('#ach_img>img').attr('src',image_src);
                                                        
                                                        /*отправляем запрос на сервер и вставляем получ.описание*/
                                                        let ach_id=target.getAttribute('id');
                                                        $.getJSON('/articles/ach_info/', {'ach_id':ach_id},function(data) {
                                                                    console.log(data);
                                                                    $('#am_desc').empty();
                                                                    $('#am_desc').append(data.desc);

                                                               });
                                                    });

        $('.close_btn').click(()=> $('#achiev_modal').fadeOut());




});



















