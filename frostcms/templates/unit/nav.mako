% if request.user :
	% if request.user.role == 0:
<div class="left">
    	<ul class="nav nav-tabs nav-stacked" id="main_nav">
        	<li class="disabled"><a href=""><i class="icon-list"></i> 公共查询</a></li>
            <li><a href="/public/lesson_list">课堂查询</a></li>
            <li class="disabled"><a href=""><i class="icon-list"></i> 管理</a></li>
            <li><a href="/location/list">实验室</a></li>
            <li><a href="/mentor/list">教师</a></li>
            <li><a href="/semester/list">学期</a></li>
            <li><a href="/student/list">学生</a></li>
            <li><a href="/college/list">院系</a></li>
            <li><a href="/faculty/list">专业</a></li>
            <li><a href="/clazz/list">班级</a></li>
            <li><a href="/course/list">课程</a></li>
            <li><a href="/admin/lesson/undolist">课堂申请 <span class="badge badge-info">
            % if request.undocount>0:
            	${request.undocount}
            % else :
            	0
            % endif
            </span>
            </a></li>
            <li class="disabled"><a href="#"><i class="icon-list"></i> 通知</a></li>
            <li><a href="/lesson/notice/list">课堂通知 <span class="badge badge-important">
            % if request.noticenum>0:
            	${request.noticenum}
            % else :
            	0
            % endif
            </span></a></li>
		</ul>
</div>
	% elif request.user.role == 1:
<div class="left">
    	<ul class="nav nav-tabs nav-stacked" id="main_nav">
        	<li class="disabled"><a href=""><i class="icon-list"></i> 公共查询</a></li>
            <li><a href="/public/lesson_list">课堂查询</a></li>
            <li class="disabled"><a href=""><i class="icon-list"></i> 教师</a></li>
            <li><a href="/mentor/course/list">我的课程</a></li>
            <li><a href="/mentor/courseware/list">我的课件</a></li>
            <li><a href="/mentor/assignment/list">我的作业</a></li>
            <!--<li><a href="#">课堂申请</a></li>-->
            <li class="disabled"><a href="#"><i class="icon-list"></i> 通知</a></li>
            <li><a href="/lesson/notice/list">课堂通知 <span class="badge badge-important">
            % if request.noticenum>0:
            	${request.noticenum}
            % else :
            	0
            % endif
            </span></a></li>
		</ul>
</div>
	% elif request.user.role == 2:
<div class="left">
    	<ul class="nav nav-tabs nav-stacked" id="main_nav">
        	<li class="disabled"><a href=""><i class="icon-list"></i> 公共查询</a></li>
            <li><a href="/public/lesson_list">课堂查询</a></li>
            <li class="disabled"><a href=""><i class="icon-list"></i> 学生</a></li>
            <li><a href="/student/course/list">我的课程</a></li>
            <li><a href="#">我的作业</a></li>
		</ul>
</div>
	% endif
% else :
<div class="left">
    	<ul class="nav nav-tabs nav-stacked" id="main_nav">
        	<li class="disabled"><a href="#">公共查询</a></li>
            <li><a href="/public/lesson_list">课堂查询</a></li>
		</ul>
</div>
% endif