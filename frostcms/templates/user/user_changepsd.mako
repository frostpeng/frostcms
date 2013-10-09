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
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="" class="add"method="post">
 				<div class="app_name">
        		修改密码
        		</div>
        		<div id="add_error">
     			</div>
 				<div class="input-prepend" >
  					<span class="add-on">旧的密码</span>
  					<input class="span2" id="oldpassword" type="password"/>
				</div>
				<br />
				<div class="input-prepend" >
  					<span class="add-on">新的密码</span>
  					<input class="span2" type="password" id="newpassword" />
				</div>
				<br />
 				<div class="input-prepend">
  					<span class="add-on">重复密码</span>
  					<input class="span2" id="repeatpassword" type="password"/>
				</div>
				<br />
 				<button class="btn btn-primary" id="add_submit" type="button">提交</button>
 			</form>
        </div>               
        
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
<script>
$(document).ready(function(){
     $("#add_submit").click(function(){
	 var newpassword=$('#newpassword').val();
     var repeatpassword=$('#repeatpassword').val();
     if(newpassword==repeatpassword){
     	$.ajax({
			url:"/api/user/change_password",
			type: "post",
			data: {oldpassword:$('#oldpassword').val(),newpassword:$('#newpassword').val()},
			dataType: "json",
			success: function(data){
				if(data.code){
					$("#add_error").html(data.error);
				}else{
					$("#add_error").html("密码修改成功");
				}
			},
			error: function(data){
				alert("系统错误，请联系管理员");
			},
			complete: function(){
			}
		});
		}else{
		 $("#add_error").html("两次输入密码不一致！");
		}
    });
});
</script>
</html>
