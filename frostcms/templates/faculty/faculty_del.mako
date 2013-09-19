<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <%include file="/unit/link_JS&CSS.mako" />
</head>

<body>
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">专业管理</div>
			<a class="btn btn-primary" id="btn_head" href="/faculty/list"><i class="icon-share-alt icon-white"></i> 专业列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/faculty/del" class="add">
 				%if faculty:
 				<div class="app_name">
        		删除专业
        		</div>
 				<input type="hidden" name="faculty.id" value="${faculty.id}"/>
 				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" placeholder="" readOnly="true" name="faculty.name" value="${faculty.name}"/>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">学院</span>
					
					% for li in lis:
						% if faculty.collegeid == li.id :
						<input class="span2" id="prependedInput" readOnly="true" type="text" value="${li.name}"/>
						% endif
					% endfor
				</div>
				<br />
 				<button class="btn btn-danger" id="add_submit" type="submit">确认删除</button>
 				%endif
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>