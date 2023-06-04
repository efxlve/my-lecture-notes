class MyArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index];
    }

    push(item) {
        // Add item to the end of the array
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }

    pop() {
        // Remove last item from the array
        const lastItem = this.data[this.length - 1];
        delete this.data[this.length - 1];
        this.length--;
        return lastItem;
    }

    delete(index) {
        // Remove item from the array
        const item = this.data[index];
        this.shiftItems(index);
        return item;
    }

    shiftItems(index) {
        // Shift items to the left
        for (let i = index; i < this.length - 1; i++) {
            // Shift items to the left
            this.data[i] = this.data[i + 1];
        }
        // Remove last item
        delete this.data[this.length - 1];
        this.length--;
    }
}

const newArray = new MyArray();
newArray.get(0); // undefined
newArray.push('hi'); // 1
newArray.push('you'); // 2
newArray.push('!'); // 3
newArray.pop(); // !
newArray.pop(); // you
newArray.push('are'); // 2
newArray.push('nice'); // 3
newArray.delete(1); // you are nice