var fs = require('fs');

if (fs.existsSync("libx")){

	console.log("Directory already exists");
	
} else {

	fs.mkdir("libx", function(err){

	if (err){
		console.log(err);
	} else {
		console.log("Directory Created ...");
	}

});

}

