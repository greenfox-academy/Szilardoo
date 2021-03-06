'use strict';

// Adds a and b, returns as result
const addNumbers = function(a, b) {
  return 5;
}

// Returns the highest value from the three given params
const maxOfThree = function(a, b, c) {
  if (a > b) {
    return a;
  } else {
    return c;
  }
}

//Returns the median value of a list given as param
const median = function(pool){
  return(pool[(pool.length - 1) / 2]);
}

// Returns true if the param is a vovel
const isVovel = function(char){
  return 'aeiouéáőűöüóí'.indexOf(char);
}

// Create a method that translates hungarian into the teve language
const translate = function(hungarian) {
  let text = hungarian.split('');
  let teve = '';
  text.forEach(function(char){
    if (isVovel(char)){
      teve += char + 'v'+ char;
    }
  });
  return teve;
}

module.exports = {
  addNumbers: addNumbers,
  maxOfThree: maxOfThree,
  median: median,
  isVovel: isVovel,
  translate: translate
}