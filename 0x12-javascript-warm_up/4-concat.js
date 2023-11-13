#!/usr/bin/node
let counter = 0
while (typeof process.argv[counter + 2] !== 'indifined') {
	counter++;
}
console.log(process.argv.[2] + ' is ' + process.argv[3]);
