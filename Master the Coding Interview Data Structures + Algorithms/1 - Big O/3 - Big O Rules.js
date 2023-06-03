//Rule 1: Worst Case
// Türkçe açıklaması: En kötü durum

const nemo = ['nemo'];
const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank'];
const large = new Array(100000).fill('nemo');

function findNemo(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!');
            break; // Rule 1: Worst Case
        }
    }
}

findNemo(large); // O(n) --> Linear Time

// Rule 2: Remove Constants
// Türkçe açıklaması: Sabitleri kaldır

function printFirstItemThenFirstHalfThenSayHi100Times(items) {
    console.log(items[0]); // O(1)

    var middleIndex = Math.floor(items.length / 2); // O(1)
    var index = 0; // O(1)

    while (index < middleIndex) { // O(n/2)
        console.log(items[index]); // O(n/2)
        index++; // O(n/2)
    }

    for (var i = 0; i < 100; i++) { // O(100)
        console.log('hi'); // O(100)
    }
}

// Big O: O(1 + 1 + 1 + n/2 + n/2 + n/2 + 100 + 100)
// Big O: O(3 + n/2 + n/2 + n/2 + 100 + 100)
// Big O: O(3 + 3n/2 + 100 + 100)
// Big O: O(200 + 3n/2)
// Big O: O(3n/2)
// Big O: O(n/2)
// Big O: O(n)
// Drop the constants --> O(n)
// Sabitleri kaldır --> O(n)

// Rule 3: Different terms for inputs
// Türkçe açıklaması: Farklı terimler için girdiler

function compressBoxesTwice(boxes, boxes2) {
    boxes.forEach(function (boxes) {
        console.log(boxes);
    });

    boxes2.forEach(function (boxes) {
        console.log(boxes);
    });
}

// Big O: O(a + b)

// Rule 4: Drop Non Dominants
// Türkçe açıklaması: Baskın olmayanları bırak

function printAllNumbersThenAllPairSums(numbers) {
    console.log('these are the numbers:');
    numbers.forEach(function (number) {
        console.log(number);
    });

    console.log('and these are their sums:');
    numbers.forEach(function (firstNumber) {
        numbers.forEach(function (secondNumber) {
            console.log(firstNumber + secondNumber);
        });
    });
}

printAllNumbersThenAllPairSums([1, 2, 3, 4, 5]);

// Big O: O(n + n^2)

// Big O Cheat Sheet:
// https://www.bigocheatsheet.com/

