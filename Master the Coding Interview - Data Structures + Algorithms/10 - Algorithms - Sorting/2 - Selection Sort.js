const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function selectionSort(array) {
    const length = array.length;
    for (let i = 0; i < length; i++) { // O(n)
        // set current index as minimum
        let min = i; // O(1)
        let temp = array[i]; // O(1)
        for (let j = i + 1; j < length; j++) { // O(n)
            if (array[j] < array[min]) {
                // update minimum if current is lower that what we had previously
                min = j; // O(1)
            }
        }
        array[i] = array[min]; // O(1)
        array[min] = temp; // O(1)
    }
    return array;
}

selectionSort(numbers); // O(n^2)
console.log(numbers); // [ 0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283 ]