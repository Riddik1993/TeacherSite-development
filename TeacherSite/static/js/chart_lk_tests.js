
/*получаем массив данных*/
$(document).ready(function(){



     
/*меняем местами диаграмму и список тестов для мобильных устройств*/
if (document.body.clientWidth<=950) {
    $('#lk_test_results').insertBefore('#diagram_lk_tests');
    $('#lk_test_results').css("margin","15px 0px");
    $('.reminders').insertBefore('#diagram_lk_tests');
    $('.reminders').css("margin","10px 0px");
}
	/*Раскрашиваем результаты тестов*/
	
    var array = $(".res");
    let array_bad;
        for(var i=0;i<array.length;i++){
            var result=array.eq(i).text();
            var result2=result.replace(',','.');

            if (result2<30) {
              array.eq(i).css('background-color','red');
            }
            if (result2>75) {
              array.eq(i).css('background-color','rgb(87, 250, 72)');
            }
            if (result2>=30&&result2<50) {
              array.eq(i).css('background-color','rgb(146, 187, 247)');
            }
            if (result2>=50&&result2<70) {
              array.eq(i).css('background-color','yellow');
            }
        }

/*Парсим json для получения данных для диаграммы и строим её*/
let data_dia=$('#dia_data').html();
let json_dia=$.parseJSON(data_dia);

let ctx = document.getElementById('testResChart');
data = {
    datasets: [{
        data: [json_dia.b,json_dia.g, json_dia.e],
        backgroundColor:['#faa0a0','#f2f7ad','#affaa0'],
        borderColor:['black','black','black']
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: [
        'Плохо',
        'Средне',
        'Отлично'
    ]
};

options ={
	animation: {
		animateScale:true
	},
	onclick:()=>alert("hi")

}

var myPieChart = new Chart(ctx, {
    type: 'pie',
    data: data,
    options:options
    
});

});