/*
Area of a circle

Complete the function which will return the area of a circle with the given radius.

Round the returned number to two decimal places. If the radius is not positive or not a number, return false.

Status: completed */

var circleArea = function(radius) {
    if (typeof(radius)!== 'number' || radius <= 0){
        return false
    }
    let areaOfCircleUnrounded = 3.14159265358979323 * radius * radius
    let areaOfCircleRounded = areaOfCircleUnrounded.toFixed(2)
    return parseFloat(areaOfCircleRounded)

  
}

