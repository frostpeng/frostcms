<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>实验教学管理系统</title>
</head>
<body>
<table>
    <thead>
      <tr>
        <th>编号</th>        
        <th>姓名</th>
        <th>操作</th>
      </tr>
    </thead>
<tfoot>
      <tr>
        <td colspan="5">
        	<div class="bulk-actions align-left">
            <!--<select name="dropdown">
              <option value="0">选择一个操作</option>
              <option value="1">删除</option>
            </select>
            <a class="button" href="#">确定</a>
            -->
          </div>
          <!-- 分页导航 -->         
        	<%include file="/unit/pagination.mako" />
          <!-- End .pagination -->
          <div class="clear"></div>
        </td>
      </tr>
    </tfoot>
    <tbody>
      % for item in items:
      <tr>
        <td>${item.id}</td>
        <td>${item.name}</td>
        <td><a href="/user/resetpsd?userid=${item.id}">重置密码</a></td>
      </tr>
      % endfor
    </tbody>
  </table>
  </body>
</html>