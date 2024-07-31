#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length < 3) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the GET request to the API for the movie details
request(apiUrl, function (err, res, body) {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }

  if (res.statusCode !== 200) {
    console.error('Error: Status code', res.statusCode);
    process.exit(1);
  }

  try {
    const movie = JSON.parse(body);
    const characters = movie.characters || [];

    // Print the name of each character in the order they appear
    characters.forEach(characterUrl => {
      request(characterUrl, function (charErr, charRes, charBody) {
        if (charErr) {
          console.error('Error:', charErr);
          return;
        }

        if (charRes.statusCode !== 200) {
          console.error('Error: Status code', charRes.statusCode);
          return;
        }

        try {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } catch (parseError) {
          console.error('Error: Failed to parse character response body:', parseError);
        }
      });
    });
  } catch (parseError) {
    console.error('Error: Failed to parse movie response body:', parseError);
    process.exit(1);
  }
});

