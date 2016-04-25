var d = document.getElementById("book5");
if (d){
  d.className += " hidden-sm hidden-xs";
}

$('.carousel').carousel({
    interval: false
}); 


function upload_img(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#id_image').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
function upload_img2(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#id_image2').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
function upload_img1(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#id_image1').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
function upload_img3(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#id_image3').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
function upload_img4(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#id_image4').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
  //your code here

  $('.likes1').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes1').load(' #likebuttonheart1');
    });
});
  $('.likes2').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes2').load(' #likebuttonheart2');
    });
});
  $('.likes3').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes3').load(' #likebuttonheart3');
    });
});
  $('.likes4').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes4').load(' #likebuttonheart4');
    });
});
  $('.likes5').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes5').load(' #likebuttonheart5');
    });
});
  $('.likes6').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes6').load(' #likebuttonheart6');
    });
});
  $('.likes7').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes7').load(' #likebuttonheart7');
    });
});
  $('.likes8').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes8').load(' #likebuttonheart8');
    });
});
  $('.likes9').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes9').load(' #likebuttonheart9');
    });
});
  $('.likes10').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes10').load(' #likebuttonheart10');
    });
});
  $('.likes11').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes11').load(' #likebuttonheart11');
    });
});
  $('.likes12').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes12').load(' #likebuttonheart12');
    });
});
  $('.likes13').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes13').load(' #likebuttonheart13');
    });
});
  $('.likes14').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes14').load(' #likebuttonheart14');
    });
});
  $('.likes15').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes15').load(' #likebuttonheart15');
    });
});
  $('.likes16').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes16').load(' #likebuttonheart16');
    });
});
  $('.likes17').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes17').load(' #likebuttonheart17');
    });
});
  $('.likes18').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes18').load(' #likebuttonheart18');
    });
});
  $('.likes19').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes19').load(' #likebuttonheart19');
    });
});
  $('.likes20').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes20').load(' #likebuttonheart20');
    });
});
  $('.likes21').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes21').load(' #likebuttonheart21');
    });
});
  $('.likes22').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes22').load(' #likebuttonheart22');
    });
});
  $('.likes23').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes23').load(' #likebuttonheart23');
    });
});
  $('.likes24').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes24').load(' #likebuttonheart24');
    });
});
  $('.likes25').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes25').load(' #likebuttonheart25');
    });
});
  $('.likes26').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes26').load(' #likebuttonheart26');
    });
});
  $('.likes27').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes27').load(' #likebuttonheart27');
    });
});
  $('.likes28').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes28').load(' #likebuttonheart28');
    });
});
  $('.likes29').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likes29').load(' #likebuttonheart29');
    });
});


  
  $('.likesp1').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp1').load(' #likebuttonheartp1');
    });
});
  $('.likesp2').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp2').load(' #likebuttonheartp2');
    });
});
  $('.likesp3').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp3').load(' #likebuttonheartp3');
    });
});
  $('.likesp4').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp4').load(' #likebuttonheartp4');
    });
});
  $('.likesp5').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp5').load(' #likebuttonheartp5');
    });
});
  $('.likesp6').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp6').load(' #likebuttonheartp6');
    });
});
  $('.likesp7').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp7').load(' #likebuttonheartp7');
    });
});
  $('.likesp8').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp8').load(' #likebuttonheartp8');
    });
});
  $('.likesp9').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp9').load(' #likebuttonheartp9');
    });
});
  $('.likesp10').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp10').load(' #likebuttonheartp10');
    });
});
  $('.likesp11').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp11').load(' #likebuttonheartp11');
    });
});
  $('.likesp12').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp12').load(' #likebuttonheartp12');
    });
});
  $('.likesp13').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp13').load(' #likebuttonheartp13');
    });
});
  $('.likesp14').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp14').load(' #likebuttonheartp14');
    });
});
  $('.likesp15').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp15').load(' #likebuttonheartp15');
    });
});
  $('.likesp16').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp16').load(' #likebuttonheartp16');
    });
});
  $('.likesp17').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp17').load(' #likebuttonheartp17');
    });
});
  $('.likesp18').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp18').load(' #likebuttonheartp18');
    });
});
  $('.likesp19').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp19').load(' #likebuttonheartp19');
    });
});
  $('.likesp20').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp20').load(' #likebuttonheartp20');
    });
});
  $('.likesp21').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp21').load(' #likebuttonheartp21');
    });
});
  $('.likesp22').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp22').load(' #likebuttonheartp22');
    });
});
  $('.likesp23').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp23').load(' #likebuttonheartp23');
    });
});
  $('.likesp24').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp24').load(' #likebuttonheartp24');
    });
});
  $('.likesp25').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp25').load(' #likebuttonheartp25');
    });
});
  $('.likesp26').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp26').load(' #likebuttonheartp26');
    });
});
  $('.likesp27').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp27').load(' #likebuttonheartp27');
    });
});
  $('.likesp28').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp28').load(' #likebuttonheartp28');
    });
});
  $('.likesp29').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/books/like/', {slug: catid}, function(data){
               $('.likesp29').load(' #likebuttonheartp29');
    });
});