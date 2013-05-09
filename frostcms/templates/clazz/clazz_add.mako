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
			var collegeid = document.clazz.collegeid.value;
			var max = 5;
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
			document.clazz.facultyid.value = -1;
		}
		
		function setClazz(){
			var facultyid = document.clazz.facultyid.value;
			var max = 5;
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
			document.clazz.clazzid.value = -1;
		}
	</script>
</head>

<body>
	<!-- 导航栏部分 -->
    <%include file="/main/nav_admin.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">专业管理</div>
			<a class="btn btn-primary" id="btn_head" href="/clazz/list">返回班级主栏</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/clazz/save" class="add" name="clazz" method="post">
 				<div class="app_name">
        		添加班级
        		</div>
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
  					<select class="span2" style="width:180px" name="facultyid" onchange="" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
						% for faculty in facultys:
						<option value="${faculty.id}" class="college_${faculty.collegeid}" style="display:none;">${faculty.name}</option>
						% endfor
					</select>
				</div>
				<br />
 				<div class="input-prepend">
  					<span class="add-on">年级</span>
  					<select class="span2" style="width:180px" name="grade" onchange="" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择年级--------</option>
						% for grade in range(time.year-4,time.year+5):
						<option value="${grade}">${grade}</option>
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">班号</span>
  					<input class="span2" id="prependedInput" type="text" name="num" placeholder="请输入班级号">
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">提交</button>
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>