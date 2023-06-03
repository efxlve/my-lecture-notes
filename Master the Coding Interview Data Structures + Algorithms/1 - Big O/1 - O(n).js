const nemo = ['nemo'];
const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank'];
const large = new Array(100000).fill('nemo');

function findNemo(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!');
        }
    }
}

findNemo(large); // O(n) --> Linear Time

// Linear Time nedir?
// Linear Time, bir algoritmanın çalışma zamanının, inputun büyüklüğüne doğru orantılı olarak artmasıdır.
// Örneğin, bir algoritma 10 elemanlı bir arrayde 10 adımda çalışıyorsa, 100 elemanlı bir arrayde 100 adımda çalışır.
// Linear Time, Big O Notasyonunda O(n) ile gösterilir.
// Linear Time, en yaygın görülen zaman karmaşıklığıdır.
// Linear Time, bir algoritmanın çalışma zamanı, inputun büyüklüğüne doğru orantılı olarak artar.