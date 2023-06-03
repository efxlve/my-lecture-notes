// LIFO - Last In First Out
// FILO - First In Last Out
class Stack {
    constructor() {
        this.array = [];
    }

    // Peek at the last element
    peek() {
        return this.array[this.array.length - 1];
    }

    // Add to the beginning
    push(val) {
        this.array.push(val);
        return this;
    }

    // Remove from the beginning
    pop() {
        this.array.pop();
        return this;
    }
}

const stack = new Stack();
stack.push("google"); // google
stack.push("udemy"); // udemy, google
stack.push("discord"); // discord, udemy, google
stack.peek(); // discord
stack.pop(); // udemy, google
stack.pop(); // google
stack.pop(); // null

