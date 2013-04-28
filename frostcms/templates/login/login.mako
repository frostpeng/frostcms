<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>实验教学管理系统</title>
<!--                       CSS                       -->
<link rel="stylesheet" type="text/css" href="static/css/for_login.css"/>
<!--                       Javascripts                       -->
</head>

<body>
<div class="frame_login">
	<div class="frame_login_left">
    	<div class="frame_logo">后台管理登录</div>

    </div>
    <div class="frame_blank"></div>
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
        <input type="submit" name="submit" class="login_submit" value="登录" />
    </form>
</div>
</body>
</html>
