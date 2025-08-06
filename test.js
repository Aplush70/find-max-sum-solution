const findMaxSum = require('./solution');
     
console.log("TEST 1 (Empty):", findMaxSum([]) === 0 ? "✅ PASS" : "❌ FAIL");
console.log("TEST 2 (No digits):", findMaxSum(["abc"]) === 0 ? "✅ PASS" : "❌ FAIL");
console.log("TEST 3 (Multiple):", findMaxSum(["a1b2"]) === 3 ? "✅ PASS" : "❌ FAIL");
console.log("TEST 4 (Example):", findMaxSum([
  "dh7js4jf", 
  "or2rjvn2w", 
  "h1n36mfl", 
  "a7e6fw"
]) === 13 ? "✅ PASS" : "❌ FAIL");