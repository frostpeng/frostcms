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
			<div class="title_2">查询课表 </div> 
			<form class="search" action="/public/lesson_list" name="form1" method="post">
			<div class="input-prepend input-append">
				<span class="add-on">第</span>
        		<input type="text" class="span2" style="width:30px;text-align:center;" name="week" placeholder="周次"
        		% if request.thisweek :
        			value="${request.thisweek}"
        		% endif
        		/>
        		<span class="add-on">周</span>
        	</div>
        		<select name="dow" class="span2 input-large" style="width:110px;">
        			<option value="0">周日</option>
        			<option value="1">周一</option>
        			<option value="2">周二</option>
        			<option value="3">周三</option>
        			<option value="4">周四</option>
        			<option value="5">周五</option>
        			<option value="6">周六</option>
        			<option value="7" selected="selected">周几（空）</option>
        		</select>
				<select name="area" class="span2  input-large" style="width:160px;"id="appendedPrependedDropdownButton" onchange="setArea();">
					<option selected="selected" value="-1">校区（置空）</option>
					<option value="0" >主校区</option>
					<option value="1" >东校区</option>
					<option value="2" >西校区</option>
					<option value="3" >同济校区</option>
				</select>
				<select name="locationid" class="span2  input-large" style="width:160px;" id="appendedPrependedDropdownButton">
					<option selected="selected" value="-1">实验室（置空）</option>
					% for li in locationdictionary:
					<option value="${li.id}" class="location_${li.area}" style="display:none;">${li.name}</option>
					% endfor
				</select>       	
         		<button type="submit" name="submit" class="btn" style="margin:0 0 10px 0;"><i class="icon-search"></i> 查询</button>        	
        	</form>
		</div>
		
        <!-- 主体信息表 -->
        <div class="right_main">
        	<table class="table table-bordered " style="text-align:center;" id="main_table">
            <thead>
      			<tr class="class-tab-head">     
        			<th colspan="8">
        			% if week :
        			<i class="icon-time"></i> 第 ${week} 周
        			% endif
        			&nbsp;&nbsp;&nbsp;
        			% if dayofweek and int(dayofweek)<=6 :
        			周 
        				% if int(dayofweek)==0 :
        					日
        				% elif int(dayofweek)==1 :
        					一
        				% elif int(dayofweek)==2 :
        					二
        				% elif int(dayofweek)==3 :
        					三
        				% elif int(dayofweek)==4 :
        					四
        				% elif int(dayofweek)==5 :
        					五
        				% elif int(dayofweek)==6 :
        					六
        				% else:
        					${dayofweek}
        				% endif
        			% endif
        			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        			% if loc :
        			<i class="icon-th-large"></i> 实验室 ：${loc.name}
        			% endif
        			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        			% if seatnum :
        			<i class="icon-user"></i> 座位 ：${seatnum}
        			% endif
        			</th>
      			</tr>
      			% if items:
      			<tr class="class-tab-head">
      				% if int(dayofweek)>=7 :
      				<th class="class-tab">星期</th>
      				<th class="class-tab">日</th>
      				<th class="class-tab">一</th>
      				<th class="class-tab">二</th>
      				<th class="class-tab">三</th>
      				<th class="class-tab">四</th>
      				<th class="class-tab">五</th>
      				<th class="class-tab">六</th>
      				% else:
      				<th class="class-tab">实验室</th>
      				<th class="class-tab">1-2</th>
      				<th class="class-tab">3-4</th>
      				<th class="class-tab">5-6</th>
      				<th class="class-tab">7-8</th>
      				<th class="class-tab">9-10</th>
      				<th class="class-tab">11-12</th>
      				% endif
      			</tr>
      			% endif
    		</thead>
            <tbody>
            % if items :
            	% if int(dayofweek)>=7 :
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
            	% else:
            		% for item in items :
            		<tr>
            			<td class="class-tab2">${item.location.name}</td>
            			% for time in range(0,6) :
            				<td class="class-tab2">
            					% for cour in item.lessons[time].courses :
            						[${cour.name}]&nbsp;&nbsp;
            					% endfor
            					<br />${item.lessons[time].studentnum}/${item.location.seatnum}
            				</td>
            			% endfor
            		</tr>
            		% endfor
            	% endif
			% endif
    		</tbody>
            </table>
        </div>               
        
    </div>
    <!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>