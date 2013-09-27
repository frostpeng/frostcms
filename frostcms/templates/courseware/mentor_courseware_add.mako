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
			<div class="title_2">课件添加</div>
			<a class="btn btn-primary" id="btn_head" href="/mentor/courseware/list">返回课件列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form enctype="multipart/form-data"  action="/mentor/courseware/save"  method="post">
 				%if courseware:
 				<div class="app_name">
        		添加课件
        		</div>
        		<input type="hidden" name="coursewareid" value="${courseware.id}"/>
  				<div class="input-prepend">
  					<span class="add-on">标题</span>
  					<input class="span2" id="prependedInput" type="text" name="title" value="${courseware.title}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">描述</span>
  					<input class="span2" id="prependedInput" type="text" name="description" value="${courseware.description}" placeholder="" />
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">保存</button>
 				%else:
 				<div class="app_name">
        		添加课件
        		</div>
  				<div class="input-prepend">
  					<span class="add-on">标题</span>
  					<input class="span2" id="prependedInput" type="text" name="title" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">描述</span>
  					<input class="span2" id="prependedInput" type="text" name="description"   placeholder="" />
				</div>
				<br />
				<div class="input-append">
				<span class="add-on">课件</span>
				<input type="file" name="coursefile" style="vertical-align:middle;height:20px;width:220px;line-height:30px;margin:0;text-aligin:center;" />
			</div>
			<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">提交</button>
 				%endif
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>