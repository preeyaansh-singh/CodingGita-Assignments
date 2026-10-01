## Q11. Predict the Hoisting Behavior

### Code:
```js
console.log(a);
console.log(b);
console.log(c);

var a = 10;
let b = 20;
const c = 30;
```
### Output:
```
undefined
ReferenceError: Cannot access 'b' before initialization
ReferenceError: Cannot access 'c' before initialization
```
#### Explanation :
- var a :
    - Hoisted to the top and initialized with undefined
    - So console.log(a) prints undefined
- let b and const c :
    - Also hoisted, but not initialized
    - They remain in a Temporal Dead Zone (TDZ) until their    declaration line
    - Accessing them before initialization causes a ReferenceError

#### Summary :
- var → hoisted + initialized (undefined)
- let / const → hoisted but not initialized (TDZ → error)

## Q12. Fix the Hoisting Errors

### Corrected Code:
```js
var x = "Hello";
let y = "World";
const z = "!";

console.log(x);
console.log(y);
console.log(z);

console.log(x + " " + y + z);
```
### Explanation:
- var is hoisted and initialized as undefined, so it would not throw an error, but printing after assignment is better practice.
- let and const are hoisted but stay in the Temporal Dead Zone (TDZ) until declared, so accessing them before declaration causes errors.
- Fix: Move all declarations before usage to avoid hoisting-related issues.