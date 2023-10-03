/*
Mean Square Error

Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair.

status: solved */

var solution = function(firstArray, secondArray) {
    let total_square_diff = 0
  
    for (i=0; i<firstArray.length; i++){
        let diff= firstArray[i]-secondArray[i]
        total_square_diff+= diff**2

  }
  return total_square_diff/firstArray.length
}