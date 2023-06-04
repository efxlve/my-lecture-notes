//0 ,1 ,1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...

// O(2^n)
function fibonacciRecursive(n) {
    if (n < 2) {
        return n;
    }
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

console.log(fibonacciRecursive(6));