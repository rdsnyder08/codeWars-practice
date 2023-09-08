function countSmileys(arr) {
    let counter = 0;
    for (i in arr){
        if(arr[i]=== ';)' || arr[i]=== ':)' || arr[i]=== ';)' || arr[i]=== ';D'|| arr[i]=== ':D' || arr[i]=== ';-)' || arr[i]=== ':-)' || arr[i]=== ';-)' || arr[i]=== ';-D'|| arr[i]=== ':-D' ||arr[i]=== ';~)' || arr[i]=== ':~)' || arr[i]=== ';~)' || arr[i]=== ';~D'|| arr[i]=== ':~D'){
            counter +=1
        }
    }
    return counter;
  }


console.log(countSmileys([':)', ';(', ';}', ':-D']))