class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }

    _hash(key) {
        let hash = 0;

        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) %
                this.data.length;
        }

        return hash;
    }

    set(key, value) {
        const address = this._hash(key);

        if (!this.data[address]) {
            this.data[address] = [];
        }

        this.data[address].push([key, value]);

        return this.data;
    }

    get(key) {
        const address = this._hash(key);
        const currentBucket = this.data[address];

        if (currentBucket) {
            for (let i = 0; i < currentBucket.length; i++) {
                const currentBucketItem = currentBucket[i];

                if (currentBucketItem[0] === key) {
                    return currentBucketItem[1];
                }
            }
        }

        return undefined;
    }

    keys() {
        const keysArray = [];

        for (let i = 0; i < this.data.length; i++) {
            const currentBucket = this.data[i];

            if (currentBucket) {
                for (let j = 0; j < currentBucket.length; j++) {
                    const currentBucketItem = currentBucket[j];

                    keysArray.push(currentBucketItem[0]);
                }
            }
        }

        return keysArray;
    }

    values() {
        const valuesArray = [];

        for (let i = 0; i < this.data.length; i++) {
            const currentBucket = this.data[i];

            if (currentBucket) {
                for (let j = 0; j < currentBucket.length; j++) {
                    const currentBucketItem = currentBucket[j];

                    valuesArray.push(currentBucketItem[1]);
                }
            }
        }

        return valuesArray;
    }
}

const myHashTable = new HashTable(50); // O(1)
myHashTable.set('grapes', 10000); // O(1)
myHashTable.set('apples', 54); // O(1)
myHashTable.set('oranges', 2); // O(1)
myHashTable.get('grapes'); // O(1)
myHashTable.keys(); // O(n)
myHashTable.values(); // O(n)
