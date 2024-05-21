#!/usr/bin/node
const r = require('request');
const url = process.argv[2];
r(url, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const jsonbody = JSON.parse(body);
    console.log(parseInt(jsonbody.results.map(function (film, index) {
      return film.characters.filter(function (character, index) {
        return character === 'https://swapi.co/api/people/18/';
      });
    }).filter(function (movie) {
      return movie.length > 0;
    }).length));
  }
});
