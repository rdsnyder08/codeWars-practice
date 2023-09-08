function XO(str) {
    let strLower = str.toLowerCase();
    if ((strLower.match(/x/g) || []).length === (strLower.match(/o/g) || []).length){
        return true
    } else {
        return false
    }
}

console.log(XO("ooxx"))