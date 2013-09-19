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
			<div class="title_2">实验室管理</div>
			<a class="btn btn-primary" id="btn_head" href="/location/list"><i class="icon-share-alt icon-white"></i> 实验室列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/location/del" class="add">
 				%if location:
 				<div class="app_name">
        		实验室删除
        		</div>
 				<input type="hidden" name="location.id" value="${location.id}"/>
 				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" readOnly="true" type="text" placeholder="" name="location.name" value="${location.name}"/>
				</div>
				<br />
				<div class="input-prepend"  id="add_adress">
  					<span class="add-on">地址</span>
  					<input class="span2" id="prependedInput" readOnly="true" type="text" placeholder="" name="location.address" value="${location.address}"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">排数</span>
  					<input class="span2" id="prependedInput" readOnly="true" type="text" placeholder="" name="location.totalrows" value="${location.totalrows}"/>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">列数</span>
  					<input class="span2" id="prependedInput" readOnly="true" type="text" placeholder="" name="location.perrow" value="${location.perrow}"/>
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