#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length < 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API
const starWarsUri = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the GET request to the API
request(starWarsUri, function (err, res, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Error: Status code', res.statusCode);
    return;
  }

  try {
    const movie = JSON.parse(body);
    console.log(movie.title); // Print the title of the movie
  } catch (parseError) {
    console.error('Error: Failed to parse response body:', parseError);
  }
});
