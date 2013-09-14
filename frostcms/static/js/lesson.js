//JavaScript for lesson
function checkEndtime(){
	var startTime = document.getElementById(("checkStarttime").getAttribute("value");
	var endTime = document.getElementById("checkEndtime").getAttribute("value");
	if (parseInt(endTime)<parseInt(startTime)){
		document.getElementById("checkEndtimeRes").innerHTML = "结束节数应大于等于开始节数";
	}
	else{
		document.getElementById("checkEndtimeRes").innerHTML = "test test " + startTime;
	}
}