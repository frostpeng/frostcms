<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>学生列表</title>
<!--                       CSS                       -->
<link rel="stylesheet" type="text/css" href="../../static/css/list.css" />
<!--                       js                        -->
<script src="../../static/bootstrap/js/bootstrap.min.js"></script>
</head>
<body>
<div class="list_head">
	<div class="list_name">&nbsp;&nbsp;&nbsp;学生信息管理</div>
	<div class="head_app">
		<div class="search">
			<!--<p class="search">学生信息&nbsp;</p>-->
			<form class="search" action="/student/list" method="post">
				<p class="search_n">&nbsp;班级&nbsp;</p>
				<input type="text" name="search_clazz" class="search_box" autocomplete="off" value="" />
				<p class="search_n">&nbsp;学号&nbsp;</p>
				<input type="text" name="search_identity" class="search_box" autocomplete="off" value="" />
				<input type="submit" name="submit" class="search_bt" autocomplete="off" value="查询" />
			</form>
		</div>	
		<div class="add">
		<a href="" role="button" data-toggle="modal">添加新学生</a>
		</div>
		<div class="add">
		<a href="">从xls文件导入</a>
		</div>
	</div>	
</div>
</div>
<table class="main_list">
    <thead>
      <tr>
        <th class="number">编号</th>        
        <th class="name">姓名</th>
        <th class="stdn">学号</th>
        <th class="faculty">院系</th>
        <th class="grade">年级</th>
        <th class="class">班级</th>
        <th >操作</th>
      </tr>
    </thead>
<tfoot>
	<tr>
		<td>
		
		</td>
	</tr>
      <tr>
        <td class="tfoot" colspan="7">
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
					<a href="?page=${i}" class="number" title="${i}"> ${i} </a>
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
        <td>${item.identity}</td>
        <td></td>
        <td></td>
       	<td>${item.clazzid}</td>
        <td class="handle"><a href="/student/add?mentorid=${item.id}">修改学生信息</a></td>
      </tr>
      % endfor
    </tbody>
  </table>
  </body>
</html>