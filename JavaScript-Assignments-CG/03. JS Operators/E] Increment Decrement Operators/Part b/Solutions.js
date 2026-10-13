// 6. Start with x = 5. Create y = x++.
// Print both x and y.
let x = 5;
let y = x++;

console.log(x); // 6
console.log(y); // 5

// Explanation:
// x++ is post-increment.
// First, the original value (5) is assigned to y.
// Then x is incremented by 1.
// Therefore, x = 6 and y = 5.


// 7. Start with a = 5. Create b = ++a.
// Print both a and b.
let a = 5;
let b = ++a;

console.log(a); // 6
console.log(b); // 6

// Explanation:
// ++a is pre-increment.
// First, a is incremented from 5 to 6.
// Then the updated value (6) is assigned to b.
// Unlike post-increment, pre-increment updates the value first.


// 8. Start with lives = 3.
// Use post-decrement and store the result in previousLives.
let lives = 3;
let previousLives = lives--;

console.log(lives);         // 2
console.log(previousLives); // 3

// Explanation:
// lives-- is post-decrement.
// The original value (3) is assigned to previousLives first.
// Then lives decreases by 1, becoming 2.


// 9. Start with attempts = 0.
// Use pre-increment and store the result in currentAttempts.
let attempts = 0;
let currentAttempts = ++attempts;

console.log(attempts);        // 1
console.log(currentAttempts); // 1

// Explanation:
// ++attempts is pre-increment.
// First, attempts increases from 0 to 1.
// Then the updated value (1) is assigned to currentAttempts.


// 10. Start with points = 100.
// Increase it using ++, then decrease it using --.
let points = 100;

points++;
points--;

console.log(points); // 100

// Explanation:
// Initial value = 100
// After points++ = 101
// After points-- = 100
// Therefore, the final value is 100.
