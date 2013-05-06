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
	<script>
		function setFaculty(){
			var collegeid = document.clazz.collegeid.value;
			var max = 5;
			% for info in infos:
			var collegeNum = ${info.collegeNum};
			% endfor
			var i = 0;
			var open = "option.college_"+collegeid.toString();
			var close = "";
			for (i=0;i<=collegeNum;i++)
			{
				close = "option.college_"+i.toString();
				$(close).hide();
			}
			$(open).show();
			document.clazz.facultyid.value = -1;
		}
		
		function setClazz(){
			var facultyid = document.clazz.facultyid.value;
			var max = 5;
			% for info in infos:
			var facultyNum = ${info.facultyNum};
			% endfor
			var i = 0;
			var open = "option.faculty_"+facultyid.toString();
			var close = "";
			for (i=0;i<=facultyNum;i++)
			{
				close = "option.faculty_"+i.toString();
				$(close).hide();
			}
			$(open).show();
			document.clazz.clazzid.value = -1;
		}
	</script>
</head>

<body>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
	<!-- 顶部固定栏 -->
    <!--<%include file="/main/head.mako" />-->
	<!-- 导航栏部分 -->
    <%include file="/main/nav_admin.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">班级管理</div>
			<!--form action="/clazz/list" class="search" name="clazz" method="post">
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:180px" name="collegeid" onchange="setFaculty();" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择学院--------</option>
						% for college in colleges:
						<option value="${college.id}">${college.name}</option>
						% endfor
					</select>
				</div>
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">专业</span>
  					<select class="span2" style="width:180px" name="facultyid" onchange="setClazz();" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
						% for faculty in facultys:
						<option value="${faculty.id}" class="college_${faculty.collegeid}" style="display:none;">${faculty.name}</option>
						% endfor
					</select>
				</div>
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">班级</span>
  					<select class="span2" style="width:180px" name="clazzid" onchange="document.all.clazz.submit();" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择班级--------</option>
						% for clazz in clazzs:
						<option value="${clazz.id}" class="faculty_${clazz.facultyid}" style="display:none;">${clazz.grade}级${clazz.num}班</option>
						% endfor
					</select>
				</div>
			</form-->
			<a class="btn btn-primary" id="btn_head" href="/clazz/list">返回班级主栏</a> 
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
            	<tr>     
        			<th colspan="4" >
        			<i class="icon-th-large"></i>
        			% for info in infos:
        			学院：${info.college} &nbsp;&nbsp;&nbsp;
        			专业：${info.faculty} &nbsp;&nbsp;&nbsp;
        			班级：${info.clazz} 
        			% endfor
        			<!--button class="btn btn-primary" style="float:right;"></button-->
        			</th>
      			</tr>
      			<tr>     
      				<th style="width:30px;text-align:center;"></th>
        			<th class="name">姓名</th>
        			<th class="stdn">学号</th>
        			<th class="app">操作</th>
      			</tr>
    		</thead>
            <tbody>
            	<form action="/clazz/del" name="clazz_del" method="post">
      			% for item in items:
      			<tr>
      				<td><input type="checkbox" name="student_${item.id}" value="${item.id}"></td>
        			<td class="name">${item.name}</td>
        			<td class="name">${item.identity}</td>
        			<td class="app">
        				<a class="btn btn-info" href="/student/add?fstudentid=${item.id}">编辑</a>
        				<a class="btn btn-danger" href="/student/del?studentid=${item.id}">删除</a>
        			</td>
      			</tr>
      			% endfor
      			<tr>
      				<td colspan="4" >
      				<!--a class="btn btn-danger" style="float:right;margin:0 15px;" href="/clazz/del?clazzid=${item.id}">删除全班学生</a-->
      				<input style="float:right;margin:0 15px;" type="submit" class="btn btn-danger" value="删除选中学生" />
      				</td>
      			</tr>
      			</form>
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
</body>
</html>