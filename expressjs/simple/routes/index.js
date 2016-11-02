exports.index = function(req, res){
	res.render('default', {
			title: 'Home',
			classname: 'home',
			users: ['Mona', 'Ralf', 'Bob']
	});
}

exports.about = function(req, res) {
	res.render('default', {
			title: 'About Us',
			classname: 'about'
	});
}