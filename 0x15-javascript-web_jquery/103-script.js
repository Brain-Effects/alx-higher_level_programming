$(document).ready(function(){
  function getTranslation() {
    const language = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: language }, function(data){
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(getTranslation);
  
  $('#language_code').keypress(function(e){
    if(e.which == 13) { // Enter key pressed
      getTranslation();
    }
  });
});
