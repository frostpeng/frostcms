<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
</head>

<body onload="searchGetCollege();">
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">课程管理</div>
			<a class="btn btn-primary" id="btn_head" href="/course/list"><i class="icon-share-alt icon-white"></i> 课程列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/course/save" class="add" name="student">
 				%if course:
 				<div class="app_name">
        		课程信息/编辑
        		</div>
 				<input type="hidden" name="course.id" value="${course.id}"/>
 				<div class="input-prepend">
  					<span class="add-on">课程名称</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="course.name" value="${course.name}"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">教师</span>
  					<select class="span2" style="width:200px" name="course.mentorid" size="1">
						<option disabled="disabled" >--------请选择教师--------</option>
						% for li in mentordictionary:
						<option value="${li.id}" 
							% if course.mentorid == li.id :
								selected="selected"
							% endif
						>${li.name}</option>
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学期</span>
  					<select class="span2" style="width:200px" name="course.semesterid" size="1">
						<option disabled="disabled">--------请选择学期--------</option>
						% for li in lis:
						<option value="${li.id}" 
							% if course.semesterid == li.id :
								selected="selected"
							% endif
							>${li.name}</option>
						% endfor
					</select>
				</div>
				<div class="dClassBox">
					<span id="dClassBox"></span>
				</div>
				<div class="ClassBox">
					<div class="ClassBoxLeft">
						<div class="ClassBoxLeftHead">班级</div>
						<div class="classBoxLeftContent">
						<span id="ClassListHave">
						% for cic in ClassInCourse:
							<input type="text" id="sign${cic.clazzid}" name="clazzid" value="${cic.clazzid}" style="display:none;"/>
							<a class="btn btn-mini classBoxSingle" id="sign${cic.clazzid}" onclick="deleteClass(this.id);">${cic.clazz.faculty.name} ${cic.clazz.year}级${cic.clazz.num}班   <i class="icon-remove"></i></a>
						% endfor
						</span>
						</div>
					</div>
					<div class="ClassBoxRight">
						<div class="ClassBoxLeftHead"><i class="icon-circle-arrow-left" style="margin:5px 0;"></i>添加班级</div>
						<br /><br />
						<div class="input-prepend"  id="add_adress">
  							<span class="add-on">学院</span>
  							<select class="span2" style="width:180px" id="putCollegeBox" name="collegeid" onchange="searchGetFaculty(this);" >
								<option disabled="disabled" selected="selected" value="-1">--------请选择学院--------</option>
							</select>
						</div>
						<br />
						<div class="input-prepend"  id="add_adress">
  							<span class="add-on">专业</span>
  							<select class="span2" id="putFacultyBox" style="width:180px" name="facultyid" onchange="searchGetClazz(this);" >
								<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
							</select>
						</div>
						<br />
						<div class="input-prepend"  id="add_adress">
  							<span class="add-on">班级</span>
  							<select class="span2" id="putClazzBox" style="width:180px" name="clazzbox" onchange="addClass(this.value,document.student.facultyid.value)">
								<option disabled="disabled" selected="selected" value="-1">--------请选择班级--------</option>
							</select>
						</div>
					</div>
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">保存</button>
 				%else:
 				<div class="app_name">
        		添加课程
        		</div>
        		<div class="input-prepend">
  					<span class="add-on">课程名称</span>
  					<input class="span2" id="prependedInput" type="text" name="course.name" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">教师</span>
  					<select class="span2" style="width:200px" name="course.mentorid" size="1" >
						<option disabled="disabled" selected="selected" >--------请选择教师--------</option>
						% for li in mentordictionary:
						<option value="${li.id}" >${li.name}</option>
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">学期</span>
  					<select class="span2" style="width:200px" name="course.semesterid" size="1" onchange="" >
						<option disabled="disabled" selected="selected" >--------请选择学期--------</option>
						% for li in lis:
						<option value="${li.id}" >${li.name}</option>
						% endfor
					</select>
				</div>
				<br />
				<!--
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">班级</span>
  					<input class="btn btn-blue" style="display:none;" id="classlist" type="text" placeholder="" onkeyup=""/>
  					<a class="btn btn-info" onclick="showClassBox()"><<添加班级</a>
					<table>
						<tr>
							<td>班级</td>
						</tr>
					</table>
				</div>
				-->
				<div class="dClassBox">
					<span id="dClassBox"></span>
				</div>
				<div class="ClassBox">
					<div class="ClassBoxLeft">
						<div class="ClassBoxLeftHead">班级</div>
						<div class="classBoxLeftContent">
						<span id="ClassListHave"></span>
						</div>
					</div>
					<div class="ClassBoxRight">
						<div class="ClassBoxLeftHead"><i class="icon-circle-arrow-left" style="margin:5px 0;"></i>添加班级</div>
						<br /><br />
						<div class="input-prepend"  id="add_adress">
  							<span class="add-on">学院</span>
  							<select class="span2" style="width:180px" id="putCollegeBox" name="collegeid" onchange="searchGetFaculty(this);" >
								<option disabled="disabled" selected="selected" value="-1">--------请选择学院--------</option>
							</select>
						</div>
						<br />
						<div class="input-prepend"  id="add_adress">
  							<span class="add-on">专业</span>
  							<select class="span2" id="putFacultyBox" style="width:180px" name="facultyid" onchange="searchGetClazz(this);" >
								<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
							</select>
						</div>
						<br />
						<div class="input-prepend"  id="add_adress">
  							<span class="add-on">班级</span>
  							<select class="span2" id="putClazzBox" style="width:180px" name="clazzbox" onchange="addClass(this.value,document.student.facultyid.value)">
								<option disabled="disabled" selected="selected" value="-1">--------请选择班级--------</option>
							</select>
						</div>
					</div>
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">提交</button>
 				%endif
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
<script type="text/javascript">
		function addMoreYh() {
		
	}
</script>
</html>