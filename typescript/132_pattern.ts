function find132pattern(nums: number[]): boolean {
    let stack: {num:number, minLeft:number}[] = []
    let currMin: number = nums[0]

   for(let n of nums.slice(1)){

        while(stack.length > 0 && n >= stack[stack.length - 1].num){
            stack.pop()
        }
        if(stack.length > 0 && n > stack[stack.length - 1].minLeft){
            return true
        }
        
        stack.push({num:n,minLeft:currMin})
        currMin = Math.min(currMin,n)

    }   

    return false
};

console.log(find132pattern([3,1,4,2]))

// brute force 0(n**3)
// function find132pattern(nums: number[]): boolean {

//     for(let i = 0; i < nums.length; i++){
//         for(let j = i; j < nums.length; j++){
//             for(let k = j + 1; k < nums.length; k++){
//                 if(nums[i] < nums[k] && nums[k] < nums[j]){
//                     return true
//                 }
//             }

//         }
//     }
//     return false
// };