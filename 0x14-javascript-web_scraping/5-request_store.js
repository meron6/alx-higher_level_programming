#!/usr/bin/node
const r = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
r
  .get(url, 'utf-8')
  .on('error', function (error) {
    console.log(error);
  })
  .on('response', function (response) {
  })
  .on('data', function (data) {
  })
  .pipe(fs.createWriteStream(file));
