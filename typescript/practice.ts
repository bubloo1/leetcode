console.log("Hello World!")


// myArray(["bubloo","ganesh"],(name:string, isTrue: boolean)=> {
//     console.log("name is: ",name, isTrue)
// })


// function myArray (array: string[], callback: (arg0: string,arg1: boolean) => void) {
//     for(let ele of array){
//         callback(ele,true)
//     }
// }



// function userDetails<T>(details:T): string {

//     return "the details are" + details
// }

// const res = userDetails<string>("bubloo")

// let myMap = new Map<string, number[]>()

// myMap.set("bubloo", [24,1234,234])

// for (let [students,grades] of myMap){
//     console.log(students + " is " + grades)
// }

// console.log(myMap.get("bubloo"))


function myPromise () {
   return new Promise((resolve,reject) => {
        const x = true
        if (x) {
            resolve("nice!")
        }else{
            reject("failed")
        }
    })
}

myPromise().then((result)=> {
    console.log(result)
})

// const fs = require('fs')

// fs.writefile('example.txt', "hello world!", (err: any) => {
//     if(err){
//         console.error('Error',err)
//     }else{
//         console.log("file is written")
//     }
// })


function getPassword() {
    var randPassword = Array(8).fill("1234567890").map(function (x) { return x[Math.floor(Math.random() * x.length)] }).join('');
    return randPassword;
}