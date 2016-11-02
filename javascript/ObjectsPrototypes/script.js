// Simple prototype example

function Player(n, s, r) {
    this.name = n;
    this.score = s;
    this.rank = r;
}

Player.prototype.logInfo = function() {
	console.log("I am:", this.name);
}

Player.prototype.promote = function() {
	this.rank++;
	console.log("My new rank is: ", this.rank);
}

var fred =  new Player("Fred", 1000, 5);
fred.logInfo();
fred.promote();














