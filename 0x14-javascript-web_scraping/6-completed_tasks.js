#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length < 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

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
    const todos = JSON.parse(body);
    const completedTasks = {};

    // Count completed tasks by user ID
    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });

    // Print users with completed tasks
    console.log(completedTasks);
  } catch (parseError) {
    console.error('Error: Failed to parse response body:', parseError);
    process.exit(1);
  }
});
