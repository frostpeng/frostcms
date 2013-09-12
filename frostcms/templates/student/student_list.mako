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
</head>

<body>
	<!-- 导航栏部分 -->
    <%include file="/main/nav_admin.mako" />
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
			<a class="btn btn-primary" id="btn_head" href="/student/add" >添加新学生</a>
			
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
        			<a class="btn btn-info" href="/student/add?studentid=${item.id}">修改学生信息</a>
        			<a class="btn btn-danger" href="/student/del?studentid=${item.id}">删除</a>
        			</td>
      			</tr>
      			% endfor
    		</tbody>
            </table>
            <div class="right_foot">
            	<div class="pagination">
                <ul>
          	 		% if items.first_page:
	          		<li><a href="?page=${items.first_page}" title="第一页">&laquo; 第一页</a></li>
	         		% endif
	         		 % if items.previous_page:
	          		<li><a href="?page=${items.previous_page}" title="上一页">&laquo; 上一页</a></li>
	          		% endif
	         		% for i in range(items.page - 3,items.page):
			  		% if items.page_count>0 and i>=items.first_page:
					<li><a href="?page=${i}" class="number" title="${i}">${i}</a></li>
					% endif
			  		% endfor
	          		<li><a href="#" class="number current" title="${items.page}">${items.page}</a></li> 
	          		% for i in range(items.page+1, items.page + 3):
			  			% if items.page_count>0 and i<=items.last_page:
						<li><a href="?page=${i}" class="number" title="${i}"> ${i} </a></li>
			  			% endif
			 		% endfor
			  		% if items.next_page:
			  		<li><a href="?page=${items.next_page}" title="下一页">下一页 &raquo;</a></li>
			  		% endif
			  		% if items.last_page:
	          		<li><a href="?page=${items.last_page}" title="最后一页">最后一页 &raquo;</a></li> 
	          		% endif
          		</ul>
            	</div>
            </div>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>