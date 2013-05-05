<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <link href="../../static/css/bootstrap.css" rel="stylesheet" />
    <link href="../../static/css/ccms.css" rel="stylesheet"/>
    <link href="../../static/css/datetimepicker.css" rel="stylesheet"/>
    <script src="../../static/js/bootstrap.js"></script>
    <script src="../../static/js/jquery.js"></script>
    <script src="../../static/js/ccms.js"></script>
    <script src="../../static/js/datetimepicker.js"></script>
    <script src="../../static/js/datetimepicker_CN.js"></script>
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
        	<form action="/semester/del" class="add" name="semester">
 				%if semester:
 				<div class="app_name">
        		学期删除
        		</div>
        		<input type="hidden" name="semester.id" value="${semester.id}"/>
        		<div class="input-prepend">
  					<span class="add-on">学期</span>
  					<input class="span2" id="prependedInput" type="text" name="semester.name" placeholder="" readOnly="true" value="${semester.name}" />
				</div>
				<br />				
        		<div class="input-prepend">
  					<span class="add-on">开始日期</span>
  					<input class="span2" id="prependedInput" type="text" name="semester.time" placeholder="" readOnly="true" value="${semester.time}" />
				</div>
				<br />								
				<div class="input-prepend">
  					<span class="add-on">周数</span>
  					<input class="span2" id="prependedInput" type="text" name="semester.weeks" placeholder="" readOnly="true" value="${semester.weeks}" />
				</div>
				<br />
 				<button class="btn btn-danger" id="add_submit" type="submit">确认删除</button>
 				%endif
 			</form>
        </div>               
        
    </div>
</body>
</html>