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
            document.getElementById('tite').innerHTML += data['resp']

            }
        })
    })
}

$(document).ready(function(){
    test();
})
