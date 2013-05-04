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
			<div class="title_2">学期管理</div>
			<a class="btn btn-primary" id="btn_head" href="/semester/list">返回学期列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/location/save" class="add">
 				%if location:
 				<div class="app_name">
        		实验室详情
        		</div>
 				<input type="hidden" name="location.id" value="${semester.id}"/>
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">开始日期</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="semester.start" value="${semester.address}"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">周数</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="semester.weeks" value="${semester.totalrows}"/>
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">保存</button>
 				%else:
 				<div class="app_name">
        		添加实验室
        		</div>
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">开始日期</span>
  					<input class="span2" id="prependedInput" type="text" name="semester.start" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">周数</span>
  					<input class="span2" id="prependedInput" type="text" name="semester.weeks" placeholder="" />
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">提交</button>
 				%endif
 			</form>
        </div>               
        
    </div>
</body>
</html>