#!/usr/bin/node
const request = require('request');

// Prints the Star Wars episode's title of the matching number.
// @param {int} movieId
const movieId = process.argv[2];
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(movieId);

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
