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
			<div class="title_2">批改作业</div>
			<a class="btn btn-primary" id="btn_head" href="Javascript:history.back()"><i class="icon-share-alt icon-white"></i>返回</a>
			<button class="btn btn-primary" id="add_submit" type="button"><i class="icon-ok icon-white"></i>打分</button>
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
            <input type="hidden" id="assignmentid" name="assignmentid" value="${request.params.get('assignmentid')}" />
        	<table class="table table-bordered table-hover" id="main_table">
            <thead>
      			<tr>     
        			<th class="name">学号</th>
        			<th class="name">姓名</th>
        			<th class="name">作业详情</th>
        			<th class="name">操作</th>
      			</tr>
    		</thead>
            <tbody>
      			% for item in items:
      			<tr>
        			<td class="name">
        			<a  href='/mentor/assignment/add'>${item.student.identity}</a>
        			</td>
        			<td class="name">
       ${item.student.name}
        			</td>
        			<td class="name">
        			<a class="btn btn-info" href='/user/getfilebyid?fsfileid=${item.fsfileid}'>作业下载</a>
        		   </td>
        			<td class="name">
        			<input class="span2" id="mark" type="text" onchange="markupload(event,${item.id})" name="mark" value="${'%.1f'%(item.mark)}" />
        			</td>
      			</tr>
      			% endfor
    		</tbody>
            </table>
            <!-- 分页导航 -->         
        	<%include file="/unit/pagination.mako" />
        </div>               
        <script>
function markupload(e,uploadid){
    var src = e.target || window.event.srcElement;
   	postdata={'uploadid': uploadid,'mark':src.value};
	$.ajax({
			url:"/api/mentor/assignment/markupload",
			type: "post",
			data:postdata,
			dataType: "json",
			success: function(data){
				if(data.code){
					alert(data.error);
					$("#add_error").html(data.error);
				}else{
				//window.location.href =data.return_url;
				}
			},
			error: function(data){
				alert("系统错误，请联系管理员");
			},
			complete: function(){
			}
		});
		}

$(document).ready(function(){
    $("#add_submit").click(function(){  
        postdata={'assignmentid': $("#assignmentid").val()};
        $.ajax({
            url:"/api/mentor/assignment/overmark",
            type: "post",
            data: postdata,
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
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>