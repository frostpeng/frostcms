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
			<div class="title_2">课件管理 ：
			% if course :
			${course.name}
			% endif
			</div>
			<a class="btn btn-primary" id="btn_head" href="/mentor/course/list">返回课程列表</a>
			% if course:
			<a class="btn btn-primary" id="btn_head" href="/mentor/course/waraadd?courseid=${course.id}">添加课件到课程</a>
			% endif
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover table-condensed" id="main_table">
            <thead>
      			<tr>     
        			<th class="name">课件名</th>
        			<th class="name">教师</th>
        			<th class="name">课件描述</th>
        			<th class="app">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">${item.title}</td>
        			<td class="name">${item.mentor.name}</td>
        			<td class="name">
        			${item.description}
        			</td>
        			<td class="app">
        			<a class="btn btn-info btn-mini" href="/user/getfilebyid?fsfileid=${item.fsfileid}">下载</a>
        			<a class="btn btn-danger btn-mini" onclick="delete_con('是否从课程中删除删除课件【${item.title}】?','/mentor/course/waradel?wareid=${item.id}&courseid=${course.id}');">从课程中删除</a>
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