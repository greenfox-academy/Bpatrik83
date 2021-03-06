'use strict';
// - Create an array variable named `ag` with the following content: `['Gin', 'Whiskey', 'Wine', 'Beer']`
// - Double all the strings in the array, use a built in array method instead of a loop
// It should print: ['GinGin', 'WhiskeyWhiskey', 'WineWine', 'BeerBeer']`

let ag = ['Gin', 'Whiskey', 'Wine', 'Beer'];

function itemDoubling(array) {
    return array.map(item => item + item);
}

console.log(itemDoubling(ag));
