<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
    <script>
		function setArea(){
			var area = document.form1.area.value;
			for(i=0;i<4;i++){
			close = "option.location_"+i.toString();
			$(close).hide();
			}
			open = "option.location_"+area.toString();
			$(open).show();
			document.form1.locationid.value = -1;
		}
		
	</script>
</head>

<body>
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">查询课表</div> 
			<form class="search form-search" action="/public/lesson_list" name="form1" method="post">
			<div class="input-append">
        		<input type="text" class="span2 search-query" name="startweek" placeholder="开始周"/>
        		<input type="text" class="span2" id="appendedPrependedDropdownButton" name="endweek" placeholder="到此周"/>
				<select name="area" class="span2  input-large" id="appendedPrependedDropdownButton" onchange="setArea();">
					<option disabled="disabled" selected="selected" value="-1">--------请选择校区--------</option>
					<option value="0" >主校区</option>
					<option value="1" >东校区</option>
					<option value="2" >西校区</option>
					<option value="3" >同济校区</option>
				</select>
				<select name="locationid" class="span2  input-large" id="appendedPrependedDropdownButton">
					<option disabled="disabled" selected="selected" value="-1">--------请选择实验室--------</option>
					% for li in locationdictionary:
					<option value="${li.id}" class="location_${li.area}" style="display:none;">${li.name}</option>
					% endfor
				</select>
         		<input type="submit" name="submit" class="btn dropdown-toggle" value="查询" />
         	</div>
        	</form>
		</div>
		
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
      			<tr>     
        			<th class="name_l">课表</th>
        			<th class="app">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name"></td>
        			<td class="app">
        				<a class="btn btn-info btn-mini" href="/college/add?collegeid=${item.id}">编辑</a>
        				<a class="btn btn-danger btn-mini" href="/college/del?collegeid=${item.id}">删除</a>
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