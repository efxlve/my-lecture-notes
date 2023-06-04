//Create a function that reverses a string:
// 'Hi My name is Andrei' should be:
// 'ierdnA si eman yM iH'

//Solution 1
function reverse(str) {
    //check input
    if (!str || str.length < 2 || typeof str !== 'string') {
        return 'hmm that is not good';
    }

    const backwards = [];
    const totalItems = str.length - 1;
    for (let i = totalItems; i >= 0; i--) {
        backwards.push(str[i]);
    }

    return backwards.join('');
}

reverse('Hi My name is Andrei');

//Solution 2
function reverse2(str) {
    return str.split('').reverse().join('');
}

reverse2('Hi My name is Andrei');

//Solution 3
const reverse3 = str => str.split('').reverse().join('');

reverse3('Hi My name is Andrei');

//Solution 4
const reverse4 = str => [...str].reverse().join('');

reverse4('Hi My name is Andrei');