<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
	<script>
		function setFaculty(){
			var collegeid = document.student.collegeid.value;
			% for info in infos:
			var collegeNum = ${info.collegeNum};
			% endfor
			var i = 0;
			var open = "option.college_"+collegeid.toString();
			var close = "";
			for (i=0;i<=collegeNum;i++)
			{
				close = "option.college_"+i.toString();
				$(close).hide();
			}
			$(open).show();
			document.student.facultyid.value = -1;
		}
		
		function setClazz(){
			var facultyid = document.student.facultyid.value;
			% for info in infos:
			var facultyNum = ${info.facultyNum};
			% endfor
			var i = 0;
			var open = "option.faculty_"+facultyid.toString();
			var close = "";
			for (i=0;i<=facultyNum;i++)
			{
				close = "option.faculty_"+i.toString();
				$(close).hide();
			}
			$(open).show();
			document.student.clazzid.value = -1;
		}
	</script>
</head>
<body
% if not student:
onload="searchGetCollege();"
% endif
>
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">学生管理</div>
			<a class="btn btn-primary" id="btn_head" href="/student/list"><i class="icon-share-alt icon-white"></i> 学生列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/student/save" class="add" name="student">
 				%if student:
 				<div class="app_name">
        		添加学生
        		</div>
        		<input type="hidden" name="student.id" value="${student.id}"/>
  				<div class="input-prepend">
  					<span class="add-on">姓名</span>
  					<input class="span2" id="prependedInput" type="text" name="student.name" value="${student.name}" placeholder="" />
				</div>
				<span id="checkStudentName"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">学号</span>
  					<input class="span2" id="prependedInput" type="text" name="student.identity" value="${student.identity}" placeholder="" />
				</div>
				<span id="checkStudentIdentity"></span>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:180px" id="putCollegeBox" name="collegeid" onchange="searchGetFaculty(this);" onfocus="searchGetCollege();">
						<option selected="selected" value="${student.clazz.faculty.college.id}">${student.clazz.faculty.college.name}</option>
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">专业</span>
  					<select class="span2" style="width:180px" id="putFacultyBox" name="facultyid" onchange="searchGetClazz(this);" >
						<option selected="selected" value="${student.clazz.faculty.id}">${student.clazz.faculty.name}</option>
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">班级</span>
  					<select class="span2" style="width:180px" id="putClazzBox" name="student.clazzid" onload="" >
						<option selected="selected" value="${student.clazz.id}">${student.clazz.year}级${student.clazz.num}班</option>
					</select>
				</div>
				<span id="checkStudentClazzid"></span>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="button" onclick="checkStudentAdd();">保存</button>
 				%else:
 				<div class="app_name">
        		添加学生
        		</div>
  				<div class="input-prepend">
  					<span class="add-on">姓名</span>
  					<input class="span2" id="prependedInput" type="text" name="student.name" placeholder="" />
				</div>
				<span id="checkStudentName"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">学号</span>
  					<input class="span2" id="prependedInput" type="text" name="student.identity" placeholder="" />
				</div>
				<span id="checkStudentIdentity"></span>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:180px" id="putCollegeBox" name="collegeid" onchange="searchGetFaculty(this);" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择学院--------</option>
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">专业</span>
  					<select class="span2" style="width:180px" id="putFacultyBox" name="facultyid" onchange="searchGetClazz(this);" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">班级</span>
  					<select class="span2" style="width:180px" id="putClazzBox" name="student.clazzid" onchange="" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择班级--------</option>
					</select>
				</div>
				<span id="checkStudentClazzid"></span>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="button" onclick="checkStudentAdd();">提交</button>
 				%endif
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>