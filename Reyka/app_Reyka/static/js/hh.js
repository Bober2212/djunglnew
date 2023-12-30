function test(){
    $('#btn').click(function(){
    let form_data= new FormData()
    form_data.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val())
    form_data.append('name',$('#name').val())
    form_data.append('photo',document.getElementById('photo').files[0])
        $.ajax('/hh/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': form_data,
            'processData':false,
            'contentType':false,
            'success': function(data){
               document.getElementById('responce').innerHTML = '<h1>Hello</h1>';

            }
        })
    })
}
$(document).ready(function(){
    test();
})