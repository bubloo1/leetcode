console.log("Hello World!")


// myArray(["bubloo","ganesh"],(name:string, isTrue: boolean)=> {
//     console.log("name is: ",name, isTrue)
// })


// function myArray (array: string[], callback: (arg0: string,arg1: boolean) => void) {
//     array.forEach((name: string) => {
//         callback(name,true)
//     })
// }



// function userDetails<T>(details:T): T {

//     return ("the details are of" + details) as T
// }

// const res = userDetails<string>("bubloo")
// console.log(res)
// let myMap = new Map<string, number[]>()

// myMap.set("bubloo", [24,1234,234])

// for (let [students,grades] of myMap){
//     console.log(students + " is " + grades)
// }

// console.log(myMap.get("bubloo"))


// function myPromise () {
//    return new Promise((resolve,reject) => {
//         const x = true
//         if (x) {
//             resolve("nice!")
//         }else{
//             reject("failed")
//         }
//     })
// }

// myPromise().then((result)=> {
//     console.log(result)
// })

// const fs = require('fs')

// fs.writefile('example.txt', "hello world!", (err: any) => {
//     if(err){
//         console.error('Error',err)
//     }else{
//         console.log("file is written")
//     }
// })


// function getPassword() {
//     var randPassword = Array(8).fill("1234567890").map(function (x) { return x[Math.floor(Math.random() * x.length)] }).join('');
//     return randPassword;
// }

// class NewClass {
//     name: string;
//     age: number;

//     constructor(name: string, age: number) {
//         this.name = name;
//         this.age = age;
//     }
// }


// let newObject = new NewClass("bubloo",24)

// console.log(newObject)


function createCounter() {
    let count = 0; // `count` is a private variable

    return function() {
        count += 1;
        return count;
    };
}

const counter1 = createCounter();
console.log(counter1()); // Output: 1
console.log(counter1()); // Output: 2
console.log(counter1()); // Output: 3

const counter2 = createCounter();
console.log(counter2()); // Output: 1
console.log(counter2()); // Output: 2



function addNumber <T>(num1:T,num2: T) {
    console.log(num1,num2)
}

const res = addNumber<number>(2,5)

console.log(res,"res")