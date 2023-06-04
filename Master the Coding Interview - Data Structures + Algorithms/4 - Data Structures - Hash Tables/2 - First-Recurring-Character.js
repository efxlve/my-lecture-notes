//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return undefined

// Solution 1 - Naive
function firstRecurringCharacter1(input) {
    for (let i = 0; i < input.length; i++) {
        for (j = i + 1; j < input.length; j++) {
            if (input[i] === input[j]) {
                return input[i];
            }
        }
    }
    return undefined;
}

firstRecurringCharacter1([2, 5, 1, 2, 3, 5, 1, 2, 4]); // O(n^2)

// Solution 2 - Hash Table
function firstRecurringCharacter2(input) {
    // Check input
    if (!input || input.length === 0) {
        return undefined;
    }

    // Find first recurring character
    const map = {};
    let firstRecurringCharacter;

    for (let i = 0; i < input.length; i++) {
        const currentCharacter = input[i];

        if (map[currentCharacter]) {
            firstRecurringCharacter = currentCharacter;
            break;
        } else {
            map[currentCharacter] = true;
        }
    }

    return firstRecurringCharacter;
}

firstRecurringCharacter2([2, 5, 1, 2, 3, 5, 1, 2, 4]); // O(n)