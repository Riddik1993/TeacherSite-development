let ctx = document.getElementById('testResChart');
console.log("hi");
data = {
    datasets: [{
        data: [10, 20, 30],
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