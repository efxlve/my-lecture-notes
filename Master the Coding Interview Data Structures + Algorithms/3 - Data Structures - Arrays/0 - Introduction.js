const strings = ['a', 'b', 'c', 'd'];
// 4*4 = 16 bytes of storage

// Accessing an element in an array by index
strings[2]; // O(1)

// Pushing an element to the end of an array
strings.push('e'); // O(1)

// Poping an element from the end of an array
strings.pop(); // O(1)

// Unshifting an element to the beginning of an array
strings.unshift('x'); // O(n)

// Splicing an element into the middle of an array
strings.splice(2, 0, 'alien'); // O(n)