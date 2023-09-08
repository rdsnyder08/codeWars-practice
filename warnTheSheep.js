function warnTheSheep(queue) {
    if (queue[queue.length -1 ]==='wolf'){
        return 'Pls go away and stop eating my sheep'
    } else {
        reverseQ= queue.reverse()
        for (i in reverseQ){
            if (reverseQ[i] == 'wolf'){
                return `Oi! Sheep number ${i}! You are about to be eaten by a wolf!`
            }
        }

    }


}

console.log(warnTheSheep(["sheep", "sheep", "sheep", "wolf", "sheep"]))