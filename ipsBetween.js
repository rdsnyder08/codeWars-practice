/*
count IP Addresses

Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Status: solved */

function ipsBetween(start, end){
  let startInt=0
  let endInt=0

  startArr= start.split('.')
  for (let i=0; i< startArr.length; i++){
    startArr[i]=parseInt(startArr[i])
    if (i===0){
      startInt+=startArr[i] * 256 ** 3
    }
    if (i===1){
      startInt+= startArr[i]*256**2
    }
    if (i===2){
      startInt+= startArr[i]*256
    }
    if (i===3){
      startInt+= startArr[i]
    }
  }

  endArr= end.split('.')
  for (let i=0; i< endArr.length; i++){
    endArr[i]=parseInt(endArr[i])
    if (i===0){
      endInt+=endArr[i] * 256 ** 3
    }
    if (i===1){
      endInt+= endArr[i]*256**2
    }
    if (i===2){
      endInt+= endArr[i]*256
    }
    if (i===3){
      endInt+= endArr[i]
    }
  }


  //console.log(startInt)
  return endInt-startInt
    
  }

console.log(ipsBetween("150.0.0.0", "150.0.0.1"))