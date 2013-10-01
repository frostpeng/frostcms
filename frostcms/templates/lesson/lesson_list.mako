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
			<form action="/lesson/list" class="search" name="college" method="post">
				按学期查询
				<select name="collegeid" size="1" onchange= "document.all.college.submit();">
					<option disabled="disabled" selected="selected" >--------请选择学期--------</option>
					% for li in lis:
					<option value="${li.id}" >${li.name}</option>
					% endfor
				</select>
			</form>
			<a class="btn btn-primary" id="btn_head" href="/lesson/add"><i class="icon-plus icon-white"></i> 添加课堂</a> 
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
      			<tr>     
        			<th class="name">周数</th>
        			<th class="name">天数</th>
        			<th class="name_l">开始节数</th>
        			<th class="name">结束节数</th>
        			<th class="app">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">item.week</td>
        			<td class="name">item.dow</td>
        			<td class="name_l">item.start</td>
        			<td class="name">item.end</td>
        			<td class="app">
        				<a class="btn btn-danger btn-mini" onclick="delete_con('是否删除该课堂？','/lesson/del?lessonid=${item.id}');" >删除</a>
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