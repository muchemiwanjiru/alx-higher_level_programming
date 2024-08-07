$('document').ready(function () {
    const URL = 'https://www.fourtonfish.com/hellosalut/?';
    $('#btn_translate').click(function () {
      $.get(URL + $.param({ lang: $('#language_code').val() }), function (data) {
        $('#hello').html(data.hello);
      });
    });
  });
