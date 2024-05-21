#!/usr/bin/node
const r = require('request');
const url = process.argv[2];
r(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
