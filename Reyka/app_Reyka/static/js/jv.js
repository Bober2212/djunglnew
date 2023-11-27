function test(){
    $('#btn').click(function(){
        $.ajax('/text/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#inp').val()
            },
            'success': function(data){

            }
        })
    })
}

$(document).ready(function(){
    test();
})
