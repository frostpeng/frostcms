// JavaScript Document for course add
var classname = "";
function showClassBox(){
	var HtmlClassBox = "";
	document.getElementById("ClassBox").innerHTML = HtmlClassBox;
}

function deleteClass(id){
	var dClassBox = document.getElementById("ClassListHave");
	var beDel = document.getElementById(id);
	dClassBox.removeChild(beDel);
	beDel = document.getElementById(id);
	dClassBox.removeChild(beDel);
}

function changeName(str){
	classname = str;
}

function addClass(classid,facultyid){
	var dClassBox = document.getElementById("ClassListHave");
	var aClass = document.createElement("input");
	var aClassButton = document.createElement("a");
	var aIm = document.createElement("i");
	
	if (document.getElementById("sign"+classid)){
		
	}
	else {
		var className = document.getElementById("faculty"+facultyid).innerHTML+" "+document.getElementById("class"+classid).innerHTML;
		aClass.setAttribute("type","text");   
		aClass.setAttribute("id","sign"+classid);   
		aClass.setAttribute("name","clazzid");   
		aClass.setAttribute("value",classid);
		aClass.setAttribute("style","display:none;");
		
		aIm.setAttribute("class","icon-remove");
		aClassButton.appendChild(document.createTextNode(className+"   "));
		aClassButton.appendChild(aIm);
		aClassButton.setAttribute("class","btn btn-mini classBoxSingle");
		aClassButton.setAttribute("id","sign"+classid); 
		aClassButton.setAttribute("onclick","deleteClass(this.id);");
	
		
	
		dClassBox.appendChild(aClass);
		dClassBox.appendChild(aClassButton);
	}
	//document.getElementById("ClassBoxHave").innerHTML = document.getElementById("dClassBoxHave").innerHTML;
	//document.getElementById("ClassListHave").innerHTML = "have done";
}
