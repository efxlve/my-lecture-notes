const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function bubbleSort(array) {
    const length = array.length;
    for (let i = 0; i < length; i++) { // O(n)
        for (let j = 0; j < length; j++) { // O(n)
            if (array[j] > array[j + 1]) {
                // Swap numbers
                let temp = array[j]; // O(1)
                array[j] = array[j + 1]; // O(1)
                array[j + 1] = temp; // O(1)
            }
        }
    }
}

bubbleSort(numbers); // O(n^2)
console.log(numbers); // [ 0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283 ]