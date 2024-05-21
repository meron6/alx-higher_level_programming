#!/usr/bin/node
const r = require('request');
const url = `http://swapi.co/api/films/${process.argv[2]}/?format=json`;
r(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
