// Create a buffer from a string
const myStrBuffer = Buffer.from("freeCodeCamp");
console.log(myStrBuffer); // <Buffer 66 72 65 65 43 6f 64 65 43 61 6d 70>

// Create a buffer from an array of numbers
const myNumBuffer = Buffer.from([
    70, 82, 69, 69, 67, 79, 68, 69, 67, 65, 77, 80,
]);

console.log(myNumBuffer); // <Buffer 46 52 45 45 43 4f 44 45 43 41 4d 50>
console.log(myNumBuffer[0]); // 70
console.log(myStrBuffer[0]); // 102
console.log(myStrBuffer.toString()); // freeCodeCamp
console.log(myNumBuffer.toString()); // FREECODECAMP
const someBuffer = Buffer.alloc(10);
console.log(someBuffer); // <Buffer 00 00 00 00 00 00 00 00 00 00>