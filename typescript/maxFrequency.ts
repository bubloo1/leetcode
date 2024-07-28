

function maxFrequency(nums: number[], k: number): number {
    nums.sort((a, b) => a - b); 
    let right = 0, left = 0
    let res = 0, total = 0

    while(right < nums.length){
        total = total + nums[right]

        while( (nums[right] * (right - left + 1) > total + k) ){
            total -= nums[left]
            left += 1
        }

        res = Math.max(res,right - left + 1)

        right += 1
    }
    return res
}


console.log(maxFrequency([1, 2, 4], 5)); 

// bruteforece using recursion

// function maxFrequency(nums: number[], k: number): number {
//     nums.sort((a, b) => a - b); 
//     let maxFreq = 0;

//     function dfs(i: number, k: number, currentFreq: number, target: number) {
//         if (i < 0) return; 

        
//         let diff = target - nums[i];
        
//         if (diff <= k) { 
//             currentFreq += 1;
//             maxFreq = Math.max(maxFreq, currentFreq); 
//             dfs(i - 1, k - diff, currentFreq, target); 
//         } else { 
//             dfs(i - 1, k, currentFreq, target); 
//         }
//     }

//     for (let i = nums.length - 1; i >= 0; i--) {
//         dfs(i, k, 0, nums[i]); 
//     }

//     return maxFreq;
// }

// console.log(maxFrequency([1, 2, 4], 5)); 


