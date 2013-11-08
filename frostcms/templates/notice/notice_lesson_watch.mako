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
    	% if notice :
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">主题 ： 
				% if notice.action == -1 :
        		 课程《${notice.lesson.course.name}》于第${notice.lesson.week}周的课堂已被删除
        		% elif notice.action == 1 :
        		 课程《${notice.lesson.course.name}》于第${notice.lesson.week}周的课堂申请成功
        		% elif notice.action == 2 :
        		 课程《${notice.lesson.course.name}》于第${notice.lesson.week}周的 课堂申请呗拒绝
        		% elif notice.action == -2 :
        		课程《${notice.lesson.course.name}》于第${notice.lesson.week}周的 删除课堂申请，已通过
        		% elif notice.action == -3 :
        		课程《${notice.lesson.course.name}》于第${notice.lesson.week}周的 删除课堂申请，呗拒绝
        		% endif 
			</div>
			<div class="notice_sender">
				<span class="label"><i class="icon-user icon-white"></i> 发件人：</span> ${notice.senduser.name}
			</div>
			<div class="notice_time">
				<%! 
					import time
					from datetime import datetime
				%>
				<span class="label"><i class="icon-time icon-white"></i> 时间：</span>
        		${datetime.fromtimestamp(notice.actiontime).year}-${datetime.fromtimestamp(notice.actiontime).month}-${datetime.fromtimestamp(notice.actiontime).day}
        		&nbsp;
        		${datetime.fromtimestamp(notice.actiontime).hour}:${datetime.fromtimestamp(notice.actiontime).minute}:${datetime.fromtimestamp(notice.actiontime).second}
        			
			</div>
			<div class="notice_app">
			<a onclick="delete_con('是否删除该通知？','/lesson/notice/del?workid=${notice.id}');" class="btn btn-danger btn-mini"><i class=" icon-remove icon-white" style="margin:2px;"></i> 删除通知</a>
			<a href="/lesson/notice/list" class="btn btn-primary btn-mini"><i class="icon-share-alt icon-white" style="margin:2px;"></i> 通知列表</a>
			</div>
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<div class="notice_main" >
        	<p>
        	课程《${notice.lesson.course.name}》的课堂（第${notice.lesson.week}周，星期
        	% if notice.lesson.dow == 0 :
        	日
        	% elif notice.lesson.dow == 1 :
        	一
        	% elif notice.lesson.dow == 2 :
        	二
        	% elif notice.lesson.dow == 3 :
        	三
        	% elif notice.lesson.dow == 4 :
        	四
        	% elif notice.lesson.dow == 5 :
        	五
        	% elif notice.lesson.dow == 6 :
        	六
        	% endif
        	，第${notice.lesson.start}-${notice.lesson.end}节）于[
        	${datetime.fromtimestamp(notice.actiontime).year}-${datetime.fromtimestamp(notice.actiontime).month}-${datetime.fromtimestamp(notice.actiontime).day}
        	&nbsp;
        	${datetime.fromtimestamp(notice.actiontime).hour}:${datetime.fromtimestamp(notice.actiontime).minute}:${datetime.fromtimestamp(notice.actiontime).second}
        	]
        	% if notice.action == -1 :
        	被[${notice.senduser.name}]删除。
        	% elif notice.action == 1 :
        	申请成功。
        	% elif notice.action == 2 :
        	申请被拒绝。
        	% elif notice.action == -2 :
        	课堂删除，申请已通过。
        	% elif notice.action == -3 :
        	课堂删除，申请被拒绝。
        	% endif
        	</p>
        	% if notice.description :
        	<p>${notice.description}</p>
        	% endif
        	<p>————本文件由服务器自动发送。</p>
        	</div>
        	<div class="notice_app2">
        		<a href="/lesson/notice/list" class="btn btn-primary btn-mini" ><i class="icon-share-alt icon-white" style="margin:2px;"></i> 通知列表</a>
				<a onclick="delete_con('是否删除该通知？','/lesson/notice/del?workid=${notice.id}');" class="btn btn-danger btn-mini" ><i class=" icon-remove icon-white" style="margin:2px;"></i> 删除通知</a>
			</div>
        </div>               
        % endif
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>