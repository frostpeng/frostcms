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
    <script src="../../static/js/lesson.js"></script>
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
        	 	%if lesson:
        	 	<input type="hidden" name="lesson.id" value="${lesson.id}" />
        	 	%endif
        			%if course :
        			<input type="hidden" name="lesson.courseid" value="${course.id}"/>
        			
						<a class="btn btn-primary disabled"><i class="icon-book icon-white"></i> ${course.name}</a>
						<a class="btn disabled"><i class=" icon-user"></i> ${course.mentor.name}</a>
						<a class="btn btn-info disabled"><i class="icon-user icon-white"></i> 课堂总人数： ${studentnum}</a>
						<%! 
							import time
							from datetime import date	 
						%>
						<a class="btn btn-inverse disabled "><i class="icon-time icon-white"></i> ${date.fromtimestamp(course.semester.start).year}
						%if date.fromtimestamp(course.semester.start).month>7 :
							年秋季
						%else :
							年春季	
						%endif
						</a>
					%endif
				<br /><br />
				<div class="input-prepend">
  					<span class="add-on">周次</span>
  					%if lesson:
  					<input class="span2" id="checkWeek" type="text" name="lesson.week" value="${lesson.week}" onkeyup="checkTime()" placeholder="" />
  					%else:
  					<input class="span2" id="checkWeek" type="text" name="lesson.week" onkeyup="checkTime()" placeholder="" />
  					%endif
				</div>
				<span id="checkWeekRes" style="margin:0 10px;color:red;font-size:14px;line-height:24px;font-family:'微软雅黑','黑体';"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">星期</span>
  					<select class="span2" style="width:140px" name="lesson.dow" onchange="checkTime()" size="1" onchange="" >
						<option value="0" 
						% if lesson and lesson.dow == 0:
							selected="selected"
						% endif
						>星期日</option>
						<option value="1" 
						% if lesson and lesson.dow == 1:
							selected="selected"
						% endif
						>星期一</option>
						<option value="2"
						%if lesson and lesson.dow == 2:
							selected="selected"
						%endif
						 >星期二</option>
						<option value="3" 
						%if lesson and lesson.dow == 3:
							selected="selected"
						%endif
						>星期三</option>
						<option value="4" 
						%if lesson and lesson.dow == 4:
							selected="selected"
						%endif
						>星期四</option>
						<option value="5" 
						%if lesson and lesson.dow == 5:
							selected="selected"
						%endif
						>星期五</option>
						<option value="6" 
						%if lesson and lesson.dow == 6:
							selected="selected"
						%endif
						>星期六</option>
					</select>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">开始节数</span>
  					%if lesson:
  					<input class="span2" id="checkStarttime" type="text" name="lesson.starttime"  value="${lesson.start}" onkeyup="checkTime()" placeholder="" />
  					%else:
  					<input class="span2" id="checkStarttime" type="text" name="lesson.starttime" onkeyup="checkTime()" placeholder="" />
  					%endif
				</div>
				<span id="checkStarttimeRes" style="margin:0 10px;color:red;font-size:14px;line-height:24px;font-family:'微软雅黑','黑体';"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">结束节数</span>
  					%if lesson:
  					<input class="span2" id="checkEndtime" type="text" name="lesson.endtime" value="${lesson.end}"  onkeyup="checkTime()" placeholder="" />
  					%else:
  					<input class="span2" id="checkEndtime" type="text" name="lesson.endtime" onkeyup="checkTime()" placeholder="" />
  					%endif
				</div>
				<span id="checkEndtimeRes" style="margin:0 10px;color:red;font-size:14px;line-height:24px;font-family:'微软雅黑','黑体';"></span>
				
				<br /><hr />
				<div class="locationBox">
					<div class="locationSelect">
						<div class="locationSelectHead" style="text-align:left;"><i class="icon-th-large" style="margin:8px;float:left;"></i> 实验室(<span id="sNumHave">0</span>)</div>
						<div class="locationSelectContent">
						<span id="locationHave">
							%if lesson:
								% for lessonlocation in lesson.lessonlocations:
								<input type="text" name="locationid" id="location${lessonlocation.locationid}" id="location"value="${lessonlocation.locationid}" style="display:none;"/>
								<input type="text" name="studentnum" id="location${lessonlocation.locationid}" value="${lessonlocation.studentnum}" style="display:none;"/>
								<a class="btn btn-mini classBoxSingle"  id="location${lessonlocation.locationid}" onclick="deleteLocation(this.id);">${lessonlocation.location.name}:${lessonlocation.studentnum}人  <i class="icon-remove"></i></a>
								% endfor
							%endif
						</span>
						</div>
					</div>
					<div class="locationAdd">
						<div class="locationSelectHead">
						<a class="btn btn-mini btn-success" style="float:left;margin:3px;" onclick="addLocations()" ><i class="icon-chevron-left icon-white" style="margin:3px 0;"></i> 添加</a>	
						<span>
						% if course :
							需要(${studentnum})
						% endif 
						</span>
						<i class="icon-comment" style="float:right;margin:8px;"></i>
						</div>
						<div class="locationSelectContent">
						<span id="locationCan"></span>
						</div>
					</div>
				</div>
				<hr />
				<span id="debug"></span>
 				<button class="btn btn-primary" id="add_submit" type="submit"><i class="icon-ok icon-white"></i>  提交</button>
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>