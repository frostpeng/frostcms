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
          <div class="pagination">
          	  % if items.first_page:
	          <a href="?page=${items.first_page}" title="第一页">&laquo; 第一页</a>
	          % endif
	          % if items.previous_page:
	          <a href="?page=${items.previous_page}" title="上一页">&laquo; 上一页</a> 
	          % endif
	          % for i in range(items.page - 3,items.page):
			  	% if items.page_count>0 and i>=items.first_page:
					<a href="?page=${i}" class="number" title="${i}">${i}</a>
				% endif
			  % endfor
	          <a href="#" class="number current" title="${items.page}">${items.page}</a> 
	          % for i in range(items.page+1, items.page + 3):
			  	% if items.page_count>0 and i<=items.last_page:
					<a href="?page=${i}" class="number" title="${i}">${i}</a>
			  	% endif
			  % endfor
			  % if items.next_page:
			  	<a href="?page=${items.next_page}" title="下一页">下一页 &raquo;</a>
			  % endif
			  % if items.last_page:
	          <a href="?page=${items.last_page}" title="最后一页">最后一页 &raquo;</a> 
	          % endif
          </div>
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