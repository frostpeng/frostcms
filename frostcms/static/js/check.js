//Checking infomations before form be submited
function putCheckOut(id,text){
	var box = document.getElementById(id);
	var out = document.createElement("span");
	box.innerHTML = "";
	out.setAttribute("class","checkOut");
	out.appendChild(document.createTextNode(text));
	box.appendChild(out);
}
function clrCheckOut(id){
	document.getElementById(id).innerHTML = "";
}

function checkLocationAdd(){
	var name = document.location['location.name'].value;
	var address = document.location['location.address'].value;
	var totalrows = document.location['location.totalrows'].value;
	var perrow = document.location['location.perrow'].value;
	var seatnum = document.location['location.seatnum'].value;
	var area = document.location['location.area'].value;
	var reg = new RegExp("^[0-9]*$");
	var rightNum = 0;
	if (name == "")
		putCheckOut("checkLocationName","实验室名称不能为空");
	else{
		++rightNum;
		clrCheckOut("checkLocationName");
	}
	
	if (address == "")
		putCheckOut("checkLocationAddress","地址不能为空");
	else{
		++rightNum;
		clrCheckOut("checkLocationAddress");
	}
	
	if (totalrows == "")
		putCheckOut("checkLocationTotalrows","排数不能为空");
	else{
		if (reg.test(totalrows)){
			++rightNum;
			clrCheckOut("checkLocationTotalrows");
		}
		else
			putCheckOut("checkLocationTotalrows","排数必须为'数字'");
	}
	
	if (perrow == "")
		putCheckOut("checkLocationPerrow","列数不能为空");
	else{
		if (reg.test(perrow)){
			++rightNum;
			clrCheckOut("checkLocationPerrow");
		}
		else 
			putCheckOut("checkLocationPerrow","列数必须为'数字'");
	}
	
	if (seatnum == "")
		putCheckOut("checkLocationSeatnum","总位数不能为空");
	else {
		if (reg.test(seatnum)){
			++rightNum;
			clrCheckOut("checkLocationSeatnum");
		}
		else 
			putCheckOut("checkLocationSeatnum","总位数必须为'数字'");
	}
	
	if (area == "-1")
		putCheckOut("checkLocationArea","未选择校区");
	else {
		++rightNum;
		clrCheckOut("checkLocationArea");
	}
	
	if (rightNum <6)
		return false;
	else{
		document.location.submit();
		return true;
	}
}

function checkMentorAdd(){
	var name = document.mentor["mentor.name"].value;
	var identity = document.mentor["mentor.identity"].value;
	var collegeid = document.mentor["mentor.collegeid"].value;
	var title = document.mentor["mentor.title"].value;
	var phone = document.mentor["mentor.phone"].value;
	var email = document.mentor["mentor.email"].value;
	var regNum = new RegExp("^[0-9]*$");
	var regWord = new RegExp("^\w+$");
	var regEmail = new RegExp("^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$");
	var rightNum = 0;
	
	if (name == "")
		putCheckOut("checkMentorName","姓名不能为空");
	else{
		++rightNum;
		clrCheckOut("checkMentorName");
	}
	
	if (identity == "")
		putCheckOut("checkMentorIdentity","教工号不能为空");
	else {
		if (regNum.test(identity)){
			++rightNum;
			clrCheckOut("checkMentorIdentity");
		}
		else 
			putCheckOut("checkMentorIdentity","教工号格式不正确");
	}
	
	if (collegeid == "-1")
		putCheckOut("checkMentorCollegeid","未选择学院");
	else {
		++rightNum;
		clrCheckOut("checkMentorCollegeid");
	}
	
	if (title == "")
		putCheckOut("checkMentorTitle","头衔不能为空");
	else{
		++rightNum;
		clrCheckOut("checkMentorTitle");
	}
	
	if (phone == "")
		putCheckOut("checkMentorPhone","教工号不能为空");
	else {
		if (regNum.test(identity)){
			++rightNum;
			clrCheckOut("checkMentorPhone");
		}
		else 
			putCheckOut("checkMentorPhone","电话号码只能由数字组成");
	}
	
	if (email == "")
		putCheckOut("checkMentorEmail","邮箱不能为空");
	else {
		if (regEmail.test(email)){
			++rightNum;
			clrCheckOut("checkMentorEmail");
		}
		else 
			putCheckOut("checkMentorEmail","电子邮箱格式不正确")
	}
	
	if (rightNum <6)
		return false;
	else{
		document.mentor.submit();
		return true;
	}
}

function checkSemesterAdd(){
	var start = document.semester["semester.start"].value;
	var weeks = document.semester["semester.weeks"].value;
	var regNum = new RegExp("^[0-9]*$");
	var rightNum = 0;
	
	if (start == "")
		putCheckOut("checkSemesterStart","未选择日期");
	else{
		++rightNum;
		clrCheckOut("checkSemesterStart");
	}
	
	if (weeks == "")
		putCheckOut("checkSemesterWeeks","周数不能为空");
	else {
		if (regNum.test(weeks)){
			++rightNum;
			clrCheckOut("checkSemesterWeeks");
		}
		else 
			putCheckOut("checkSemesterWeeks","周数只能含数字");			
	}
		
	if (rightNum <2)
		return false;
	else{
		document.semester.submit();
		return true;
	}
}

