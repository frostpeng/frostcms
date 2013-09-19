// for search faculty,calss in JavaScript
//获取学院列表
function addOptionCollege(college){
	var CollegeBox = document.getElementById("putCollegeBox");
	var option = document.createElement("option");
	option.setAttribute("value",college.id);
	option.appendChild(document.createTextNode(college.name));
	CollegeBox.appendChild(option);
}

function searchGetCollege(){
	var CollegeBox = document.getElementById("putCollegeBox");
	CollegeBox.innerHTML = "";
	var option = document.createElement("option");
	option.setAttribute("value","-1");
	option.setAttribute("disabled","disabled");
	option.setAttribute("selected","selected");
	option.appendChild(document.createTextNode("--------请选择学院--------"));
	CollegeBox.appendChild(option);
	$.ajax({
		url:"/api/college/list",
		type: "post",
		data: {},
		dataType: "json",
		success: function(data){
			for (var ix=0;ix<data.colleges.length;++ix)
				addOptionCollege(data.colleges[ix]);
		},
		error: function(data){
			alert("系统错误，请联系管理员");
		},
		complete: function(){
		}
	});
}

//根据学院，获取专业列表
function addOptionFaculty(faculty){
	var FacultyBox = document.getElementById("putFacultyBox");
	var option = document.createElement("option");
	option.setAttribute("value",faculty.id);
	option.setAttribute("id","faculty"+faculty.id);
	option.appendChild(document.createTextNode(faculty.name));
	FacultyBox.appendChild(option);
}

function searchGetFaculty(CollegeInput){
	var FacultyBox = document.getElementById("putFacultyBox");
	var CollegeId = CollegeInput.value;
	if (CollegeId != ""){
		FacultyBox.innerHTML = "";
		var option = document.createElement("option");
		option.setAttribute("value","-1");
		option.setAttribute("disabled","disabled");
		option.setAttribute("selected","selected");
		option.appendChild(document.createTextNode("--------请选择专业--------"));
		FacultyBox.appendChild(option);
		$.ajax({
			url:"/api/faculty/list",
			type: "post",
			data: {collegeid:CollegeId},
			dataType: "json",
			success: function(data){
				for (var ix=0;ix<data.faculties.length;++ix)
					addOptionFaculty(data.faculties[ix]);
			},
			error: function(data){
				alert("系统错误，请联系管理员");
			},
			complete: function(){
			}
		});
	}
}

//根据专业获取班级列表
function addOptionClazz(clazz){
	var ClazzBox = document.getElementById("putClazzBox");
	var option = document.createElement("option");
	option.setAttribute("value",clazz.id);
	option.setAttribute("id","class"+clazz.id);
	option.appendChild(document.createTextNode(clazz.year+"级"+clazz.num+"班"));
	ClazzBox.appendChild(option);
}

function searchGetClazz(FacultyInput){
	var ClazzBox = document.getElementById("putClazzBox");
	var FacultyId = FacultyInput.value;
	if (FacultyId != ""){
		ClazzBox.innerHTML = "";
		var option = document.createElement("option");
		option.setAttribute("value","-1");
		option.setAttribute("disabled","disabled");
		option.setAttribute("selected","selected");
		option.appendChild(document.createTextNode("--------请选择班级--------"));
		ClazzBox.appendChild(option);
		$.ajax({
			url:"/api/clazz/list",
			type: "post",
			data: {facultyid:FacultyId},
			dataType: "json",
			success: function(data){
				for (var ix=0;ix<data.clazzes.length;++ix)
					addOptionClazz(data.clazzes[ix]);
			},
			error: function(data){
				alert("系统错误，请联系管理员");
			},
			complete: function(){
			}
		});
	}
}