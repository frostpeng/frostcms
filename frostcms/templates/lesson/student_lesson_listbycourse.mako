<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
</head>

<body>
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">课堂管理</div>	
			
			<a class="btn btn-primary" id="btn_head" href="Javascript:history.back()"><i class="icon-share-alt icon-white"></i>返回</a>
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
            	<tr>
            		<th colspan="6">
            		% if course :
						<a class="btn btn-primary disabled" style="margin:0 0 8px 0;"><i class="icon-book icon-white"></i> ${course.name}</a>
						<a class="btn disabled" style="margin:0 0 8px 5px;"><i class=" icon-user"></i> ${course.mentor.name}</a>
						<%! 
							import time
							from datetime import date 
						%>
						<a class="btn btn-inverse disabled " style="float:right;margin:0 0 8px 0;"><i class="icon-time icon-white"></i> ${date.fromtimestamp(course.semester.start).year}
						% if date.fromtimestamp(course.semester.start).month>7 :
							年秋季
						% else :
							年春季	
						% endif
						</a>
						<br />
						<a class="btn btn-info disabled" style="margin:5px 5px 0 0;"><i class="icon-tags icon-white"></i> 班级</a>
						% for aclazz in course.course_classes :
							<a class="btn disabled" style="margin:5px 0 0 0;"><i class="icon-tag"></i> ${aclazz.clazz.faculty.name} ${aclazz.clazz.year}(${aclazz.clazz.num})班</a>
						% endfor
					% endif
            		</th>
            	</tr>
      			<tr>     
        			<th class="name">周数</th>
        			<th class="name">星期</th>
        			<th class="name">开始节数</th>
        			<th class="name">结束节数</th>
        			<th class="name_l">教室安排</th>
        			<th class="name">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">${item.week}</td>
        			<td class="name">
        			% if item.dow == 0 :
        			日
        			% elif item.dow == 1:
        			一
        			% elif item.dow == 2:
        			二
        			% elif item.dow == 3:
        			三
        			% elif item.dow == 4:
        			四
        			% elif item.dow == 5:
        			五
        			% elif item.dow == 6:
        			六
        			% endif
        			</td>
        			<td class="name">${item.start}</td>
        			<td class="name">${item.end}</td>
        			<td class="name">
        			% for lessonlocation in item.lesson_locations:
        				${lessonlocation.location.name}—${lessonlocation.studentnum}人
        				<br/>
        			%endfor
        			</td>
        			<td class="name">
        			%if item.assignmentid:
        			<a class="btn btn-info" href='/student/assignment/detail?assignmentid=${item.assignmentid}'>查看作业</a>
        			%else:
        			暂无作业
        			%endif
        			</td>
      			</tr>
      			% endfor
    		</tbody>
            </table>
            <!-- 分页导航 -->         
        	<%include file="/unit/pagination.mako" />
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>