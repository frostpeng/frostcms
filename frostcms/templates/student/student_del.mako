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
</head>

<body>
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
        	<form action="/student/del" class="add" name="student">
 				%if student:
 				<div class="app_name">
        		添加学生
        		</div>
        		<input type="hidden" name="student.id" value="${student.id}"/>
  				<div class="input-prepend">
  					<span class="add-on">姓名</span>
  					<input class="span2" style="width:220px;" readOnly="true" id="prependedInput" type="text" name="student.name" value="${student.name}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">学号</span>
  					<input class="span2" style="width:220px;" readOnly="true"  id="prependedInput" type="text" name="student.identity" value="${student.identity}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">学院</span>
  					<input class="span2" style="width:220px;" readOnly="true"  id="prependedInput" type="text" name="college" value="${student.clazz.faculty.college.name}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">专业</span>
  					<input class="span2" style="width:220px;" readOnly="true"  id="prependedInput" type="text" name="faculty" value="${student.clazz.faculty.name}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">班级</span>
  					<input class="span2" style="width:220px;" readOnly="true"  id="prependedInput" type="text" name="clazz" value="${student.clazz.grade}级${student.clazz.num}班" placeholder="" />
				</div>
				<br />
 				<button class="btn btn-danger" id="add_submit" type="submit">确认删除</button>
 				%endif
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>