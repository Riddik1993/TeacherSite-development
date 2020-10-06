$(document).ready(function(){

    user_answers_date=$('#received_answers').text();
    user_answers=JSON.parse(user_answers_date);


    for (key in user_answers) {
        $('li[ans_id]').each(function(){
            if($(this).attr('ans_id')==key) {
                if(user_answers[key]=='Y') {
                    $(this).append('<span style="font-size:1.5em; color:green;"> ✔ </span> ');



                 }
                 else {
                      $(this).append('<span style="font-size:1.5em; color:red;"> X </span> ');

                 }



            }


        });



    }



});
