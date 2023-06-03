class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

// LIFO - Last In First Out
// FILO - First In Last Out
class Stack {
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    // Peek at the last element
    peek() {
        return this.first;
    }

    // Add to the beginning
    push(val) {
        const newNode = new Node(val);

        if (!this.first) {
            this.first = newNode;
            this.last = newNode;
        } else {
            const temp = this.first;

            this.first = newNode;
            this.first.next = temp;
        }

        ++this.size;
        return this;
    }

    // Remove from the beginning
    pop() {
        if (!this.first) return null;

        const temp = this.first;

        if (this.first === this.last) {
            this.last = null;
        }

        this.first = this.first.next;
        this.size--;

        return temp.val;
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

