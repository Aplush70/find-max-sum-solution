function findMaxSum(strings) {
  let maxSum = 0;
  
  for (const str of strings) {
    let currentSum = 0;
    
    for (const char of str) {
      if (char >= '0' && char <= '9') {
        currentSum += Number(char);
      }
    }
    
    if (currentSum > maxSum) maxSum = currentSum;
  }
  
  return maxSum;
}
module.exports = findMaxSum;