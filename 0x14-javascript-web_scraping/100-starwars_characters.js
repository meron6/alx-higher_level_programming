#!/usr/bin/node
const r = require('request');
const url = `https://swapi.co/api/films/${process.argv[2]}`;
r(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const characterslinks = film.characters;
    characterslinks.map(function (link, index) {
      return r(link, function (error2, response2, body2) {
        if (error2) {
          console.error(error2);
        } else {
          console.log(JSON.parse(body2).name);
        }
      });
    });
  }
});
