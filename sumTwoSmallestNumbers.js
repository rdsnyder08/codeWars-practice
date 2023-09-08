function sumTwoSmallestNumbers(numbers) {
    numbers.sort(function(a, b){return b - a});
    while (numbers.length>2){
        numbers.shift();

    }
    let sum = numbers[0]+numbers[1]
    return sum  

  }

console.log(sumTwoSmallestNumbers([19,5,42,2,77]))
