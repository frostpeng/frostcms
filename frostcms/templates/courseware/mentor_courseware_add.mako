<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <script type="text/javascript" src="/static/js/jquery-1.10.2.min.js"></script>
     <script type="text/javascript" src="/static/js/jquery-ui.js"></script>
   <script type="text/javascript" src="/static/js/jquery.validate.min.js"></script>
       <script type="text/javascript" src="/static/js/ajaxfileupload2.js"></script>
	<link href="/static/css/bootstrap.css" rel="stylesheet" media="screen"/>
<link href="/static/css/ccms.css" rel="stylesheet" media="screen"/>
<script src="../../static/js/bootstrap.js"></script>
<script src="../../static/js/ccms.js"></script>
<script src="../../static/js/searchID.js"></script>
<script src="/static/js/datetimepicker.js"></script>
</head>

<body>
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">课件添加</div>
			<a class="btn btn-primary" id="btn_head" href="Javascript:history.back()">返回</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<div class="add">
 				<div class="app_name">
        		添加课件
        		</div>
  				<div class="input-prepend">
  					<span class="add-on">标题</span>
  					<input class="span2" id="title" type="text" name="title"  placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">描述</span>
  					<input class="span2" id="description" type="text" name="description"  placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">附件</span>
  					<button class="btn" onclick="uploadfile.click()">选择文件</button>
					<input type="file" id="uploadfile" name="uploadfile" onchange="fileupload()" style="display:none;vertical-align:middle;height:20px;width:220px;line-height:30px;margin:0;text-aligin:center;" />
					<input type='hidden' id='fsfileid' name='fsfileid' value='${assignmentupload.fsfileid if assignmentupload else u' '} ' />	
				</div>
				<br />
				<div class="input-prepend" id="download_div" type="hidden">
				%if assignmentupload:
					<span class='add-title'>${assignmentupload.fsfile.filename}</span>
					<span class='add-on'>已上传附件</span>
					<span class='add-on'><a href='/user/getfilebyid?fsfileid=${assignmentupload.fsfileid}'>附件下载</a></span>
				%endif
				</div>
				<hr />
				<span id="debug"></span>
 				<button class="btn btn-primary" id="add_submit">保存</button>
 			</div>
        </div>               	
    </div>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>
<script type="text/javascript">
   function fileupload(){
	$.ajaxFileUpload({
			url:"/api/user/uploadfile",
			type: "post",
			secureuri:false,
			fileElementId:['uploadfile'],
			dataType: "json",
			success: function(data){
				//$('.avatarfile_display').attr('src',filesrc);
				//$('.avatarfile_display').attr('style','display:block');
				//$("#pFileid").attr("value",data.fileid);
				if(data.code){
					$("#add_error").html(data.error);
				}else{
				$('#fsfileid').attr('value',data.fsfileid);
				$('#download_div').empty();
				$('#download_div').append("<span class='add-on'>已上传附件: "+data.filename+"</span>")
				$('#download_div').append("<span class='add-on'><a href='/user/getfilebyid?fsfileid="+data.fsfileid+"'>附件下载</a></span>");
				}
			},
			error: function (data,status,e){
				alert("error");
			},
			complete: function(){
			
			}
			
		});};
		
		
$(document).ready(function(){
   	$("#add_submit").click(function(){	
		postdata={'title': $("#title").val(),'description': $("#description").val(),
				'fsfileid': $("#fsfileid").val()};
     	$.ajax({
			url:"/api/mentor/courseware/add",
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