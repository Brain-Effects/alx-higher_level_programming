$(document).ready(function(){
  $('#btn_translate').click(function(){
    const language = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: language }, function(data){
      $('#hello').text(data.hello);
    });
  });
});
