// 1. A teacher distributes 144 pencils equally among 12 students.
// Find the number of pencils each student receives.
let totalPencils = 144;
let numberOfStudents = 12;
console.log(totalPencils / numberOfStudents); // 12


// 2. A train travels 360 kilometres in 6 hours.
// Find its average distance travelled per hour.
let totalDistance = 360;
let travelTime = 6;
console.log(totalDistance / travelTime); // 60


// 3. A company distributes ₹72,000 equally among 9 departments.
// Find the amount received by each department.
let totalAmount = 72000;
let numberOfDepartments = 9;
console.log(totalAmount / numberOfDepartments); // 8000


// 4. Predict the output.
let a = "20";
let b = 4;
let result = a / b;
console.log(result); // 5
// Explanation: JavaScript converts the string "20" into the number 20.
// 20 / 4 = 5


// 5. Predict the output.
let x = "100";
let y = "5";
let result2 = x / y;
console.log(result2); // 20
// Explanation: Both strings are converted into numbers.
// 100 / 5 = 20


// 6. What is the output of 144 / 12?
console.log(144 / 12); // 12


// 7. 360 students are divided equally into 9 classrooms.
// How many students per classroom?
let totalStudents = 360;
let numberOfClassrooms = 9;
console.log(totalStudents / numberOfClassrooms); // 40


// 8. What is the result of "100" / 4 and "100" / "4"?
console.log("100" / 4);   // 25
console.log("100" / "4"); // 25
// Explanation: The division operator (/) converts numeric strings
// into numbers before performing the calculation.


// 9. A bill of ₹2400 is shared equally among 6 friends.
// Write the expression and find each person's share.
// Expression: 2400 / 6 = 400
let totalBill = 2400;
let numberOfFriends = 6;
console.log(totalBill / numberOfFriends); // 400


// 10. Predict and explain the outputs.

// Division by positive zero
console.log(10 / 0); // Infinity
// Explanation: A positive number divided by zero produces Infinity
// in JavaScript.


// Division by negative zero
console.log(-10 / 0); // -Infinity
// Explanation: A negative number divided by positive zero
// produces -Infinity.


// Zero divided by zero
console.log(0 / 0); // NaN
// Explanation: 0 / 0 is undefined mathematically.
// JavaScript returns NaN (Not-a-Number).


// Division with numeric strings
console.log("20" / "4" / 2); // 2.5
// Explanation: "20" and "4" are converted into numbers.
// Division is evaluated from left to right:
// 20 / 4 = 5
// 5 / 2 = 2.5


// Division with a non-numeric string
console.log("abc" / 5); // NaN
// Explanation: "abc" cannot be converted into a valid number.
// Therefore, the result is NaN.

