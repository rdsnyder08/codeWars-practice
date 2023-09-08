function duplicateCount(text){
    let textLower = text.toLowerCase();
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',]
    counter = 0
    for (i in arr) {
        if (text.split(arr[i]).length-1>=2){
            counter++

        }
    }
    return counter
}
console.log(duplicateCount("aabbcde"))