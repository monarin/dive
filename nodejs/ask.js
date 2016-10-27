var questions = [
	"What is your name?",
	"Whate is your hobby?",
	"What is your prefereed language?"
];
var answers = [];

function ask(i){
	process.stdout.write(`\n\n\n ${questions[i]}`);
	process.stdout.write("   >   ");
}

process.stdin.on('data', function(data) {
	//process.stdout.write('\n' + data.toString().trim() + '\n');
	answers.push(data.toString().trim());
	if (answers.length < questions.length) {
		ask(answers.length);
	} else {
		process.exit();
	}
});

process.on('exit', function(){
	process.stdout.write('\n\n\n');
	process.stdout.write(`Go ${answers[1]} ${answers[0]}`);
	process.stdout.write('\n\n\n');
});
ask(0);