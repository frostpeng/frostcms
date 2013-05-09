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

<body  onload="pageinit();">
	<!-- 导航栏部分 -->
    <%include file="/main/nav_admin.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">实验室管理</div>
			<a class="btn btn-primary" id="btn_head" href="/location/list">返回实验室列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/location/save" class="add">
 				%if location:
 				<div class="app_name">
        		实验室详情
        		</div>
 				<input type="hidden" name="location.id" value="${location.id}"/>
 				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.name" value="${location.name}"/>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">地址</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.address" value="${location.address}"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">排数</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.totalrows" value="${location.totalrows}"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">列数</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.perrow" value="${location.perrow}"/>
				</div>
				<br />
					<div class="input-prepend">
  					<span class="add-on">校区</span>
  					<select name="location.area" class="span2  input-large" id="location_area" value="${location.area}">
					<option disabled="disabled" value="-1">--------请选择校区--------</option>
					<option value="0" >主校区</option>
					<option value="1" >东校区</option>
					<option value="2" >西校区</option>
					<option value="3" >同济校区</option>
				</select>
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="submit">保存</button>
 				%else:
 				<div class="app_name">
        		添加实验室
        		</div>
  				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" name="location.name" placeholder="" />
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">地址</span>
  					<input class="span2" id="prependedInput" type="text" name="location.address" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">排数</span>
  					<input class="span2" id="prependedInput" type="text" name="location.totalrows" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">列数</span>
  					<input class="span2" id="prependedInput" type="text" name="location.perrow" placeholder="" />
				</div>
				<br />
					<div class="input-prepend">
  					<span class="add-on">校区</span>
  					<select name="location.area" class="span2  input-large" id="appendedPrependedDropdownButton">
					<option disabled="disabled" selected="selected" value="-1">--------请选择校区--------</option>
					<option value="0" >主校区</option>
					<option value="1" >东校区</option>
					<option value="2" >西校区</option>
					<option value="3" >同济校区</option>
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
<script type="text/javascript">
function pageinit()
{
    %if location:
	var location_area="${location.area}";
	selectoption("location_area",location_area);
	%endif
}

function selectoption(selectid,value)
{
	var select=document.getElementById(selectid);
	if(select !=null)
	{
		var option=select.options
		for(var i=0;i<option.length;i++)
	 	{
	 		if(option[i].value==value)
	 		{
	 			option[i].selected=true;
	 		}
	 	}
	}
}

	
</script>
</html>