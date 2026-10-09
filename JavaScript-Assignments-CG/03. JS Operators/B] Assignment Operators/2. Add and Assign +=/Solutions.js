// 1. A player's score is 80. He scores 25 more points.
let playerScore = 80;
playerScore += 25;

console.log(playerScore); // 105


// 2. A wallet has ₹1500. Cashback of ₹120 is added.
let walletBalance = 1500;
walletBalance += 120;

console.log(walletBalance); // 1620


// 3. Predict the output.
let count = 10;
count += 5;

console.log(count); // 15
// Explanation: count += 5 means count = count + 5.
// Therefore, 10 + 5 = 15.


// 4. Predict the output.
let msg = "Good";
msg += " Morning";

console.log(msg); // Good Morning
// Explanation: The += operator joins the two strings.


// 5. Find the final value after n += "5".
let n = 20;
n += "5";

console.log(n);        // 205
console.log(typeof n); // string

// Explanation:
// n += "5" is equivalent to n = n + "5".
// Since one operand is a string, + performs concatenation.
// Therefore, 20 + "5" becomes "205", a string.

