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

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var l=s.length;
    var a=[]
    var b=[]
    //console.log(l)
    for(var i=0; i<l; i++){
        if(s[i]=="a" ||s[i]=="e" ||s[i]=="i" ||s[i]=="o" ||s[i]=="u"){
          a=s[i];
        console.log(a)
        }else
            b=b+s[i]+"\n";
        }
    console.log(b)
}

