//JavaScript for lesson

function addSingleBox(location){
	var Box = document.getElementById("locationCan");
	var singleBox = document.createElement("div");
	var title = document.createElement("div");
	var useNum = document.createElement("input");
	var canNum = document.createElement("div");
	var imgT = document.createElement("i");
	var imgN = document.createElement("i");
	
	//image title
	imgT.setAttribute("class","icon-share");
	imgT.setAttribute("style","margin:3px 0;");
	
	//image had student number
	imgN.setAttribute("class","icon-user");
	imgN.setAttribute("style","margin:3px 0;");
	
	//singleBox
	singleBox.setAttribute("class","singleLocationBox");
	
	//title
	title.setAttribute("class","singleLocationTitle");
	title.appendChild(imgT);
	title.appendChild(document.createTextNode(" "+location.name));
	
	//useNum
	useNum.setAttribute("class","singleLocationUse locationBox"+location.id);
	useNum.setAttribute("type","text");
	useNum.setAttribute("name","locationUse");
	useNum.setAttribute("placeholder",location.name);
	useNum.setAttribute("id",location.id);
	//useNum.setAttribute("value","0");
	
	//canNum
	canNum.setAttribute("class","singleLocationCan");
	canNum.appendChild(imgN);
	canNum.appendChild(document.createTextNode(" "+location.leftnum));
	
	singleBox.appendChild(title);
	singleBox.appendChild(canNum);
	singleBox.appendChild(useNum);
	
	Box.appendChild(singleBox);
}


//检查周次，开始节数与结束节数，如果正确，则提交给服务器
function checkTime(){
	var starttime = document.course["lesson.starttime"].value;
	var endtime = document.course["lesson.endtime"].value;
	var week = document.course["lesson.week"].value;
	var dow = document.course["lesson.dow"].value;
	if (week==""){
		document.getElementById("checkWeekRes").innerHTML = "！请输入周数！";
		return;
	}
	else{
		document.getElementById("checkWeekRes").innerHTML = "";
	}
	
	if (starttime==""){
		document.getElementById("checkStarttimeRes").innerHTML = "！请输入开始节数！";
		return;
	}
	else{
		document.getElementById("checkStarttimeRes").innerHTML = "";
	}
	
	if (parseInt(endtime)<parseInt(starttime)){
		document.getElementById("checkEndtimeRes").innerHTML = "！结束节数应大于等于开始节数！";
		return;
	}
	else{
		document.getElementById("checkEndtimeRes").innerHTML = "";
	}
	
	if (week!="" && starttime!="" && endtime!=""){
		/**var xmlhttp;
		if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp=new XMLHttpRequest();
		}
		else{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
	
		xmlhttp.open("GET","../api/location_studentnum/list?week="+week+"&dow="+dow+"&start="+starttime+"&end="+endtime,true);
		xmlhttp.send();
		xmlDoc=xmlhttp.responseXML;
		
		//应用列表：添加实验室
		document.getElementById("locationHave").innerHTML = "";
		document.getElementById("locationCan").innerHTML = "";
		
		var locations = xmlhttp.responseText;
		var location;
		for (location in locations)
			addSingleBox(location);
		**/
		document.getElementById("locationHave").innerHTML = "";
		document.getElementById("locationCan").innerHTML = "";
		 $.ajax({
				url:"../api/location_studentnum/list?week="+week+"&dow="+dow+"&start="+starttime+"&end="+endtime,
				type: "pos",
				data: {week:week,dow:dow,start:starttime,end:endtime},
				dataType: "json",
				success: function(data){
					for (var ix=0;ix<data.locations.length;++ix)
						addSingleBox(data.locations[ix]);
				},
				error: function(data){
					alert("系统错误，请联系管理员");
				},
				complete: function(){
				}
			});
	}
				
}

function addLocations(){
	document.getElementById("locationHave").innerHTML = "";
	var Box = document.getElementById("locationHave");
	var sNumHave = 0;
	var locationUse = document.getElementsByName("locationUse");
	for (var lx=0;lx<locationUse.length;++lx){
		var input_id = document.createElement("input");
		var input_num = document.createElement("input");
		var button = document.createElement("a");
		var imgT = document.createElement("i");
		
		if (document.course.locationUse[lx].value == "" || document.course.locationUse[lx].value== "0")
			continue;
		
		imgT.setAttribute("class","icon-remove");
		imgT.setAttribute("style","margin:3px 0;");
		
		input_id.setAttribute("name","locationid");
		input_id.setAttribute("id","location"+locationUse[lx].getAttribute("id"));
		input_id.setAttribute("value",locationUse[lx].getAttribute("id"));
		input_id.setAttribute("type","text");
		input_id.setAttribute("style","display:none;");
		
		input_num.setAttribute("name","studentnum");
		input_num.setAttribute("id","location"+locationUse[lx].getAttribute("id"));
		input_num.setAttribute("value",document.course.locationUse[lx].value);
		input_num.setAttribute("type","text");
		input_num.setAttribute("style","display:none;");
			
		button.setAttribute("id","location"+locationUse[lx].getAttribute("id"));
		button.setAttribute("class","btn");
		button.appendChild(document.createTextNode(locationUse[lx].getAttribute("placeholder")+" : "+ document.course.locationUse[lx].value + "人  "));
		button.setAttribute("onclick","deleteLocation(\"location"+locationUse[lx].getAttribute("id")+"\")");
		button.setAttribute("style","margin:5px 5px 0 0;");
		button.appendChild(imgT);
		
		Box.appendChild(input_id);
		Box.appendChild(input_num);
		Box.appendChild(button);
		
		sNumHave += parseInt(document.course.locationUse[lx].value);
	}
	document.getElementById("sNumHave").innerHTML = sNumHave.toString();
}

function deleteLocation(id){
	var Box = document.getElementById("locationHave");
	var beDel = document.getElementById(id);
	Box.removeChild(beDel);
	beDel = document.getElementById(id);
	Box.removeChild(beDel);
	beDel = document.getElementById(id);
	Box.removeChild(beDel);
}

function sumStudentNum(needNum){
	
}