const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function mergeSort(array) {
    if (array.length === 1) {
        return array
    }
    // Split Array in into right and left
    const length = array.length;
    const middle = Math.floor(length / 2);
    const left = array.slice(0, middle);
    const right = array.slice(middle);
    // console.log('left:', left);
    // console.log('right:', right);

    return merge(
        mergeSort(left),
        mergeSort(right)
    )
}

function merge(left, right) {
    const result = [];
    let leftIndex = 0;
    let rightIndex = 0;
    // console.log('left:', left);
    // console.log('right:', right);
    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            // console.log('left[leftIndex]:', left[leftIndex]);
            // console.log('right[rightIndex]:', right[rightIndex]);
            result.push(left[leftIndex]);
            leftIndex++;
        } else {
            // console.log('right[rightIndex]:', right[rightIndex]);
            // console.log('left[leftIndex]:', left[leftIndex]);
            result.push(right[rightIndex]);
            rightIndex++;
        }
    }
    // console.log(left, right);
    // console.log(leftIndex, rightIndex);
    return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
}


const answer = mergeSort(numbers);  // O(n log n)
console.log(answer);            // [ 0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283 ]