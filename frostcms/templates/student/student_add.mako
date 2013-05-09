<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <link href="../../static/css/bootstrap.css" rel="stylesheet" media="screen"/>
    <link href="../../static/css/ccms.css" rel="stylesheet" media="screen"/>
    <script src="../../static/js/bootstrap.js"></script>
    <script src="../../static/js/jquery.js"></script>
    <script src="../../static/js/ccms.js"></script>
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

<body>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
	<!-- 顶部固定栏 -->
    <!--<%include file="/main/head.mako" />-->
	<!-- 导航栏部分 -->
    <%include file="/main/nav_admin.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">学生管理</div>
			<a class="btn btn-primary" id="btn_head" href="/student/list">返回学生列表</a>   
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
				<br />
				<div class="input-prepend">
  					<span class="add-on">学号</span>
  					<input class="span2" id="prependedInput" type="text" name="student.identity" value="${student.identity}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:180px" name="collegeid" onchange="setFaculty();" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择学院--------</option>
						% for college in colleges:
						<option value="${college.id}" 
						%if college.id == student.clazz.faculty.collegeid :
						selected="selected"
						%endif
						>${college.name}</option>
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">专业</span>
  					<select class="span2" style="width:180px" name="facultyid" onchange="setClazz();" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
						% for faculty in facultys:
						<option value="${faculty.id}" class="college_${faculty.collegeid}" style="display:none;"
						%if faculty.id == student.clazz.facultyid :
						selected="selected"
						%endif
						>${faculty.name}</option>
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">班级</span>
  					<select class="span2" style="width:180px" name="clazzid" onchange="" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择班级--------</option>
						% for clazz in clazzs:
							% if clazz.id == student.clazzid :
							<option value="${clazz.id}" class="faculty_${clazz.facultyid}" selected="selected">${clazz.grade}级${clazz.num}班</option>
							% else :
							<option value="${clazz.id}" class="faculty_${clazz.facultyid}" style="display:none;">${clazz.grade}级${clazz.num}班</option>
							% endif
						% endfor
					</select>
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">保存</button>
 				%else:
 				<div class="app_name">
        		添加学生
        		</div>
  				<div class="input-prepend">
  					<span class="add-on">姓名</span>
  					<input class="span2" id="prependedInput" type="text" name="student.name" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">学号</span>
  					<input class="span2" id="prependedInput" type="text" name="student.identity" placeholder="" />
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:180px" name="collegeid" onchange="setFaculty();" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择学院--------</option>
						% for college in colleges:
						<option value="${college.id}">${college.name}</option>
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">专业</span>
  					<select class="span2" style="width:180px" name="facultyid" onchange="setClazz();" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
						% for faculty in facultys:
						<option value="${faculty.id}" class="college_${faculty.collegeid}" style="display:none;">${faculty.name}</option>
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">班级</span>
  					<select class="span2" style="width:180px" name="clazzid" onchange="" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择班级--------</option>
						% for clazz in clazzs:
						<option value="${clazz.id}" class="faculty_${clazz.facultyid}" style="display:none;">${clazz.grade}级${clazz.num}班</option>
						% endfor
					</select>
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">提交</button>
 				%endif
 			</form>
        </div>               
        
    </div>
</body>
</html>