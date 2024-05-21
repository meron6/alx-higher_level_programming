#!/usr/bin/node
const r = require('request');
const url = process.argv[2];
r(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const uniqueIds = new Set();
    const myObj = {};

    for (const todo of todos) {
      uniqueIds.add(todo.userId);
    }

    for (const id of uniqueIds) {
      let counter = 0;
      myObj[id] = counter;
      for (const todo of todos) {
        if (todo.userId === id && todo.completed) {
          counter++;
          myObj[id] = counter;
        }
      }
    }
    console.log(myObj);
  }
});
