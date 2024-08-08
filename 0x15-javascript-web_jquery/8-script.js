$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const films = data.results;
    films.forEach(function (film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  });
});
