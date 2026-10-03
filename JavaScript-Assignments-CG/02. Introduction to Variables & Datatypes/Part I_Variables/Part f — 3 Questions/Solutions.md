## JavaScript Advanced Data Types

### 5. Symbol Uniqueness
```js
let sym1 = Symbol("id");
let sym2 = Symbol("id");

console.log(sym1 === sym2); // false

let obj = {};
obj[sym1] = "Value 1";
obj[sym2] = "Value 2";

console.log(obj[sym1]);
console.log(obj[sym2]);
```
#### Explanation:

- Every Symbol is unique, even if they have the same description.
- sym1 === sym2 → false because they are different unique identifiers.
- Symbols are often used as object keys to avoid conflicts.

### 6. BigInt Precision
```js
let num = 9007199254740991;

console.log(num + 1);
console.log(num + 2);
console.log(num + 3);

let big = 9007199254740991n;

console.log(big + 1n);
console.log(big + 2n);
console.log(big + 3n);
```
#### Explanation:

- Regular number loses precision beyond Number.MAX_SAFE_INTEGER
- BigInt (n at the end) maintains exact precision
- Example issue:
    - num + 1 and num + 2 may give the same result (precision loss)
    - BigInt avoids this problem completely

### 7. Choose the Correct Type
- Unique identifier → Symbol
    ```js
    let id = Symbol("id");
    ```
- Very large integer with exact precision → BigInt
    ```js
    let bigNumber = 12345678901234567890n;
    ```
- Declared but not assigned → undefined
    ```js
    let x;
    ```
- Intentional empty value → null
    ```js
    let y = null;
    ```