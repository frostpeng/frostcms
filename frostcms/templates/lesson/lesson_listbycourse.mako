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
			<div class="title_2">课堂管理</div>	
			% if course:	
			<a class="btn btn-primary" id="btn_head" href="/lesson/addtocourse?courseid=${course.id}"><i class="icon-plus icon-white"></i> 添加课堂</a>
			% endif
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
            	<tr>
            		<th colspan="6">
            		% if course :
						<a class="btn btn-primary disabled" style="margin:0 0 8px 0;"><i class="icon-book icon-white"></i> ${course.name}</a>
						<a class="btn disabled" style="margin:0 0 8px 5px;"><i class=" icon-user"></i> ${course.mentor.name}</a>
						<%! 
							import time
							from datetime import date 
						%>
						<a class="btn btn-inverse disabled " style="float:right;margin:0 0 8px 0;"><i class="icon-time icon-white"></i> ${date.fromtimestamp(course.semester.start).year}
						% if date.fromtimestamp(course.semester.start).month>7 :
							年秋季
						% else :
							年春季	
						% endif
						</a>
						<br />
						<a class="btn btn-info disabled" style="margin:5px 5px 0 0;"><i class="icon-tags icon-white"></i> 班级</a>
						% for aclazz in course.course_classes :
							<a class="btn disabled" style="margin:5px 0 0 0;"><i class="icon-tag"></i> ${aclazz.clazz.faculty.name} ${aclazz.clazz.year}(${aclazz.clazz.num})班</a>
						% endfor
					% endif
            		</th>
            	</tr>
      			<tr>     
        			<th class="name">周数</th>
        			<th class="name">天数</th>
        			<th class="name">开始节数</th>
        			<th class="name">结束节数</th>
        			<th class="name_l">教室安排</th>
        			<th class="name">状态</th>
        			<th class="name_l">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">${item.week}</td>
        			<td class="name">${item.dow+1}</td>
        			<td class="name">${item.start}</td>
        			<td class="name">${item.end}</td>
        			<td class="name">
        			% for lessonlocation in item.lesson_locations:
        				<a href="/location/add?locationid=${lessonlocation.locationid}">
        				${lessonlocation.location.name}
        			</a>—${lessonlocation.studentnum}人
        				<br/>
        			%endfor
        			</td>
        			<td class="name">
        			%if item.state==0:
        			申请中
        			%elif item.state==1:
        			申请成功
        			%elif item.state==2:
        			申请失败
        			%endif
					</td>
        			<td class="name">
        			<a class="btn btn-info" href="/admin/lesson/edit?lessonid=${item.id}">编辑</a>
        			<a class="btn btn-danger" href="/lesson/del?lessonid=${item.id}">删除</a></td>
      			</tr>
      			% endfor
    		</tbody>
    		<!--
    		<tfoot >
    			<tr>
    				<th colspan="6"><a class="btn btn-primary" id="btn_head" href="/lesson/add" style="margin:0;width:97%;"><i class="icon-plus-sign icon-white"></i> 添加课堂</a> </th>
    			</tr>
    		</tfoot>
    		-->
            </table>
            <div class="right_foot">
            	<div class="pagination">
                <ul>
          	 		% if items.first_page:
	          		<li><a href="?courseid=${request.params.get('courseid')}&page=${items.first_page}" title="第一页">&laquo; 第一页</a></li>
	         		% endif
	         		 % if items.previous_page:
	          		<li><a href="?courseid=${request.params.get('courseid')}&page=${items.previous_page}" title="上一页">&laquo; 上一页</a></li>
	          		% endif
	         		% for i in range(items.page - 3,items.page):
			  		% if items.page_count>0 and i>=items.first_page:
					<li><a href="?courseid=${request.params.get('courseid')}&page=${i}" class="number" title="${i}">${i}</a></li>
					% endif
			  		% endfor
	          		<li><a href="#" class="number current" title="${items.page}">${items.page}</a></li> 
	          		% for i in range(items.page+1, items.page + 3):
			  			% if items.page_count>0 and i<=items.last_page:
						<li><a href="?courseid=${request.params.get('courseid')}&page=${i}" class="number" title="${i}"> ${i} </a></li>
			  			% endif
			 		% endfor
			  		% if items.next_page:
			  		<li><a href="?courseid=${request.params.get('courseid')}&page=${items.next_page}" title="下一页">下一页 &raquo;</a></li>
			  		% endif
			  		% if items.last_page:
	          		<li><a href="?courseid=${request.params.get('courseid')}&page=${items.last_page}" title="最后一页">最后一页 &raquo;</a></li> 
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