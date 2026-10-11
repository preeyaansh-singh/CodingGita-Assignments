// 1. Minimum marks required for distinction is 75.
// A student scored 75. Check if the student gets distinction.
let marks = 75;
let distinctionMarks = 75;

console.log(marks >= distinctionMarks); // true
// Explanation: 75 is equal to 75, so the student gets distinction.
// The >= operator checks whether a value is greater than or equal to another.


// 2. Ticket price is ₹300. A person has ₹300.
// Check if they can buy the ticket.
let ticketPrice = 300;
let availableMoney = 300;

console.log(availableMoney >= ticketPrice); // true
// Explanation: The person has exactly the required amount.
// Therefore, they can buy the ticket.


// 3. Predict the output.
console.log(25 >= 25); // true
console.log(30 >= 25); // true
console.log(20 >= 25); // false

// Explanation:
// 25 is equal to 25, so the result is true.
// 30 is greater than 25, so the result is true.
// 20 is neither greater than nor equal to 25, so the result is false.


// 4. Predict the output.
console.log("25" >= 25);  // true
console.log("10" >= "2"); // false
console.log(null >= 0);   // true

// Explanation:
// "25" >= 25: The string "25" is converted to the number 25.
// Therefore, 25 >= 25 is true.

// "10" >= "2": Both operands are strings, so JavaScript
// compares them lexicographically (character by character).
// "1" comes before "2", so the result is false.

// null >= 0: null is converted to the number 0.
// Therefore, 0 >= 0 is true.


// 5. What is the result of undefined >= 0?
console.log(undefined >= 0); // false
// Explanation: undefined is converted to NaN during comparison.
// Relational comparisons involving NaN return false.


// 6. A lift can carry a maximum of 8 people.
// Currently, 8 people are inside.
// Check whether the lift is full or overloaded using >=.
let liftCapacity = 8;
let currentPeople = 8;

console.log(currentPeople >= liftCapacity); // true
// Explanation: 8 >= 8 is true.
// The lift has reached its maximum capacity.


// 7. Predict and explain the outputs.

console.log(true >= 1); // true
// Explanation: true is converted to the number 1.
// Therefore, 1 >= 1 is true.


console.log("" >= 0); // true
// Explanation: The empty string "" is converted to the number 0.
// Therefore, 0 >= 0 is true.


console.log(NaN >= NaN); // false
// Explanation: NaN represents Not-a-Number.
// Relational comparisons involving NaN always return false.
