var sayings = [
	"Hello",
	"Blah",
	"Yup",
	"Hungry!"
];

var interval = setInterval(function() {
	var i = Math.floor(Math.random() * sayings.length);
	process.stdout.write(`${sayings[i]} \n`);
}, 1000);

process.stdin.on('data', function(data) {
	console.log(`STDIN Data Received -> ${data.toString().trim()}`);
	clearInterval(interval);
	process.exit();
});