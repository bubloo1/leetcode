
function checkInclusion(s1: string, s2: string): boolean {
    if (s1.length > s2.length) return false

    let charCountOfS1 = []
    let charCountOfS2 = []
    let count = 0
    for(let i =0; i<26; i++){
        charCountOfS2.push(0)
        charCountOfS1.push(0)
    }

    for(let i = 0; i < s1.length; i++){
        charCountOfS1[s1.charCodeAt(i) - 'a'.charCodeAt(0)] += 1
    }

    for(let j = 0; j<s2.length; j++){
        count = 0
        charCountOfS2[s2.charCodeAt(j) - 'a'.charCodeAt(0)] += 1

        if(j >= s1.length){
            charCountOfS2[s2[j - s1.length].charCodeAt(0) -  'a'.charCodeAt(0)] -= 1
        }

        for(let k = 0; k < 26; k++){
            if(charCountOfS1[k] === charCountOfS2[k]) count ++ 
        }

        if(count === 26) return true

    }
    return false
};

console.log(checkInclusion("ab", "eidbaooo"))