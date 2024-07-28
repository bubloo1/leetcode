
function containsNearbyDuplicate(nums: number[], k: number): boolean {
    
    let window = new Set()

    for(let i = 0, start = 0; i<nums.length; i++){

        if(i - start > k){
            window.delete(nums[start])
            start ++
        }
     
        if(window.has(nums[i])){
            return true
        }
        window.add(nums[i])
    }
 
    return false

};

console.log(containsNearbyDuplicate([1,0,1,1],1))