## Q9. Predict and Explain

### Code:
```js
var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y);
console.log(z);
```
### Output

```
20
ReferenceError: y is not defined
ReferenceError: z is not defined
```
#### Observation
- var x is function/global scoped, so the value 20 overwrites the previous value 10.
- let y and const z are block-scoped, so they are only accessible inside the if block.
- Accessing y and z outside the block causes ReferenceError.

## Q10. Fixed Program
- Corrected Code:
```js
const name = "Preeyaansh"; // initialized properly

let age = 20;
age = 25; // re-assignment instead of re-declaration

if (true) {
    var city = "Delhi";     // accessible outside
    var country = "India";  // changed to var so it's accessible
}

console.log(country);

const score = 50;
// score = 80; ❌ not allowed, so removed

console.log(name);
console.log(age);
console.log(score);
```
#### Fixes Applied:
- const name; → initialized during declaration
- Removed re-declaration of age → used re-assignment
- Changed country to var → so it can be accessed outside the block
- Removed re-assignment of const score → not allowed