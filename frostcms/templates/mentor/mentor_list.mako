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
			<div class="title_2">教师管理</div>
			<form action="/mentor/list" class="search" name="college" method="post">
				按院系查询
				<select name="collegeid" size="1" onchange= "document.all.college.submit();">
					<option disabled="disabled" selected="selected" >--------请选择学院--------</option>
					% for li in lis:
					<option value="${li.id}" >${li.name}</option>
					% endfor
				</select>
			</form>
			<a class="btn btn-primary" id="btn_head" href="/mentor/add"><i class="icon-plus icon-white"></i> 添加教师</a> 
			<div class="search">
			<form enctype="multipart/form-data"  action="/mentor/upload" method="post">
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
        			<th class="name">姓名</th>
        			<th style="width:160px;text-align:center;">学院</th>
        			<th class="name">电话</th>
        			<th class="name_l" style="width:220px;" >mail</th>
        			<th class="app">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">${item.name}</td>
        			<td style="width:160px;text-align:center;">${item.college.name}</td>
        			<td class="name">${item.phone}</td>
        			<td class="name" style="width:220px;">${item.email}</td>
        			<td class="app">
        				<a class="btn btn-info btn-mini" href="/mentor/add?mentorid=${item.id}">详情与修改</a>
        				<a class="btn btn-danger btn-mini" href="/mentor/del?mentorid=${item.id}">删除</a>
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
