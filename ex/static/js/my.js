$(document).ready(function(){
    var date = new Date();
    $('#id_event_date').datepicker({
        dateFormat: "yy-mm-dd",
        minDate: new Date('2016-01-01  '),
        maxDate: new Date(date),
    });
});
