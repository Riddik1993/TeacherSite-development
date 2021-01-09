
/*получаем массив данных*/

function ready() {
  let disk_json=document.getElementById('disk_info');
  let perc_el=document.getElementById('perc');
  let disc_msg=document.getElementById('d_msg');

  let disk_info=JSON.parse(disk_json.innerHTML);
  let free_sp=disk_info.free_space.toFixed(2);
  let used_sp=disk_info.used_space.toFixed(2);

  //подставляем процент и подсвечиваем если критично
  perc_el.innerHTML=disk_info.percent;
  if (disk_info.percent>=80) {
    disc_msg.style.color = 'red';

  }



  let ctx = document.getElementById('pie_memory_used');
data = {
    datasets: [{
        data: [used_sp,free_sp],
        backgroundColor:['#faa0a0','#affaa0'],
        borderColor:['black','black']
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: [
        'Занятое место (Гб)',
        'Свободное место (Гб)'
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





