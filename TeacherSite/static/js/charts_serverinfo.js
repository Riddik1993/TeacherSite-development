
/*получаем массив данных*/

function ready() {
  
  let ctx = document.getElementById('pie_memory_used');
data = {
    datasets: [{
        data: [8,10],
        backgroundColor:['#faa0a0','#affaa0'],
        borderColor:['black','black']
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: [
        'Занятое место',
        'Свободное место'
    ]
};

options ={
    animation: {
        animateScale:true
    },
   
}

var myPieChart = new Chart(ctx, {
    type: 'pie',
    data: data,
    options:options
    
});


}


document.addEventListener("DOMContentLoaded", ready);






/*
}
	
	
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


let data_dia=$('#dia_data').html();
let json_dia=$.parseJSON(data_dia);
*/
