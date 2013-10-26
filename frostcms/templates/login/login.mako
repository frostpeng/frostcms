<div class="navbar navbar-inverse navbar-fixed-top">
	<div class="navbar-inner">
    <a class="brand" href="" style="font-family:'微软雅黑','黑体';margin:auto auto auto 15px;">实验室管理系统</a>
    <ul class="nav">
    </ul>
    <ul class="nav pull-right">
    % if request.user :
        <li><a href=""><i class="icon-user icon-white" title="修改密码"></i> ${request.getusername.name}</a></li>
        <li><a href="/user/change_password" title="修改密码""><i class="icon-wrench icon-white"></i> 密码</a></li>
        <li><a href="/logout" title="退出登录"><i class="icon-remove icon-white"></i> 退出</a></li>
    % else :
    	<li><button id="btn_login" class="btn btn-primary" type="button">登录</button></li>
    % endif
    	<li><a href=""> </a></li>
    </ul>
  	</div>
</div>
<!--
<div class="head" >
    <div class="title">
   	 实验室管理系统
    </div>
	% if request.user :
	<div class="topNav">
	<ul>
    <a href="#">
      <li>
            <p><i class="icon-user icon-white"></i> ${request.getusername.name}</p>
      </li>
    </a>
    <a href="/user/change_password" title="修改密码">
      <li>
          <p><i class="icon-wrench icon-white"></i> 密码</p>
      </li>
    </a>
    <a href="/logout" title="退出登录">
      <li>
          <p><i class="icon-remove icon-white"></i> 退出</p>
      </li>
    </a>
  </ul>
  </div>
    % else :
    	<button id="btn_login" class="btn btn-primary" type="button">登录</button>
    %endif
</div>
-->
<div class="login" id="login"
% if request:
style="display:none;"
% else :
style=""
% endif
>
	<form class="login" action="" method="post">
    	<div class="frame_login">
    		<button id="btn_close" class="btn btn-danger" type="button">关闭</button>
        	<div class="input-prepend">
  				<span class="add-on">用户名</span>
        		<input type="text" name="username" id="username" autocomplete="off" class="login_box" />
        	</div>
        	<div class="input-prepend">
  				<span class="add-on">密&nbsp;&nbsp;&nbsp;&nbsp;码</span>
            	<input type="password" id="password" name="password" autocomplete="off" class="login_box" />
            </div>
            <div class="check_box">
  				<input type="checkbox" id="remember" autocomplete="off" class="login_age" value="1209600"/>
            	记住用户名？
            </div>	
            <div id="add_error">
     		</div>
     		<div id="login_submit">
     			<input id="login_btn"  class="btn btn-primary"  value="登录" />
     		</div>
        </div>
        
	</form>
</div>
<script>
$(document).ready(function(){
     $("#login_btn").click(function(){
     	$.ajax({
			url:"/api/user/login",
			type: "post",
			data: {username:$('#username').val(), password:$('#password').val(),
				remember:document.getElementById('remember').checked},
			dataType: "json",
			success: function(data){
				if(data.code){
					alert(data.error);
					$("#add_error").html(data.error);
				}else{
				window.location.href =data.return_url;
				}
			},
			error: function(data){
				alert("系统错误，请联系管理员");
			},
			complete: function(){
			}
		});
    });
});
</script>