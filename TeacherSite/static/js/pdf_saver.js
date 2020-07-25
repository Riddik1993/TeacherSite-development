$('document').ready(function(){
    $('#pdf_load').click(function() {
            var div_height=$('#for_pdf').height();
            var div_width=$('#for_pdf').width();


            html2canvas($("#for_pdf")[0]).then(function(canvas) {


            //задаем максимальную высоту страницы
            var a4_height=1000;
            var list_number=canvas.height/a4_height;



            var pdf = new jsPDF();
            //вставляем канвас на первую страницу
            var canvasCopy = document.createElement("canvas");
            var copyContext = canvasCopy.getContext("2d");
            canvasCopy.width=canvas.width
            canvasCopy.height=a4_height
            copyContext.drawImage(canvas, 0, 0, canvas.width, a4_height, 0, 0, canvas.width,a4_height);
            var imgCut=canvasCopy.toDataURL("image/png");

            pdf.addImage( imgCut, 'JPEG', 10, 10);


            //добавляем страницы после 1й
            var i=1;
            while (i<Math.ceil(list_number)) {
              pdf.addPage();


              var canvasCopy = document.createElement("canvas");
              var copyContext = canvasCopy.getContext("2d");
              canvasCopy.width=canvas.width
              canvasCopy.height=a4_height
              copyContext.drawImage(canvas, 0, i*a4_height, canvas.width, a4_height, 0, 0, canvas.width,a4_height);
              var imgCut=canvasCopy.toDataURL("image/png");
              pdf.addImage( imgCut, 'JPEG', 10, 10);
              pdf.addPage();
              i+=1;
            }

            //получаем данные для названия файла
            var u_name=$("#FIO").text();
            var test=$("#test_name").text();
            var pass_date=String($("#pass_date").text());
            var pass_date_cl=pass_date.slice(0,pass_date.length-6)

            //сохраняем результат в pdf
            pdf.save(pass_date_cl+u_name+test.slice(0,40)+".pdf");


              });




     });



});
