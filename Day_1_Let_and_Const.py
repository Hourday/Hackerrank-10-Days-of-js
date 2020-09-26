'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    const PI=Math.PI;
    var r=readLine();
    function area(){
        return PI*r*r;
    }
    function perimeter(){
        return 2*PI*r;
    }
    // Print the area of the circle:
console.log(area());
console.log(perimeter());
    // Print the perimeter of the circle:

    try {    