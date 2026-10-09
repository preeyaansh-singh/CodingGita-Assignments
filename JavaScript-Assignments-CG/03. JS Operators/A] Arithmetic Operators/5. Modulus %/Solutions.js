// 1. A teacher has 53 students and forms groups of 5.
// Find the number of students left over.
let totalStudents = 53;
let studentsPerGroup = 5;

console.log(totalStudents % studentsPerGroup); // 3


// 2. A shop has 128 candies and packs 10 candies in each box.
// Find the number of candies left unpacked.
let totalCandies = 128;
let candiesPerBox = 10;

console.log(totalCandies % candiesPerBox); // 8


// 3. A factory produces 237 toys and packs them in boxes of 6.
// Find how many toys are left after packing full boxes.
let totalToys = 237;
let toysPerBox = 6;

console.log(totalToys % toysPerBox); // 3


// 4. A bus can carry 40 passengers.
// If 185 people are waiting, find how many people are left
// after filling as many full buses as possible.
let people = 185;
let busCapacity = 40;

console.log(people % busCapacity); // 25


// 5. Predict the output.
let a = 10;
let b = 0;
let result = a % b;

console.log(result); // NaN
// Explanation: The remainder operation with a divisor of zero
// produces NaN in JavaScript.


// 6. What is the output of 29 % 5?
console.log(29 % 5); // 4
// Explanation: 29 = (5 * 5) + 4
// The remainder is 4.


// 7. There are 23 chocolates to be packed in boxes of 4.
// How many chocolates will be left over?
let chocolates = 23;
let chocolatesPerBox = 4;

console.log(chocolates % chocolatesPerBox); // 3


// 8. What is the result of 0 % 7 and 15 % 0? Explain.
console.log(0 % 7);  // 0
console.log(15 % 0); // NaN
// Explanation:
// 0 % 7 = 0 because zero divided by 7 leaves no remainder.
// 15 % 0 = NaN because the divisor is zero.


// 9. A total of 47 pages need to be printed on sheets
// that hold 6 pages each.
// Find the number of full sheets and pages left over.
let totalPages = 47;
let pagesPerSheet = 6;

let fullSheets = Math.floor(totalPages / pagesPerSheet);
let leftoverPages = totalPages % pagesPerSheet;

console.log(fullSheets);    // 7
console.log(leftoverPages); // 5

// Expressions:
// Full sheets = Math.floor(47 / 6) = 7
// Pages left over = 47 % 6 = 5


// 10. Predict and explain the outputs, especially the signs.

console.log(17 % 5); // 2
// Explanation: 17 = (3 * 5) + 2
// The remainder is 2.

console.log(-17 % 5); // -2
// Explanation: The remainder takes the sign of the dividend (-17).

console.log(17 % -5); // 2
// Explanation: The remainder takes the sign of the dividend (17),
// so the result is positive.

console.log(-17 % -5); // -2
// Explanation: The dividend is negative (-17),
// so the remainder is negative.

console.log(10 % 0); // NaN
// Explanation: Modulus with a divisor of zero produces NaN.

