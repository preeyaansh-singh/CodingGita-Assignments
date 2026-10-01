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