var beeramid = function(bonus, price) {
    let cost_so_far= 0
    let n=0
    let height=0
    if (price > bonus){
        return 0
    }
    while (cost_so_far <= bonus) {
        cost_so_far += n**2 * price
        height+=1
        n+=1
        console.log(`height is now ${height}`)

    }
    return height-2
  
}

console.log(beeramid(455, 5))