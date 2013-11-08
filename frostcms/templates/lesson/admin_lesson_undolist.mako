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
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
      			<tr>    
      				<th class="name">课程名</th> 
      				<th class="name">申请人</th> 
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
      				<td class="name">
      				<a href="/course/add?courseid=${item.course.id}">
      				${item.course.name}
      				</a></td>
      				<td class="name">
      				<a  href="/mentor/add?mentorid=${item.course.mentorid}">
      				${item.course.mentor.name}
      				</a></td>
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
        			申请课堂
        			%elif item.state==1:
        			申请成功
        			%elif item.state==2:
        			申请失败
        			%elif item.state==-2:
        			申请删除
        			%endif
					</td>
        			<td class="name">
        			<a class="btn btn-info" href="/admin/lesson/agree?lessonid=${item.id}">批准</a>
        			<a class="btn btn-danger" href="/admin/lesson/disagree?lessonid=${item.id}">拒绝</a>
        			</td>
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