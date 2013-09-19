<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
    <script>
    function course_search(){
    	var key = document.course.courseid.value;
    	var open = "#course_name";
    	var str = "option.course_";
    	var show_id = "";
    	if (document.activeElement.id=="input_course_search")
    	{
    		if (key!=""){
    			$(open).show(600);
    			% for course in courses:
    			show_id = "#course_${course.id}";
    			$(show_id).hide();
    			show_name = "${course.name}";
    			if (show_name.indexOf(key) != -1){
    				$(show_id).show(10);}
    			else {
    				$(show_id).hide(10);}	
    			% endfor
    			}
    		else {
    			$(open).hide(600);
    		}
    		setInterval("course_search()",1500);
    	}
    	else {
    		$(open).hide(600);
    	}
   	}
    function course_close(){
    	var close = "#course_name";
    	$(close).hide(600);
    }
    function select(id){
    	document.course.courseid.value = document.course.course_name.value; 
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
			<div class="title_2">课堂管理</div>
			<a class="btn btn-primary" id="btn_head" href="/lesson/list"><i class="icon-share-alt icon-white"></i> 课堂列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/lesson/del" class="add" name="course">
 				%if lesson:
 				<input type="hidden" name="lesson.id" value="${lesson.id}"/>
 				<div class="app_name">
        		课堂删除
        		</div>
        		<div class="input-prepend"   id="add_adress">
  					<span class="add-on">课程</span>
  					<select class="span2" style="width:200px" name="lesson.courseid" size="1" onchange="" readOnly="true">
						<option disabled="disabled" selected="selected" >--------请选择课程--------</option>
						% for course in courses:
							% if course.id == lesson.courseid :
						 	<option value="${course.id}" selected="selected" >${course.name}</option>
							% else :
							<option value="${course.id}" >${course.name}</option>
							% endif
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">学期</span>
  					<select class="span2" style="width:200px" name="lesson.collegeid" size="1" onchange="" readOnly="true">
						<option disabled="disabled" selected="selected" >--------请选择学期--------</option>
						% for li in lis:
							% if li.id == lesson.course.semesterid :
							<option value="${li.id}" selected="selected">${li.name}</option>
							% else :
							<option value="${li.id}" >${li.name}</option>
							% endif
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">周次</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.week" value="${lesson.week}" placeholder="" readOnly="true" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">星期</span>
  					<select class="span2" style="width:200px" name="lesson.dow" size="1" onchange="" readOnly="true">
						<option value="0" 
						% if lesson.dow == 0 :
						selected="selected"
						% endif
						>星期日</option>
						<option value="1" 
						% if lesson.dow == 1 :
						selected="selected"
						% endif
						>星期一</option>
						<option value="2" 
						% if lesson.dow == 2 :
						selected="selected"
						% endif
						>星期二</option>
						<option value="3" 
						% if lesson.dow == 3 :
						selected="selected"
						% endif
						>星期三</option>
						<option value="4" 
						% if lesson.dow == 4 :
						selected="selected"
						% endif
						>星期四</option>
						<option value="5" 
						% if lesson.dow == 5 :
						selected="selected"
						% endif
						>星期五</option>
						<option value="6" 
						% if lesson.dow == 6 :
						selected="selected"
						% endif
						>星期六</option>
					</select>
				</div>
				<hr />
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">实验室</span>
  					<select class="span2" style="width:200px" name="lesson.locationid" size="1" onchange="" readOnly="true">
						<option disabled="disabled" selected="selected" >--------请选择实验室--------</option>
						% for location in locations:
							% if location.id == lesson.locationid :
							<option value="${location.id}" selected="selected">${location.name}</option>
							% else :
							<option value="${location.id}" >${location.name}</option>
							% endif
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">座次第一行</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.firstrow" value="${lesson.firstrow}" placeholder="" readOnly="true"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">座次最后一行</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.lastrow" value="${lesson.lastrow}" placeholder="" readOnly="true"/>
				</div>
				<hr />
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">备用实验室</span>
  					<select class="span2" style="width:200px" name="lesson.ext_location" size="1" onchange="" readOnly="true">
						<option disabled="disabled" selected="selected" >--------请选择实验室--------</option>
						% for location in locations:
							% if location.id == lesson.ext_location :
							<option value="${location.id}" selected="selected">${location.name}</option>
							% else :
							<option value="${location.id}" >${location.name}</option>
							% endif
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">备用座次第一行</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.ext_firstrow" value="${lesson.ext_firstrow}" placeholder="" readOnly="true"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">备用座次最后一行</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.ext_lastrow" value="${lesson.ext_lastrow}" placeholder="" readOnly="true"/>
				</div>
				<hr />
				<div class="input-prepend">
  					<span class="add-on">开始节数</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.starttime" value="${lesson.starttime}" placeholder="" readOnly="true"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">结束节数</span>
  					<input class="span2" id="prependedInput" type="text" name="lesson.endtime" value="${lesson.endtime}" placeholder="" readOnly="true"/>
				</div>
				<br />
				<div class="input-prepend" style="float:left;">
  					<span class="add-on">是否独占实验室</span>
				</div>
				<div style="float:left;margin:5px;">
					<input type="radio" name="lesson.monopolize" id="optionsRadios1" value="1" readOnly="true"
					% if lesson.monopolize == 1:
					checked
					% endif
					>
  					是&nbsp;&nbsp;&nbsp;&nbsp;
  					<input type="radio"name="lesson.monopolize" id="optionsRadios1" value="0" readOnly="true"
  					% if lesson.monopolize != 1:
					checked
					% endif
  					>
  					否
				</div>
				<br /><hr />
 				<button class="btn btn-danger" id="add_submit" type="submit">确认删除</button>
 				%endif
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>