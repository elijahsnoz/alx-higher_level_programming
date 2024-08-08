$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error fetching translation');
    });
  }

  // Handle button click
  $('#btn_translate').click(fetchTranslation);

  // Handle Enter key press in input field
  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // 13 is the Enter key
      fetchTranslation();
    }
  });
});

