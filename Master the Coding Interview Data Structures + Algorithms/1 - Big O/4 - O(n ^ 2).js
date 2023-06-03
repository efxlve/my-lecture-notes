//Log all pairs of array
const boxes = ['a', 'b', 'c', 'd', 'e'];

function logAllPairsOfArray(array) {
    for (let i = 0; i < array.length; i++) { // O(n)
        for (let j = 0; j < array.length; j++) { // O(n)
            console.log(array[i], array[j]); // O(1)
        }
    }
}

logAllPairsOfArray(boxes); // O(n * n) --> O(n^2) --> Quadratic Time
// Quadratic Time nedir?
// Quadratic Time, bir algoritmanın çalışma zamanının, inputun karesine doğru orantılı olarak artmasıdır.
// Örneğin, bir algoritma 10 elemanlı bir arrayde 100 adımda çalışıyorsa, 100 elemanlı bir arrayde 10000 adımda çalışır.
// Quadratic Time, Big O Notasyonunda O(n^2) ile gösterilir.
// Quadratic Time, bir algoritmanın çalışma zamanı, inputun karesine doğru orantılı olarak artar.