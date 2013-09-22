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
			<div class="title_2">课程通知</div>
		
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover table-condensed" id="main_table">
            <thead>
      			<tr>     
        			<th class="notice_head"></th>
        			<th class="notice_sender">发件人</th>
        			<th class="notice_title">主题</th>
        			<th class="notice_time">时间</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items :
      			<tr class="notice_all" onclick="notice_page(${item.id})">
      				<td class="notice_head">
      				% if item.viewstate == 0 :
      				<span class="label label-important"> <i class="icon-envelope icon-white"></i> </span>
      				% else :
      				<span class="label label-info"> <i class="icon-envelope icon-white"></i> </span>
      				% endif
      				</td>
        			<td class="notice_sender">${item.senduser.name}</td>
        			<td class="notice_title">
        			% if item.action == -1 :
        			<span class="label label-info">通知</span> 课程《${item.lesson.course.name}》于第${item.lesson.week}周的 <span class="label label-important">课堂已被删除</span>
        			% elif item.action == 1 :
        			<span class="label label-info">通知</span> 课程《${item.lesson.course.name}》于第${item.lesson.week}周的 <span class="label label-success">课堂申请成功</span>
        			% elif item.action == 2 :
        			<span class="label label-info">通知</span> 课程《${item.lesson.course.name}》于第${item.lesson.week}周的 <span class="label label-warning">课堂申请呗拒绝</span>
        			% endif 
        			</td>
        			<td class="notice_time">
        			<%! 
							import time
							from datetime import datetime
					%>
        			${datetime.fromtimestamp(item.actiontime).year}-${datetime.fromtimestamp(item.actiontime).month}-${datetime.fromtimestamp(item.actiontime).day}
        			&nbsp;
        			${datetime.fromtimestamp(item.actiontime).hour}:${datetime.fromtimestamp(item.actiontime).minute}:${datetime.fromtimestamp(item.actiontime).second}
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