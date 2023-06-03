const boxes = [0, 1, 2, 3, 4, 5];

function logFirstTwoBoxes(boxes) {
    console.log(boxes[0]); // O(1)
    console.log(boxes[1]); // O(1)
}

logFirstTwoBoxes(boxes); // O(2) --> O(1) --> Constant Time

// Constant Time nedir?
// Constant Time, bir algoritmanın çalışma zamanının, inputun büyüklüğüne bağlı olarak değişmemesidir.
// Örneğin, bir algoritma 10 elemanlı bir arrayde 10 adımda çalışıyorsa, 100 elemanlı bir arrayde de 10 adımda çalışır.
// Constant Time, Big O Notasyonunda O(1) ile gösterilir.
// Constant Time, en iyi zaman karmaşıklığıdır.
// Constant Time, bir algoritmanın çalışma zamanı, inputun büyüklüğüne bağlı olarak değişmez.

// Exercise 1
// What is the Big O of the below function? (Hint, you may want to go line by line)
// Türkçe açıklaması: Aşağıdaki fonksiyonun Big O Notasyonu nedir? (İpucu: Satır satır gitmek isteyebilirsiniz)
function funChallenge(input) {
    let a = 10; // O(1)
    a = 50 + 3; // O(1)

    for (let i = 0; i < input.length; i++) { // O(n)
        anotherFunction(); // O(n)
        let stranger = true; // O(n)
        a++; // O(n)
    }
    return a; // O(1)
}

// O(3 + 4n)

// Exercise 2
// What is the Big O of the below function? (Hint, you may want to go line by line)
// Türkçe açıklaması: Aşağıdaki fonksiyonun Big O Notasyonu nedir? (İpucu: Satır satır gitmek isteyebilirsiniz)
function anotherFunChallenge(input) {
    let a = 5; // O(1)
    let b = 10; // O(1)
    let c = 50; // O(1)
    for (let i = 0; i < input; i++) { // O(n)
        let x = i + 1; // O(n)
        let y = i + 2; // O(n)
        let z = i + 3; // O(n)
    }
    for (let j = 0; j < input; j++) { // O(n)
        let p = j * 2; // O(n)
        let q = j * 2; // O(n)
    }
    let whoAmI = "I don't know"; // O(1)
}

// O(4 + 7n)


