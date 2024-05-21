#!/usr/bin/node
const fs = require('fs');

const content = process.argv[3];
const file = process.argv[2];

fs.writeFile(file, content, { encoding: 'utf-8', flag: 'a' }, err => {
  if (err) {
    console.log(err);
  } else {

  }
});
