function rot13(message){
    let lower_start=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    let upper_start=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    let lower_end=['n','o','p','q','r','s','t','u','v','w','x','y','z', 'a','b','c','d','e','f','g','h','i','j','k','l','m']
    let upper_end=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M']
    let final_message=[]

    for (i in message){
        if (lower_start.includes(message[i])){
            final_message.push(lower_end[lower_start.indexOf(message[i])])
            console.log(final_message)
        } else if (upper_start.includes(message[i])){
            final_message.push(upper_end[upper_start.indexOf(message[i])])
            console.log(final_message)
        } else {
            final_message.push(message[i])
            console.log(final_message)
        }

    }
    return final_message.join('')  
}

console.log(rot13('test'))