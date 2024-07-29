
function maxSlidingWindow(nums: number[], k: number): number[] {
    let res: number[] = [] 
    let left: number = 0
    let right: number = 0
    let queue: number[] = []

    while(right < nums.length){
        while(queue && nums[queue[queue.length - 1]] < nums[right]){
            queue.pop()
        }
        queue.push(right)
 
        if(left > queue[0]){
            queue.shift()
        }

        if(right + 1 >= k){
            res.push(nums[queue[0]])
            left++
        }
        right ++

    }

    return res    
};


console.log(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))

// brute force solution time complexity = Olog(n - k) * k

// function maxSlidingWindow(nums: number[], k: number): number[] {
//     let res: number[] = [] 
//     for(let i = 0; i < nums.length - k + 1; i++){
//         let maxNumber = -Infinity 
//         for(let j = i; j < i + k; j++){

//             maxNumber = Math.max(nums[j],maxNumber)
//         }
//         res.push(maxNumber)
//     }

//     return res
    
// };

// [1  3  -1] -3  5  3  6  7 

