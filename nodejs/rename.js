var fs = require('fs');

fs.renameSync("./libx/project-config.js", "./libx/config.json");

console.log("Config json file renamed");

fs.rename("./libx/notes.md", "./notes.md", function(err){
	
	if (err){
		console.log(err);
	}else{
		console.log("Nodes.md moved successfully.");
	}

});