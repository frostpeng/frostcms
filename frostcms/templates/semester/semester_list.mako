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
			<div class="title_2">学期管理</div>
			<a class="btn btn-primary" id="btn_head" href="/semester/add"><i class="icon-plus icon-white"></i> 添加学期</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
      			<tr>     
        			<th class="name">学期</th>
        			<th class="stdn">开始日期</th>
        			<th class="stdn">总周数</th>
        			<th class="app">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">${item.name}</td>
        			<td class="name">${item.time}</td>
        			<td class="name">${item.weeks}</td>
        			<td class="app">
        				<a class="btn btn-info btn-mini" href="/semester/add?semesterid=${item.id}">编辑</a>
        				<a class="btn btn-danger btn-mini" onclick="delete_con('是否删除学期【${item.name}】？','/semester/del?semesterid=${item.id}');" >删除</a>
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