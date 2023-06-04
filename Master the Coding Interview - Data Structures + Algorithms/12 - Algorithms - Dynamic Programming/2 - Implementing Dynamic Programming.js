//0 ,1 ,1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...

let calculations = 0;

function fibonacciRecursive(n) { // O(2^n)
    //calculations++;
    if (n < 2) {
        return n;
    }
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

function fibonacciMaster() { // O(n)
    let cache = {};
    return function fib(n) {
        calculations++;
        if (n in cache) {
            return cache[n];
        } else {
            if (n < 2) {
                return n;
            } else {
                cache[n] = fib(n - 1) + fib(n - 2);
                return cache[n];
            }
        }
    };
}

function fibonacciMaster2(n) { // O(n)
    let answer = [0, 1];
    for (let i = 2; i <= n; i++) {
        answer.push(answer[i - 2] + answer[i - 1]);
    }
    return answer.pop();
}

const fasterFib = fibonacciMaster();

console.log("Slow", fibonacciRecursive(10));
console.log("DP", fasterFib(10));
console.log("DP2", fibonacciMaster2(10));
console.log("We did " + calculations + " calculations");

