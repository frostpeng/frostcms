<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
</head>

<body onload="searchGetCollege();">
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">专业管理</div>
			<a class="btn btn-primary" id="btn_head" href="/clazz/list"><i class="icon-share-alt icon-white"></i> 班级主栏</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/clazz/save" class="add" name="clazz" method="post">
 				<div class="app_name">
        		添加班级
        		</div>
 				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:180px" id="putCollegeBox" name="clazz.collegeid" onchange="searchGetFaculty(this);" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择学院--------</option>
					</select>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">专业</span>
  					<select class="span2" style="width:180px" id="putFacultyBox" name="clazz.facultyid" onchange="" >
						<option disabled="disabled" selected="selected" value="-1">--------请选择专业--------</option>
					</select>
				</div>
				<span id="checkClazzFacultyid"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">年级</span>
  					<input class="span2" style="width:160px;" id="prependedInput" type="text" name="clazz.year" placeholder="请输入年级，例：2013">
				</div>
				<span id="checkClazzYear"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">班号</span>
  					<input class="span2" id="prependedInput" type="text" name="clazz.num" placeholder="请输入班级号">
				</div>
				<span id="checkClazzNum"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">位置浮动率</span>
  					<input class="span2" id="prependedInput" type="text" name="clazz.mulfloat" placeholder="请输入班级号" value="1">
  					<span class="add-on">%</span>
				</div>
				<span id="checkClazzMulfloat"></span>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="button" onclick="checkClazzAdd();">提交</button>
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>