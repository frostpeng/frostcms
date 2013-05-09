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

<body>
	<!-- 导航栏部分 -->
    <%include file="/main/nav_admin.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">教师管理</div>
			<a class="btn btn-primary" id="btn_head" href="/mentor/list">返回教师列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/mentor/del" class="add">
 				%if mentor:
 				<div class="app_name">
        		教师删除
        		</div>
 				<input type="hidden" name="mentor.id" value="${mentor.id}"/>
  				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" readOnly="true" name="mentor.name" value="${mentor.name}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">教工号</span>
  					<input class="span2" id="prependedInput" type="text" readOnly="true" name="mentor.identity" value="${mentor.identity}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend" style="float:left;">
  					<span class="add-on">性别</span>
				</div>
				<div style="float:left;margin:5px;">
					% if mentor.gender=='1':
					<input type="radio" name="mentor.gender" readOnly="true" id="optionsRadios1" value="1" checked/>
  					男&nbsp;&nbsp;&nbsp;&nbsp;
  					<input type="radio"name="mentor.gender" readOnly="true" id="optionsRadios1" value="0" />
  					女
  					% else :
  					<input type="radio" name="mentor.gender" readOnly="true" id="optionsRadios1" value="1" />
  					男&nbsp;&nbsp;&nbsp;&nbsp;
  					<input type="radio"name="mentor.gender" readOnly="true" id="optionsRadios1" value="0" checked/>
  					女
  					% endif
				</div>
				<br /><br />
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:200px" name="mentor.collegeid" readOnly="true" size="1" onchange= "">
						<option disabled="disabled" selected="selected" >--------请选择学院--------</option>
						% for li in lis:
						<option value="${li.id}" 
						% if li.id == mentor.collegeid :
						selected="selected"
						% endif
						>${li.name}</option>
						% endfor
					</select>
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">头衔</span>
  					<input class="span2" id="prependedInput" type="text" readOnly="true" name="mentor.title" value="${mentor.title}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">电话</span>
  					<input class="span2" id="prependedInput" type="text" readOnly="true" name="mentor.phone" value="${mentor.phone}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">邮箱</span>
  					<input class="span2" id="prependedInput" type="text" readOnly="true" name="mentor.email" value="${mentor.email}" placeholder="" />
				</div>
				<br />
				<div >
				描述：
				<br />
				<textarea rows="3" cols="100" style="margin:0 0 0 30px;width:560px;" readOnly="true" name="mentor.decription">${mentor.decription}</textarea>
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