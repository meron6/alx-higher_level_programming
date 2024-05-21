#!/usr/bin/node
const r = require('request');
class GetData {
  asyncReq (url) {
    const that = this;
    return new Promise((resolve, reject) => {
      r({ url: url, json: true }, function (error, response, body) {
        if (error) {
          console.log(error);
          reject(error);
        } else {
          that.body = body;
          resolve();
        }
      });
    });
  }

  async namesloop (url) {
    const that = this;
    await that.asyncReq('https://swapi.co/api/films/' + process.argv[2]);
    const characters = that.body.characters;

    for (const character of characters) {
      await that.asyncReq(character);
      console.log(that.body.name);
    }
  }
}
const data = new GetData();

data.namesloop('https://swapi.co/api/films/' + process.argv[2]);
