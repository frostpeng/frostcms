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
			<div class="title_2">专业管理</div>
			<a class="btn btn-primary" id="btn_head" href="/faculty/list">返回专业列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/faculty/save" class="add">
 				%if faculty:
 				<div class="app_name">
        		专业编辑
        		</div>
 				<input type="hidden" name="faculty.id" value="${faculty.id}"/>
 				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="faculty.name" value="${faculty.name}"/>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:200px" name="faculty.collegeid" size="1" onchange= "">
						<option disabled="disabled">--------请选择学院--------</option>
						% for li in lis:
						<option value="${li.id}" 
							% if faculty.collegeid == li.id :
								selected="selected"
							% endif
							>${li.name}</option>
						% endfor
					</select>
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">保存</button>
 				%else:
 				<div class="app_name">
        		添加专业
        		</div>
  				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" name="faculty.name" placeholder="" />
				</div>
				<br />
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:200px" name="faculty.collegeid" size="1" onchange= "">
						<option disabled="disabled" selected="selected" >--------请选择学院--------</option>
						% for li in lis:
						<option value="${li.id}" >${li.name}</option>
						% endfor
					</select>
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