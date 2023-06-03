const letters = ['a', 'd', 'z', 'e', 'r', 'b'];
const basket = [2, 65, 34, 2, 1, 7, 8];
const spanish = ['único', 'árbol', 'cosas', 'fútbol'];

letters.sort(); //sorts in alphabetical order // ["a", "b", "d", "e", "r", "z"]

basket.sort(); //sorts in ascending order // [1, 2, 2, 34, 65, 7, 8]
basket.sort(function (a, b) {
    return a - b; //sorts in ascending order // [1, 2, 2, 7, 8, 34, 65]
});

spanish.sort(); //sorts in alphabetical order // ["cosas", "fútbol", "árbol", "único"]
spanish.sort(function (a, b) {
    return a.localeCompare(b); 
}); // ["árbol", "cosas", "fútbol", "único"]

console.log('2'.charCodeAt(0)) // 50
console.log('65'.charCodeAt(0)) // 54
console.log('34'.charCodeAt(0)) // 51
console.log('7'.charCodeAt(0)) // 55