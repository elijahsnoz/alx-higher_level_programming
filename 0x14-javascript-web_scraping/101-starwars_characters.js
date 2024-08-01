#!/usr/bin/node

const request = require('request');

// Function to fetch data from a URL and return a Promise
function getDataFrom(url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, _res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

// Error handler function to log errors
function errHandler(err) {
  console.log(err);
}

// Function to fetch and print characters from a Star Wars movie
function printMovieCharacters(movieId) {
  const movieUri = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  getDataFrom(movieUri)
    .then(body => JSON.parse(body)) // Parse movie details
    .then(res => {
      const characters = res.characters;
      const promises = characters.map(characterUrl => getDataFrom(characterUrl)); // Create an array of Promises

      return Promise.all(promises); // Wait for all character requests to complete
    })
    .then(results => {
      results.forEach(result => {
        const character = JSON.parse(result);
        console.log(character.name); // Print each character's name
      });
    })
    .catch(errHandler); // Handle any errors
}

// Run the function with the provided movie ID
printMovieCharacters(process.argv[2]);

