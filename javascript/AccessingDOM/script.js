/*
var mainTitle = document.getElementById("mainTitle");
console.log("type:", mainTitle.nodeType);
console.log("the Inner HTML is ", mainTitle.innerHTML);
console.log("Child nodes: ", mainTitle.childNodes.length);

var myLinks = document.getElementsByTagName("a");
console.log("Links: ", myLinks.length);

var mainContent = document.getElementById("mainContent");
mainContent.setAttribute("align", "right");

var sidebar = document.getElementById("sidebar");
//console.log("the Inner HTML is ", sidebar.innerHTML);


//create new element
var newHeading = document.createElement("h1");
var newParagraph = document.createElement("p");

//newHeading.innerHTML = "Did you know?";
//newParagraph.innerHTML = "California produces over 17 million gallons of wine each year!";

var h1Text = document.createTextNode("Did you know?");
var paraText = document.createTextNode("California produces over 17 million gallons of wine each year!");
newHeading.appendChild(h1Text);
newParagraph.appendChild(paraText);

document.getElementById("trivia").appendChild(newHeading);
document.getElementById("trivia").appendChild(newParagraph);


//handling Events 
document.onclick = function(){
	alert("You click something!");
};
*/

/*
function prepareEventHandlers() {
	var myImage = document.getElementById("mainImage");
	myImage.onclick = function() {
		alert("You click an image");
	};
}

window.onload = function(){
	prepareEventHandlers();
};
*/

//onfocus vs onblur
var emailField = document.getElementById("email");

emailField.onfocus = function() {
	if (emailField.value == "your email") {
		emailField.value = "";
	}
};

emailField.onblur = function(){
	if (emailField.value == "") {
		emailField.value = "your email";
	}

};












