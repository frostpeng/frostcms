<div class="login">
	<form class="frame_login_right" action="" method="post">
    	<div class="frame_login_in">
        	<label for="n" class="login_box_n" >用户名</label>
        	<input type="text" name="username" id="n" autocomplete="off" class="login_box" />
        	<label for="p" class="login_box_p" >密码</label>
            <input type="password" name="password" id="p" autocomplete="off" class="login_box" />
            <br />
            <input type="checkbox" name="max_age" autocomplete="off" class="login_age" value="1209600"/>&nbsp;&nbsp;记住用户名？
            % if error:
	  			<div class="error">
       				${error}
     			</div>
     		% endif
        </div>
        % if request.user.role==0 :
        
    	<a id="btn_logout" class="btn" type="button" href="/logout">${request.user.name}</a>
    	% else :
    	<button id="btn_login" class="btn" type="button">登录</button>
    	% endif
	</form>
</div>