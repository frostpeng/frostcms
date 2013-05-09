<div class="head">
    <div class="title">
    实验室管理系统
    </div>
    % if request.user :
    <button id="btn_logout" class="btn" type="button">${request.user.name}</button>
    % else :
    <button id="btn_login" class="btn" type="button">登录</button>
    % endif
</div>
