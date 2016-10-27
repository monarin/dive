var fs = require('fs');

try {
	fs.unlinkSync("./libx/config.json");
} catch (err) {
	console.log(err)
}

fs.unlink("notes.md", function(err){
	if (err){
		console.log(err);
	} else {
		console.log("Nodes.md removed");
	}
});

