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
			<div class="title_2">学生信息管理</div>
            
            <div class="search">
				<form class="form-search" action="/student/list" method="post">
				<div class="input-append">
				<input type="text" name="search_identity" class="span2 search-query" autocomplete="off" value="" />
				<input type="submit" name="submit" class="btn" autocomplete="off" value="按学号查询" />
				</div>
				</form>
			</div>	
			<a class="btn btn-primary" id="btn_head" href="/student/add" ><i class="icon-plus icon-white"></i> 添加新学生</a>
			
			<div class="search">
			<form enctype="multipart/form-data"  action="/student/upload" method="post">
			<div class="input-append">
				<input type="file"  accept="xls" style="vertical-align:middle;height:20px;width:220px;line-height:30px;margin:0;text-aligin:center;" class="btn" name="file"/>
				<input type="submit" name="submit" class="btn btn-primary" value="从xls文件导入" />
			</div>
			</form>
            </div>
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
      			<tr>
      				<th class="stdn">学号</th>
        			<th class="name">姓名</th>
        			<th class="name">年级</th>
        			<th class="app">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="stdn">${item.identity}</td>
        			<td class="name">${item.name}</td>
        			<td class="name">${item.clazz.year}</td>
        			<td class="app">
        			<a class="btn btn-info btn-mini" href="/student/add?studentid=${item.id}">修改学生信息</a>
        			<a class="btn btn-danger btn-mini" onclick="delete_con('是否删除学生【${item.name}】？','/student/del?studentid=${item.id}');" >删除</a>
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