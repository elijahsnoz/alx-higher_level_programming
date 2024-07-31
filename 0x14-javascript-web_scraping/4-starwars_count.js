#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length < 3) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Define the character ID for "Wedge Antilles"
const wedgeAntillesId = 18;

// Make the GET request to the API
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
    const data = JSON.parse(body);
    const movies = data.results || [];
    const count = movies.filter(movie => movie.characters.some(character => character.includes(`/${wedgeAntillesId}/`))).length;
    console.log(count);
  } catch (parseError) {
    console.error('Error: Failed to parse response body:', parseError);
    process.exit(1);
  }
});
