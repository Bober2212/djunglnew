function createTask(){
    $('#btn').click(function(){
        $.ajax($('#btn').data("url"), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#text').val(),
                'status': $('#status').val(),
                'deadline': $('#deadline').val()
            },
            'success': function(data){
                document.getElementById('btns').innerHTML += data;
            }
        })
    })
}

$(function(){
    $(document).click(function(event){
        var element = $(event.target);
        if (element.attr('class') == 'edit_button') {
            $.ajax(element.data('url'), {
                'type': 'POST',
                'async': true,
                'dataType': 'json',
                'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'id': element.attr('id')
                },
                'success': function(data){
                    document.getElementById(`task${element.attr('id')}`).innerHTML += data;
                }
            })
        }
    })
})

$(document).ready(function(){
    createTask();
})