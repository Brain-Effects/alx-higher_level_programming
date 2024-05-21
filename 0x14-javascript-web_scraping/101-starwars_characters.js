#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function getCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  for (const url of characterUrls) {
    const name = await getCharacterName(url);
    console.log(name);
  }
});
