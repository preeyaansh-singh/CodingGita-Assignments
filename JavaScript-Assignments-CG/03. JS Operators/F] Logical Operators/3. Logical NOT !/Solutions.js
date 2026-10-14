// JavaScript Practice – Logical NOT Operator (!)


// 1. A user is not banned.
// Check if they can login by negating isBanned.
let isBanned = false;

console.log(!isBanned); // true
// Explanation: !false = true.
// The user is not banned, so login is allowed.


// 2. A task is not completed.
// Check if it is still pending using !.
let isCompleted = false;

console.log(!isCompleted); // true
// Explanation: !false = true.
// The task is not completed, so it is still pending.


// 3. A light is on.
// Check if it is off using !.
let isOn = true;

console.log(!isOn); // false
// Explanation: !true = false.
// The light is on, so it is not off.


// 4. A subscription is not active.
// Check if the user cannot access premium content using !.
let isActive = false;

console.log(!isActive); // true
// Explanation: !false = true.
// The subscription is inactive, so premium access is unavailable.


// 5. A file is not read-only.
// Check if it can be edited using !.
let isReadOnly = false;

console.log(!isReadOnly); // true
// Explanation: !false = true.
// The file is not read-only, so it can be edited.


// Key Concept:
// The ! operator reverses the boolean value.
// !true  = false
// !false = true

// JavaScript Practice – Logical NOT Operator (!)
// Additional Questions (Q6 – Q10)


// 6. Predict the output.
{
    let a = 0;
    let b = 1;

    console.log(!a, !b); // true false

    // Explanation:
    // 0 is falsy, so !0 returns true.
    // 1 is truthy, so !1 returns false.
}


// 7. Predict the output.
{
    let x = "Hello";
    let y = "";

    console.log(!x, !y); // false true

    // Explanation:
    // "Hello" is a non-empty string, so it is truthy.
    // An empty string "" is falsy.
    // Therefore, !"Hello" = false and !"" = true.
}


// 8. Predict the output.
{
    let val = 5;
    let result = !val;

    console.log(result); // false

    // Explanation:
    // 5 is a non-zero number, so it is truthy.
    // The ! operator reverses its boolean value.
    // Therefore, !5 returns false.
}


// 9. Predict the output.
{
    let a = 10;
    let b = 20;
    let result = !(a && b);

    console.log(result); // false

    // Explanation:
    // Both 10 and 20 are truthy values.
    // a && b returns 20 (the last truthy operand).
    // !20 returns false.
    // Therefore, result = false.
}


// 10. Predict the output.
{
    let x = 0;
    let y = 1;
    let result = !(x || y);

    console.log(result); // false

    // Explanation:
    // 0 is falsy and 1 is truthy.
    // x || y returns 1 (the first truthy operand).
    // !1 returns false.
    // Therefore, result = false.
}


// Key Concept:
// The ! operator converts a value to a boolean
// and reverses its truthiness.

// Examples:
console.log(!0);       // true
console.log(!1);       // false
console.log(!"");      // true
console.log(!"Hello"); // false
console.log(!null);    // true
console.log(!undefined); // true
console.log(!NaN);     // true