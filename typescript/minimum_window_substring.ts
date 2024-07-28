
function minWindow(s: string, t: string): string {

    let charCountOfSubString: {[key:string]:number} = {}
    let windowOfString: {[key:string]: number } = {}
    let need = 0, have = 0
    let res = Infinity
    let start: number = 0
    let ans: [number, number] = [-1,-1]

    for(const char of t){
        charCountOfSubString[char] = (charCountOfSubString[char] ?? 0) + 1
    }
    need = Object.keys(charCountOfSubString).length
    
    for(let i = 0; i<s.length; i++){
        windowOfString[s[i]] = (windowOfString[s[i]] ?? 0) + 1

        if(charCountOfSubString[s[i]] && windowOfString[s[i]] === charCountOfSubString[s[i]]) have ++

        while (have === need){
            
            if(res > i - start){
                ans = [start,i]
                res = i - start
            }

            if(s[start] in windowOfString){
                windowOfString[s[start]] --
                if(windowOfString[s[start]] < charCountOfSubString[s[start]]){
                    have --
                }
            }
            
            start ++
        }

    }

    return res === Infinity ? "" : s.slice(ans[0],ans[1] + 1)
}
console.log(minWindow("ADOBECODEBANC", "ABC"))