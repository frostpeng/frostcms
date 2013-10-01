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
			<div class="title_2">课件添加 ： 
			% if course :
			${course.name}
			% endif
			</div>
			% if course :
			<a class="btn btn-primary" id="btn_head" href="/mentor/course/warelist?courseid=${course.id}">返回课件列表 : ${course.name}</a> 
			% endif
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/mentor/course/warasave" class="" name="course_ware">
        	<table class="table table-bordered table-hover table-condensed" id="main_table">
            <thead>
      			<tr>     
      				<th class="name"></th>
        			<th class="name">课件名</th>
        			<th class="name">课件描述</th>
        			<th class="app">上传时间</th>
      			</tr>
    		</thead>
            <tbody>
            		<%! 
							import time
							from datetime import datetime
					%>
      			% for item in items:
      			<tr>
      				<td class="name">
      				<input type="checkbox" id="inlineCheckbox1" name="addwares" value="${item.id}">
      				</td>
        			<td class="name">${item.title}</td>
        			<td class="name">
        			${item.description}
        			</td>
        			<td class="app">
        			${datetime.fromtimestamp(item.createtime).year}-${datetime.fromtimestamp(item.createtime).month}-${datetime.fromtimestamp(item.createtime).day}
        			&nbsp;
        			${datetime.fromtimestamp(item.createtime).hour}:${datetime.fromtimestamp(item.createtime).minute}:${datetime.fromtimestamp(item.createtime).second}
        			</td>
      			</tr>
      			% endfor
      			<tr>
      				<td colspan="4">
      				% if course: 
      				<input  type="hidden" name="courseid" value="${course.id}" />
      				% endif
      				<input type="submit" class="btn btn-primary" value="添加" />
      				</td>
      			</tr>
    		</tbody>
            </table>
            </form>
            <!-- 分页导航 -->         
        	<%include file="/unit/pagination.mako" />
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>