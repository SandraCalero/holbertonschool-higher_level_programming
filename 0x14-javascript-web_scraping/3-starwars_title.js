#!/usr/bin/node
// This script is printing the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');
const id = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + id;

request(endpoint, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body.body);
    console.log(movie.title);
  }
});