function checkStudentAdd(){
	var name = document.student["student.name"].value;
	var identity = document.student["student.identity"].value;
	var clazzid = document.student["student.clazzid"].value;
	var regWord = new RegExp("^[A-Za-z0-9]+$");
	var rightNum = 0;
	
	if (name == "")
		putCheckOut("checkStudentName","姓名不能为空");
	else{
		++rightNum;
		clrCheckOut("checkStudentName");
	}
	
	if (identity == "")
		putCheckOut("checkStudentIdentity","学号不能为空");
	else {
		if (regWord.test(identity)){
			++rightNum;
			clrCheckOut("checkStudentIdentity");
		}
		else 
			putCheckOut("checkStudentIdentity","学号号格式不正确");
	}
	
	if (clazzid == "-1")
		putCheckOut("checkStudentClazzid","未选择班级");
	else {
		++rightNum;
		clrCheckOut("checkStudentClazzid");
	}
	
	if (rightNum <3)
		return false;
	else{
		document.student.submit();
		return true;
	}
}

function checkCollegeAdd(){
	var name = document.college["college.name"].value;
	var rightNum = 0;
	
	if (name == "")
		putCheckOut("checkCollegeName","名称不能为空");
	else{
		++rightNum;
		clrCheckOut("checkCollegeName");
	}
	
	if (rightNum <1)
		return false;
	else{
		document.college.submit();
		return true;
	}
}

function checkFacultyAdd(){
	var name = document.faculty["faculty.name"].value;
	var collegeid = document.faculty["faculty.collegeid"].value;
	var rightNum = 0;
	
	if (name == "")
		putCheckOut("checkFacultyName","名称不能为空");
	else{
		++rightNum;
		clrCheckOut("checkFacultyName");
	}
	
	if (collegeid == "-1")
		putCheckOut("checkFacultyCollegeid","未选择学院");
	else {
		++rightNum;
		clrCheckOut("checkFacultyCollegeid");
	}
	
	if (rightNum <2)
		return false;
	else{
		document.faculty.submit();
		return true;
	}
}

function checkClazzAdd(){
	var facultyid = document.clazz["clazz.facultyid"].value;
	var year = document.clazz["clazz.year"].value;
	var num = document.clazz["clazz.num"].value;
	var mulfloat = document.clazz["clazz.mulfloat"].value;
	var regNum = new RegExp("^[0-9]*$");
	var rightNum = 0;
	
	if (facultyid == "-1")
		putCheckOut("checkClazzFacultyid","未选择专业");
	else {
		++rightNum;
		clrCheckOut("checkClazzFacultyid");
	}
	
	if (year == "")
		putCheckOut("checkClazzYear","年级不能为空");
	else {
		if (regNum.test(year)){
			++rightNum;
			clrCheckOut("checkClazzYear");
		}
		else 
			putCheckOut("checkClazzYear","年级只能含数字");			
	}
	
	if (num == "")
		putCheckOut("checkClazzNum","班号不能为空");
	else {
		if (regNum.test(num)){
			++rightNum;
			clrCheckOut("checkClazzNum");
		}
		else 
			putCheckOut("checkClazzNum","班号只能含数字");			
	}
	
	if (mulfloat == "")
		putCheckOut("checkClazzMulfloat","浮动率不能为空");
	else {
		if (regNum.test(mulfloat)){
			++rightNum;
			clrCheckOut("checkClazzMulfloat");
		}
		else 
			putCheckOut("checkClazzMulfloat","浮动率只能含数字");			
	}
	
	if (rightNum <4)
		return false;
	else{
		document.clazz.submit();
		return true;
	}
}

function checkCourseAdd(){
	var rightNum = 0;
	var name = document.course["course.name"].value;
	var mentorid = "";
	if (document.course["course.mentorid"]){
		mentorid = document.course["course.mentorid"].value;
		if (mentorid == "-1" || mentorid == "")
			putCheckOut("checkCourseMentorid","未选择教师");
		else {
			++rightNum;
			clrCheckOut("checkCourseMentorid");
		}
	}
	else
		++rightNum;
	var semesterid = document.course["course.semesterid"].value;
	var classes = document.getElementById("ClassListHave").innerHTML;
	classes = classes.replace(/\s+/g, "");
	classes = classes.replace(/<\/?.+?>/g,"");
	classes = classes.replace(/[\r\n]/g, ""); 
	
	if (name == "")
		putCheckOut("checkCourseName","名称不能为空");
	else{
		++rightNum;
		clrCheckOut("checkCourseName");
	}
	
	if (semesterid == "-1" || semesterid == "")
		putCheckOut("checkCourseSemesterid","未选择学期");
	else {
		++rightNum;
		clrCheckOut("checkCourseSemesterid");
	}
	
	if (classes == "")
		putCheckOut("checkCourseClazzes","未添加班级");
	else {
		++rightNum;
		clrCheckOut("checkCourseClazzes");
	}
	
	if (rightNum <4)
		return false;
	else{
		document.course.submit();
		return true;
	}
}

function checkLessonAdd(){
	var locations = document.getElementById("locationHave").innerHTML;
	locations = locations.replace(/\s+/g, "");
	locations = locations.replace(/<\/?.+?>/g,"");
	locations = locations.replace(/[\r\n]/g, ""); 
	if (locations == "")
		putCheckOut("checkLessonLocations","未添加实验室");
	else {
		clrCheckOut("checkLessonLocations");
		document.course.submit();
	}
}