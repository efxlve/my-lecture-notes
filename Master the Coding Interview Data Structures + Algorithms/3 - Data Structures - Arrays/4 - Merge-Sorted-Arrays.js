// [0, 3, 4, 4, 6, 30, 31]

// Solution 1
function mergeSortedArrays(array1, array2) {
    // Check input
    if (!array1 || !array2 || array1.length === 0 || array2.length === 0) {
        return 'Invalid input';
    }

    // Merge arrays
    const mergedArray = [];
    let array1Item = array1[0];
    let array2Item = array2[0];
    let i = 1;
    let j = 1;

    while (array1Item || array2Item) {
        if (!array2Item || array1Item < array2Item) {
            mergedArray.push(array1Item);
            array1Item = array1[i];
            i++;
        } else {
            mergedArray.push(array2Item);
            array2Item = array2[j];
            j++;
        }
    }

    return mergedArray;
}

mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]);