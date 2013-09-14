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
			<div class="title_2">课堂管理</div>
			% if course:
			<a class="btn btn-primary" id="btn_head" href="/lesson/listbycourse?courseid=${course.id}"><i class="icon-share-alt icon-white"></i> 课堂列表</a>   			
			% endif
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/lesson/save" class="add" name="course">
        			% if course :
						<a class="btn btn-primary disabled"><i class="icon-book icon-white"></i> ${course.name}</a>
						<a class="btn disabled"><i class=" icon-user"></i> ${course.mentor.name}</a>
						<%! 
							import time
							from datetime import date
							
							 
						%>
						<a class="btn btn-inverse disabled "><i class="icon-time icon-white"></i> ${date.fromtimestamp(course.semester.start).year}
						% if date.fromtimestamp(course.semester.start).month>7 :
							年秋季
						% else :
							年春季	
						% endif
						</a>
					% endif
				<br /><br />
				<div class="input-prepend">
  					<span class="add-on">周次</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.week" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">星期</span>
  					<select class="span2" style="width:140px" name="lesson.dow" size="1" onchange="" >
						<option value="0" >星期日</option>
						<option value="1" 
						
						>星期一</option>
						<option value="2" 
						
						>星期二</option>
						<option value="3" 
						
						>星期三</option>
						<option value="4" 
						
						>星期四</option>
						<option value="5" 
						
						>星期五</option>
						<option value="6" 
						
						>星期六</option>
					</select>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">开始节数</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.starttime"  placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">结束节数</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.endtime" placeholder="" />
				</div>
				
				
				<br /><hr />
 				<button class="btn btn-primary" id="add_submit" type="submit"><i class="icon-ok icon-white"></i>  提交</button>
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>