## JavaScript Variable Practice (Part 2)

### 5. Choose the Correct Keyword
```js
const studentName = "Preeyaansh"; // will not change
let marks = 75;                  // can change
const schoolName = "ABC School"; // will not change

marks = 90;

console.log(studentName);
console.log(marks);
console.log(schoolName);
```
### 6. Understand Scope
```js
if (true) {
  var a = 10;
  let b = 20;
  const c = 30;
}

console.log(a); // ✅ Accessible (function/global scoped)
console.log(b); // ❌ Error (block scoped)
console.log(c); // ❌ Error (block scoped)
```
#### Observation
- var is accessible outside the block
- let and const are block-scoped (not accessible outside)

### 7. Test Re-declaration
```js
var user = "John";
var user = "Doe"; // ✅ Allowed
console.log(user);

let user2 = "Alice";
// let user2 = "Bob"; ❌ Error (Cannot redeclare)
```
#### Observation
- var allows re-declaration
- let does NOT allow re-declaration

### 8. Test Re-assignment
```js
var x = 10;
let y = 20;
const z = 30;

x = 15; // ✅ Allowed
y = 25; // ✅ Allowed
// z = 35; ❌ Error (Cannot reassign constant)

console.log(x);
console.log(y);
console.log(z);
```
#### Observation:
- var → re-assign allowed
- let → re-assign allowed
- const → ❌ cannot be re-assigned