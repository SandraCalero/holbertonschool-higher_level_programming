#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
const request = require('request');
const id = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + id;

request(endpoint, function (error, body) {
  if (error) {
    return error;
  }
  const characters = JSON.parse(body.body).characters;
  characters.map((character) => {
    request(character, (error, data, body) => {
      if (error) {
        return error;
      }
      console.log(JSON.parse(body).name);
    });
    return true;
  });
});
