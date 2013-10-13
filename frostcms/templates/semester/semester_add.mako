<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
    <script src="/static/js/datetimepicker.js"></script>
    <script src="/static/js/datetimepicker_CN.js"></script>
    <script >	
						function noneDays(){
							var year = document.semester.year.value;
							var mon = document.semester.mon.value;
							var mon_day = [31,28,31,30,31,30,31,31,30,31,30,31];
							if ((year%100 && year%4==0) || year%400==0)
								mon_day[1] +=1;
							var day = 0;
							for (day=1;day<=31;day++)
							{
								var str = "#day_"+day.toString();
								$(str).hide();
							}
						}
	</script>
</head>

<body onload="noneDays();">
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">学期管理</div>
			<a class="btn btn-primary" id="btn_head" href="/semester/list"><i class="icon-share-alt icon-white"></i> 学期列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/semester/save" class="add" name="semester">
 				%if semester:
 				<div class="app_name">
        		学期管理
        		</div>
        		<input type="hidden" name="semester.id" value="${semester.id}"/>				
				<fieldset>
            		<div class="control-group">
                		<label class="control-label"></label>
                		<div class="controls input-prepend input-append date form_datetime" id="datetimepicker" data-date="${semester.time}" data-date-format="yyyy-MM-dd" data-link-field="dtp_input1">
                   		<span class="add-on">开始日期</span>
                    		<input size="16" type="text" name="semester.start" value="${semester.time}" readonly>
                    		<span class="add-on"><i class=" icon-remove"></i></span>
							<span class="add-on"><i class=" icon-th"></i></span>
                		</div>
						<input type="hidden" id="dtp_input1" value="" />
						<span id="checkSemesterStart"></span>
            		</div>			
        		</fieldset>									
				<div class="input-prepend">
  					<span class="add-on">周数</span>
  					<input class="span2" id="prependedInput" type="text" name="semester.weeks" placeholder="" value="${semester.weeks}" />
				</div>
				<span id="checkSemesterWeeks"></span>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="button" onclick="checkSemesterAdd()">保存</button>
 				%else:
 				<div class="app_name">
        		添加学期
        		</div>							
				<fieldset>
            		<div class="control-group">
                		<label class="control-label"></label>
                		<div class="controls input-prepend input-append date form_datetime" id="datetimepicker" data-date="2013-09-1" data-date-format="yyyy-MM-dd" data-link-field="dtp_input1">
                   		<span class="add-on">开始日期</span>
                    		<input size="16" type="text" name="semester.start" value="" readonly>
                    		<span class="add-on"><i class=" icon-remove"></i></span>
							<span class="add-on"><i class=" icon-th"></i></span>
                		</div>
						<input type="hidden" id="dtp_input1" value="" />
						<span id="checkSemesterStart"></span>
            		</div>
        		</fieldset>										
				<div class="input-prepend">
  					<span class="add-on">周数</span>
  					<input class="span2" id="prependedInput" type="text" name="semester.weeks" placeholder="" />
				</div>
				<span id="checkSemesterWeeks"></span>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="button" onclick="checkSemesterAdd()">提交</button>
 				%endif
 		
 			</form>
        </div>               
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>
<script type="text/javascript">
    		$('.form_datetime').datetimepicker({
        		language:'zh-CN',
        		weekStart:0,
        		format:'yyyy-mm-dd',
        		todayBtn:0,
        		daysOfWeekDisabled:'1,2,3,4,5,6',
				autoclose:1,
				todayHighlight:1,
				startView:2,
				minView:2,
				forceParse:0,
        		showMeridian:1
   	 		});
	</script>