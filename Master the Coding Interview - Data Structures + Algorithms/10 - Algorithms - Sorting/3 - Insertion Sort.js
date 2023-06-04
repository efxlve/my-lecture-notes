const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function insertionSort(array) {
    const length = array.length;
    for (let i = 0; i < length; i++) { // O(n)
        if (array[i] < array[0]) {
            // move number to the first position
            array.unshift(array.splice(i,1)[0]); // O(n)
        }
        else {
            // find where number should go
            for (let j = 1; j < i; j++) { // O(n)
                if (array[i] > array[j-1] && array[i] < array[j]) {
                    // move number to the right spot
                    array.splice(j,0,array.splice(i,1)[0]); // O(n)
                }
            }
        }
    }
}

insertionSort(numbers); // O(n^2)
console.log(numbers);   // [ 0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283 ]