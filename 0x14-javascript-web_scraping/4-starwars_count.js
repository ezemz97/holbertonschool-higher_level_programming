#!/usr/bin/node
const request = require('request');

// Prints the number of movies where the character “Wedge Antilles” is present.
// @param {string} starWarsUri: Star Wars API URL https://swapi-api.hbtn.io/api/films/
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const characterId = characters[j].split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }
  console.log(times);
});
