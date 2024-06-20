#!/usr/bin/node

// Import the dictionary from the required file
const dict = require('./101-data.js').dict;

// Initialize an empty dictionary for the new structure
let newDict = {};

// Iterate over each key in the imported dictionary
for (let key in dict) {
  // Get the occurrence value
  let value = dict[key];
  
  // Check if the value exists in the new dictionary
  if (!newDict[value]) {
    // If not, create an array with the current key
    newDict[value] = [key];
  } else {
    // If it exists, push the current key into the array
    newDict[value].push(key);
  }
}

// Print the new dictionary
console.log(newDict);
