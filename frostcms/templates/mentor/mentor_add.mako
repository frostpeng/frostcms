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
			<div class="title_2">教师管理</div>
			<a class="btn btn-primary" id="btn_head" href="/mentor/list"><i class="icon-share-alt icon-white"></i> 教师列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/mentor/save" class="add" name="mentor">
 				%if mentor:
 				<div class="app_name">
        		教师信息
        		</div>
 				<input type="hidden" name="mentor.id" value="${mentor.id}"/>
  				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.name" value="${mentor.name}" placeholder="" />
				</div>
				<span id="checkMentorName"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">教工号</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.identity" value="${mentor.identity}" placeholder="" />
				</div>
				<span id="checkMentorIdentity"></span>
				<br />
				<div class="input-prepend" style="float:left;">
  					<span class="add-on">性别</span>
				</div>
				<div style="float:left;margin:5px;">
					% if mentor.gender=='1':
					<input type="radio" name="mentor.gender" id="optionsRadios1" value="1" checked/>
  					男&nbsp;&nbsp;&nbsp;&nbsp;
  					<input type="radio"name="mentor.gender" id="optionsRadios1" value="0" />
  					女
  					% else :
  					<input type="radio" name="mentor.gender" id="optionsRadios1" value="1" />
  					男&nbsp;&nbsp;&nbsp;&nbsp;
  					<input type="radio"name="mentor.gender" id="optionsRadios1" value="0" checked/>
  					女
  					% endif
				</div>
				<br /><br />
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:200px" name="mentor.collegeid" size="1" onchange= "">
						<option disabled="disabled" selected="selected" value="-1" >--------请选择学院--------</option>
						% for li in lis:
						<option value="${li.id}" 
						% if li.id == mentor.collegeid :
						selected="selected"
						% endif
						>${li.name}</option>
						% endfor
					</select>
				</div>
				<span id="checkMentorCollegeid"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">头衔</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.title" value="${mentor.title}" placeholder="" />
				</div>
				<span id="checkMentorTitle"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">电话</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.phone" value="${mentor.phone}" placeholder="" />
				</div>
				<span id="checkMentorPhone"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">邮箱</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.email" value="${mentor.email}" placeholder="" />
				</div>
				<span id="checkMentorEmail"></span>
				<br />
				<div >
				描述：
				<br />
				<textarea rows="3" cols="100" style="margin:0 0 0 30px;width:560px;" name="mentor.description">${mentor.description if mentor.description else u'' }</textarea>
				</div>
				<span id="checkMentorDescription"></span>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="button" onclick="checkMentorAdd()">保存</button>
 				%else:
 				<div class="app_name">
        		添加教师
        		</div>
  				<div class="input-prepend">
  					<span class="add-on">姓名</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.name" placeholder="" />
				</div>
				<span id="checkMentorName"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">教工号</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.identity" placeholder="" />
				</div>
				<span id="checkMentorIdentity"></span>
				<br />
				<div class="input-prepend" style="float:left;">
  					<span class="add-on">性别</span>
				</div>
				<div style="float:left;margin:5px;">
					<input type="radio" name="mentor.gender" id="optionsRadios1" value="1" checked/>
  					男&nbsp;&nbsp;&nbsp;&nbsp;
  					<input type="radio"name="mentor.gender" id="optionsRadios1" value="0" />
  					女
				</div>
				<br /><br />
				<div class="input-prepend"   id="add_adress">
  					<span class="add-on">学院</span>
  					<select class="span2" style="width:200px" name="mentor.collegeid" size="1" onchange= "">
						<option disabled="disabled" selected="selected" value="-1" >--------请选择学院--------</option>
						% for li in lis:
						<option value="${li.id}" >${li.name}</option>
						% endfor
					</select>
				</div>
				<span id="checkMentorCollegeid"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">头衔</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.title" placeholder="" />
				</div>
				<span id="checkMentorTitle"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">电话</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.phone" placeholder="" />
				</div>
				<span id="checkMentorPhone"></span>
				<br />
				<div class="input-prepend">
  					<span class="add-on">邮箱</span>
  					<input class="span2" id="prependedInput" type="text" name="mentor.email" placeholder="" />
				</div>
				<span id="checkMentorEmail"></span>
				<br />
				<div >
				描述：
				<br />
				<textarea rows="3" cols="100" style="margin:0 0 0 30px;width:560px;" name="mentor.description"></textarea>
				</div>
				<span id="checkMentorDescription"></span>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="button" onclick="checkMentorAdd()">提交</button>
 				%endif
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>