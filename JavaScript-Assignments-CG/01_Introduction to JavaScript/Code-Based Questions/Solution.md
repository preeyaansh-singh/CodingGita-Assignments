## Q20. Output Prediction

```js
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);
```
### Output 
- number
- string
- boolean

### Explanation:
- JavaScript is **dynamically typed**, so the type of a variable can change at runtime.
- `25` → number  
- `"JavaScript"` → string  
- `false` → boolean

## Q21. HTML + JavaScript Alert Program

```html
<!DOCTYPE html>
<html>
<head>
  <title>JS Alert</title>
</head>
<body>

<button onclick="showAlert()">Click Me</button>

<script>
function showAlert() {
  alert("Welcome to JavaScript!");
}
</script>

</body>
</html>
```
## Q22. Event-Driven Programming Example

```html
<!DOCTYPE html>
<html>
<head>
  <title>Event Example</title>
</head>
<body>

<button id="myBtn">Click Me</button>
<p id="demo">Original Text</p>

<script>
document.getElementById("myBtn").addEventListener("click", function() {
  document.getElementById("demo").innerText = "Button was clicked!";
});
</script>

</body>
</html>
```