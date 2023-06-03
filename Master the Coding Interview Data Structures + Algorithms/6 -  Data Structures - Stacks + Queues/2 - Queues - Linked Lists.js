class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// FIFO
class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    // Peek at the first element
    peek() {
        return this.first;
    }

    // Add to the end
    enqueue(value) {
        const newNode = new Node(value);

        if (!this.first) {
            this.first = newNode;
            this.last = this.first;
        } else {
            const temp = this.last;
            this.last = newNode;
            temp.next = this.last;
        }

        ++this.size;
        return this;
    }

    // Remove from the beginning
    dequeue() {
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

const queue = new Queue();
queue.enqueue("google"); // google
queue.enqueue("udemy"); // google, udemy
queue.enqueue("discord"); // google, udemy, discord
queue.enqueue("facebook"); // google, udemy, discord, facebook
queue.peek(); // google
queue.dequeue(); // udemy, discord, facebook
queue.dequeue(); // discord, facebook
queue.dequeue(); // facebook
queue.dequeue(); // null