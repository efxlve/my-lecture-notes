class DoublyLinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null,
            prev: null,
        };
        this.tail = this.head;
        // this.length = 1;
    }
    append(value) {
        const newNode = {
            value: value,
            next: null,
            prev: null,
        };
        newNode.prev = this.tail;
        // this.length++;
        this.tail.next = newNode;
        this.tail = newNode;
        return this;
    }
    prepend(value) {
        const newNode = {
            value: value,
            next: null,
            prev: null,
        };
        // this.length++;
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
        return this;
    }
    printList() {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }
    insert(index, value) {
        // Check for proper parameters;
        if (index >= this.length) {
            console.log('yes');
            return this.append(value);
        }

        const newNode = {
            value: value,
            next: null,
            prev: null,
        };
        const leader = this.traverseToIndex(index - 1);
        const follower = leader.next;
        leader.next = newNode;
        newNode.prev = leader;
        newNode.next = follower;
        follower.prev = newNode;
        // this.length++;
        return this.printList();
    }
    traverseToIndex(index) {
        //Check parameters
        let counter = 0;
        let currentNode = this.head;
        while (counter !== index) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }
    remove(index) {
        // Check Parameters
        const leader = this.traverseToIndex(index - 1);
        const unwantedNode = leader.next;
        leader.next = unwantedNode.next;
        // this.length--;
        return this.printList();
    }
    reverse() {
        if (!this.head.next) {
            return this.head;
        }
        let first = this.head;
        this.tail = this.head;
        let second = first.next;
        while (second) {
            const temp = second.next;
            second.next = first;
            first = second;
            second = temp;
        }
        this.head.next = null;
        this.head = first;
        return this.printList();
    }
}

const myLinkedList = new DoublyLinkedList(10); 
myLinkedList.append(5); 
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.insert(2, 99);
myLinkedList.remove(2);
