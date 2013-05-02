<div class="head">
    <div class="title">
   	 实验室管理系统
    </div>
	<button id="btn_login" class="btn" type="button">登录</button>
</div>
<div class="login" id="login">
	
	<form class="login" action="" method="post">
    	<div class="frame_login">
    		<button id="btn_close" class="btn btn-danger" type="button">关闭</button>
        	<div class="input-prepend">
  				<span class="add-on">用户名</span>
        		<input type="text" name="username" id="n" autocomplete="off" class="login_box" />
        	</div>
        	<div class="input-prepend">
  				<span class="add-on">密&nbsp;&nbsp;&nbsp;&nbsp;码</span>
            	<input type="password" name="password" autocomplete="off" class="login_box" />
            </div>
            <div class="check_box">
  				<input type="checkbox" name="max_age" autocomplete="off" class="login_age" value="1209600"/>
            	记住用户名？
            </div>	
            % if error:
	  			<div class="error">
       				${error}
     			</div>
     		% endif
     		<div id="login_submit">
     			<input type="submit" name="submit" class="btn btn-primary"  value="登录" />
     		</div>
        </div>
        
	</form>
</div>