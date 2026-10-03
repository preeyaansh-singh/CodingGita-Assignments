## JavaScript Data Types Practice

### 1. Classify the Types
```js
let wholeNumber = 10;
let decimalNumber = 3.14;
let text = "Hello";
let isTrue = true;

console.log(wholeNumber, typeof wholeNumber);
console.log(decimalNumber, typeof decimalNumber);
console.log(text, typeof text);
console.log(isTrue, typeof isTrue);
```
### 2. Undefined vs Null
```js
let a;        // undefined
let b = null; // explicitly assigned null

console.log(a, typeof a);
console.log(b, typeof b);
```
#### Explanation:
- undefined → variable declared but not assigned any value
- null → intentional absence of value (set by programmer)
- Note: typeof null returns "object" (this is a known JavaScript quirk)

### 3. Number Special Values
```js
let posInfinity = Infinity;
let negInfinity = -Infinity;
let notANumber = NaN;
let scientific = 2.5e3;      // 2500
let readable = 1_000_000;    // 1000000

console.log(posInfinity, typeof posInfinity);
console.log(negInfinity, typeof negInfinity);
console.log(notANumber, typeof notANumber);
console.log(scientific, typeof scientific);
console.log(readable, typeof readable);
```
### 4. String Styles
```js
let name = "Preeyaansh";

let str1 = 'Hello';
let str2 = "World";
let str3 = `Hello, ${name}!`;

console.log(str1);
console.log(str2);
console.log(str3);
```