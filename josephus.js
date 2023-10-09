function josephus(items,k){
    let expandedArr=[]
    if (items.length===0){
        return expandedArr
    }
    for (let i=0; i<=1000 ; i++){
        expandedArr.push(...items)
    }
    //console.log(expandedArr)
    counter= 0
    finalArr=[]
    for (let i=0;i<expandedArr.length; i++){
        if (!finalArr.includes(expandedArr[i])){
            counter += 1
            //console.log(expandedArr[i])
        }
        if (counter%k===0 && !finalArr.includes(expandedArr[i])){
            //console.log(`counter is ${counter}`)
            //console.log(expandedArr[i])
            finalArr.push(expandedArr[i])
        }
        if (finalArr.length === items.length){
            return finalArr
        }

    }

  }

console.log(josephus([1,2,3,4,5,6,7],3))