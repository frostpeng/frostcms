<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
	 <script type="text/javascript" src="/static/js/jquery-1.10.2.min.js"></script>
     <script type="text/javascript" src="/static/js/jquery-ui.js"></script>
   <script type="text/javascript" src="/static/js/jquery.validate.min.js"></script>
       <script type="text/javascript" src="/static/js/ajaxfileupload2.js"></script>
	<link href="/static/css/bootstrap.css" rel="stylesheet" media="screen"/>
<link href="/static/css/ccms.css" rel="stylesheet" media="screen"/>
<script src="../../static/js/bootstrap.js"></script>
<script src="../../static/js/ccms.js"></script>
<script src="../../static/js/searchID.js"></script>
<script src="/static/js/datetimepicker.js"></script>
</head>

<body>
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">作业安排</div>
			<a class="btn btn-primary" id="btn_head" href="Javascript:history.back()"><i class="icon-share-alt icon-white"></i> 返回</a>   			
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/lesson/save" class="add" name="course">
        	   <br />
				<div class="input-prepend">
  					<span class="add-on">标题</span>
  					<span class="add-on">${assignment.title if assignment else u''}</span>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">描述</span>
  					<span class="add-on">${assignment.description if assignment else u''}</span>
  				</div>
				<br />
			<div class="input-prepend">
                   		<span class="add-on">截止时间</span>
                   		<span class="add-on">
                    		<%!import time %>
       ${time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(assignment.duedate))}
       </span>
            		</div>		
				<br />
				<div class="input-prepend" id="download_div" type="hidden">
				%if assignment:
					<span class='add-on'>已上传附件</span>
					<span class='add-on'><a href='/user/getfilebyid?fsfileid=${assignment.fsfileid}'>附件下载</a></span>
				%endif
				</div>
				<hr />
				<span id="debug"></span>
 			</form>
        </div>               
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>