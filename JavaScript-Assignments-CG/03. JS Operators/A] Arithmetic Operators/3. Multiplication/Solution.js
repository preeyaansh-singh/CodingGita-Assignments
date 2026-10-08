// 1. One notebook costs ₹45. Calculate the cost of buying 8 notebooks.
let notebookCost = 45;
let notebooks = 8;
let totalNotebookCost = notebookCost * notebooks;

console.log(totalNotebookCost); // 360


// 2. A machine produces 120 bottles per hour. Calculate its production in 6 hours.
let bottlesPerHour = 120;
let hours = 6;
let totalBottles = bottlesPerHour * hours;

console.log(totalBottles); // 720


// 3. A garden has 7 rows with 15 plants in each row.
let rows = 7;
let plantsPerRow = 15;
let totalPlants = rows * plantsPerRow;

console.log(totalPlants); // 105


// 4. Predict the output:
let a = "5";
let b = 4;
let result = a * b;

console.log(result); // 20
// Explanation: JavaScript converts the string "5" into the number 5.


/* 5. Predict the output:
let x = "10";
let y = "2";
let result = x * y;
console.log(result);
*/

// Output: 20
// Explanation: Both strings are converted to numbers during multiplication.


// 6. What is the output of 12 * 8?
console.log(12 * 8); // 96


// 7. One pizza costs ₹299. What is the total cost of 4 pizzas?
let pizzaCost = 299;
let pizzas = 4;
let totalPizzaCost = pizzaCost * pizzas;

console.log(totalPizzaCost); // 1196


// 8. What is the result of "7" * 6 and "7" * "6"?
console.log("7" * 6);   // 42
console.log("7" * "6"); // 42

// Explanation: The * operator converts numeric strings into numbers.


// 9. A factory produces 45 units per hour.
// How many units does it produce in 8 hours?
let unitsPerHour = 45;
let productionHours = 8;
let totalUnits = unitsPerHour * productionHours;

console.log(totalUnits); // 360
// Expression: 45 * 8 = 360


// 10. Predict and explain the outputs:

console.log("5" * 3 * "2");
// Output: 30
// Explanation: "5" becomes 5 and "2" becomes 2.
// 5 * 3 * 2 = 30


console.log("abc" * 4);
// Output: NaN
// Explanation: "abc" cannot be converted into a number.



console.log(10 * "2.5");
// Output: 25
// Explanation: "2.5" is converted into the number 2.5.
// 10 * 2.5 = 25


console.log("10" * "2.5" * "0");
// Output: 0
// Explanation: All three strings are converted into numbers.
// 10 * 2.5 * 0 = 0