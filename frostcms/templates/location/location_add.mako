<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
</head>

<body  onload="pageinit();">
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">实验室管理</div>
			<a class="btn btn-primary" id="btn_head" href="/location/list"><i class="icon-share-alt icon-white"></i> 实验室列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/location/save" class="add" name="location">
 				%if location:
 				<div class="app_name">
        		实验室详情
        		</div>
 				<input type="hidden" name="location.id" value="${location.id}"/>
 				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.name" value="${location.name}"/>
				</div>
				<span id="checkLocationName"></span>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">地址</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.address" value="${location.address}"/>
				</div>
				<span id="checkLocationAddress"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">排数</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.totalrows" value="${location.totalrows}"/>
				</div>
				<span id="checkLocationTotalrows"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">列数</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.perrow" value="${location.perrow}"/>
				</div>
				<span id="checkLocationPerrow"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">总位数</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.seatnum" value="${location.seatnum}"/>
				</div>
				<span id="checkLocationSeatnum"></span>
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
				<span id="checkLocationArea"></span>
				</div>
				<br />
 				<input class="btn btn-primary" id="add_submit" type="button" value="保存" onclick="checkLocationAdd();" />
 				%else:
 				<div class="app_name">
        		添加实验室
        		</div>
  				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" name="location.name" placeholder="" />
				</div>
				<span id="checkLocationName"></span>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">地址</span>
  					<input class="span2" id="prependedInput" type="text" name="location.address" placeholder="" />
				</div>
				<span id="checkLocationAddress"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">排数</span>
  					<input class="span2" id="prependedInput" type="text" name="location.totalrows" placeholder="" />
				</div>
				<span id="checkLocationTotalrows"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">列数</span>
  					<input class="span2" id="prependedInput" type="text" name="location.perrow" placeholder="" />
				</div>
				<span id="checkLocationPerrow"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">总位数</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" name="location.seatnum"/>
				</div>
				<span id="checkLocationSeatnum"></span>
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
				<span id="checkLocationArea"></span>
				</div>
				<br />
 				<input class="btn btn-primary" id="add_submit" type="button" value="提交" onclick="checkLocationAdd();" />
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