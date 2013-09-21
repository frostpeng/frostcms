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
        		<input type="text" class="span2 search-query" style="width:100px;" name="week" placeholder="周次"/>
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
        	<table class="table table-bordered " style="text-align:center;" id="main_table">
            <thead>
      			<tr class="class-tab-head">     
        			<th colspan="8">
        			<i class="icon-time"></i> 周次：
        			% if week :
        			${week}
        			% endif
        			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        			<i class="icon-th-large"></i> 实验室 ： 
        			% if loc :
        			${loc.name}
        			% endif
        			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        			<i class="icon-user"></i> 座位 ：
        			% if seatnum :
        			${seatnum}
        			% endif
        			</th>
      			</tr>
      			<tr class="class-tab-head">
      				<th class="class-tab">星期</th>
      				<th class="class-tab">日</th>
      				<th class="class-tab">一</th>
      				<th class="class-tab">二</th>
      				<th class="class-tab">三</th>
      				<th class="class-tab">四</th>
      				<th class="class-tab">五</th>
      				<th class="class-tab">六</th>
      			</tr>
    		</thead>
            <tbody>
            	% for time in range(0,6) :
            	<tr class="class-tab">
            		<th class="class-tab"><br />${time*2+1}-${time*2+2}</th>
            		% for dow in range(0,7) :
            		% if items :
            			% if items[dow][time].studentnum==0 :
            			<td class="class-tab">	
            			% elif items[dow][time].studentnum==seatnum :
            			<td class="class-tab-none">
            			% else :
            			<td class="class-tab-have">
            			% endif
            			% for cour in items[dow][time].courses :
            			[${cour.lesson.course.name}]
            			% endfor
            			<br />${items[dow][time].studentnum}/${seatnum}
            		% else :
            			<td class="class-tab">
            		% endif
            			</td>
            		% endfor
            	</tr>
            	% endfor
            	<!--
            	<tr class="class-tab">
            		<td class="class-tab"><br />1-2</td>
            		<td colspan="7" rowspan="6">
            		<table class="class-tab-inner table-hover">
            		<span id="ClassTableInner"></span>
            		</table>
            		</td>
            	</tr>
            	<tr class="class-tab">
            		<td class="class-tab"><br />3-4</td>
            	</tr>
            	<tr class="class-tab">
            		<td class="class-tab"><br />5-6</td>
            	</tr>
            	<tr class="class-tab">
            		<td class="class-tab"><br />7-8</td>
            	</tr>
            	<tr class="class-tab">
            		<td class="class-tab"><br />9-10</td>
            	</tr>
            	<tr class="class-tab">
            		<td class="class-tab"><br />11-12</td>
            	</tr>
            	-->
    		</tbody>
            </table>
        </div>               
        
    </div>
    <!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>