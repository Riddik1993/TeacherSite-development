$(document).ready(function(){
  attempt_data=$('#attempts').text();
  var obj=JSON.parse(attempt_data);

  for (key in obj) {
    $('a[test_id]').each(function(){
        if($(this).attr("test_id")==key) {
            var text='Осталось попыток:&nbsp'+obj[key];
            $(this).after(function(){
                    return '<span class="atmp_counter" atmp="'+obj[key]+'"><i>&nbsp' +text+'</i></span>';
                    })

        }

    })
  };

 setTimeout(color,100);

});

function color() {
  $('.atmp_counter').each(function(){

    if ($(this).attr("atmp")==0) {
      $(this).css('color','red');
    }
    else {
      $(this).css('color','green');
    }


  });
}
