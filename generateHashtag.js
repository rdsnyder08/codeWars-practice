/*
The Hashtag Generator

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

status:solved*/

function generateHashtag (str) {
    if (str === '') {
        return false
    }
    let strArr = []
    for (i in str){
        strArr.push(str[i])
        //console.log(strArr)
    }
    for (let i = 0; i < strArr.length-1; i++) {
        if (strArr[i] === ' ') {
            //console.log(i)
            strArr[i+1] = strArr[i+1].toUpperCase()
            //console.log(strArr)
        }
    }
    for (let i = 0; i < strArr.length; i++) {
        if (strArr[i] === ' ') {
            
            strArr[i] = ''
            //console.log(strArr)
        }
    }
    finalStr='#'
    strArr[0]=strArr[0].toUpperCase()
  
    for (let i=0;i<strArr.length;i++){
        finalStr+=strArr[i]
    }
    if (finalStr.length > 140 || finalStr==='#'){
        return false
    }
    return finalStr
}

console.log(generateHashtag("Do We have A Hashtag"))