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
			<div class="title_2">作业管理</div>
			<form action="/mentor/assignment/list" name="assignment" class="search"  method="post">
				按课程查询
				<select name="collegeid" size="1" onchange= "document.all.assignment.submit();">
					<option disabled="disabled" selected="selected" >--------请选择课程--------</option>
					% for li in courses:
					<option value="${li.id}" >${li.name}</option>
					% endfor
				</select>
			</form> 
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
      			<tr>     
        			<th class="name">标题</th>
        			<th class="name">到期时间</th>
        			<th class="name">课程名称</th>
        			<th class="name">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">${item[0].title}</td>
        			<td class="name">${item[0].duedate}</td>
        			<td class="name"><a href='/mentor/lesson/listbycourse?courseid=${item[1].course.id}'>${item[1].course.name}</td>
        			<td class="name">
        			<a class="btn btn-info" href='/user/getfilebyid?fsfileid=${item[0].fsfileid}'>附件下载</a>
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