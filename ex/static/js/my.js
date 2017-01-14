$(document).ready(function(){
    var date = new Date();
    $('#id_event_date').datepicker({
        dateFormat: "dd.mm.yy",
        minDate: new Date('01.01.2016'),
        maxDate: new Date(date),
    });
});

/*
$(document).ready(function (){
    $('.btn').click(function(){
        var catid;
        catid = $(this).attr("data-catid");
        var uniq_id = ".axaj_"+catid;
        $.get('/like_post/', {post_id: catid}, function(data){
            $(".ajax_3").html(data);
        });
    });
});
*/

function getAjax(divdett,pageload) {
    $(function(){$(divdett).load(pageload).show()
    ;})
    ;}

$(document).ready(function () {
    $('.dislike').click(function () {
        $(this).toggleClass('dislike like');
    });
});


$(document).ready(function () {
    $('.like').click(function () {
        $(this).toggleClass('like dislike');
    });
})

