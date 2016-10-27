var path = require("path");

var hello = "Hello World New"

var justNode = hello.slice(7);

console.log("Hello World");
console.log(hello);
console.log(`Rock on World from ${justNode}`);

console.log(__dirname);

console.log(__filename);

console.log(`Rock on World from ${path.basename(__filename)}`);