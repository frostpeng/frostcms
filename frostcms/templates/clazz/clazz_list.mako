<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
	<%include file="/unit/link_JS&CSS.mako" />
</head>

<body onload="searchGetCollege();">
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">班级管理</div>
			<form action="/clazz/list" class="search" name="clazz" method="post" >
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:180px" id="putCollegeBox" name="collegeid" onchange="searchGetFaculty(this);" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择学院--------</option>
					</select>
				</div>
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">专业</span>
  					<select class="span2" style="width:180px" id="putFacultyBox" name="facultyid" onchange="searchGetClazz(this);" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
					</select>
				</div>
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">班级</span>
  					<select class="span2" style="width:180px" id="putClazzBox" name="clazzid" onchange="document.all.clazz.submit();" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择班级--------</option>
					</select>
				</div>
			</form>
			<a class="btn btn-primary" id="btn_head" href="/clazz/add"><i class="icon-plus icon-white"></i> 添加班级</a> 
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
            	<tr>     
        			<th colspan="3" >
        			<i class="icon-th-large"></i>
        			% for info in infos:
        			学院：${info.college} &nbsp;&nbsp;&nbsp;
        			专业：${info.faculty} &nbsp;&nbsp;&nbsp;
        			班级：${info.clazz} 
        			% endfor
        			</th>
      			</tr>
      			<tr>     
      				<!--th style="width:30px;text-align:center;"></th-->
        			<th class="name">姓名</th>
        			<th class="stdn">学号</th>
        			<th class="app">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">${item.name}</td>
        			<td class="name">${item.identity}</td>
        			<td class="app">
        				<a class="btn btn-info" href="/student/add?studentid=${item.id}">编辑</a>
        				<a class="btn btn-danger" onclick="delete_con('是否删除学生【${item.identity}】','/student/del?studentid=${item.id}');">删除</a>
        			</td>
      			</tr>
      			% endfor
    		</tbody>
            </table>     
            <!-- 分页导航 -->         
        	<%include file="/unit/pagination.mako" />
    </div>
    <!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>