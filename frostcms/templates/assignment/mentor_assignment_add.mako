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
   
</head>

<body>
	<!-- 导航栏部分 -->
    <%include file="/unit/nav.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">作业安排</div>
			% if lesson:
			<a class="btn btn-primary" id="btn_head" href="/mentor/lesson/listbycourse?courseid=${lesson.courseid}"><i class="icon-share-alt icon-white"></i> 课堂列表</a>   			
			% endif
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/lesson/save" class="add" name="course">
        	 	<input type="hidden" name="lesson_id" value="${lesson.id}" />
        	   <br />
				<div class="input-prepend">
  					<span class="add-on">标题</span>
  					<input class="span2" id="title" type="text" name="title" value="${assignment.title if assignment else u''}" placeholder="" />
				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">描述</span>
  					<input class="span4" id="description" type="text" name="description" value="${assignment.description if assignment else u''}" placeholder="" />
  				</div>
				<br />
				<div class="input-prepend">
  					<span class="add-on">附件</span>
					<input class="span2" type="file" id="uploadfile" name="uploadfile" onchange="upload()" style="vertical-align:middle;height:20px;width:220px;line-height:30px;margin:0;text-aligin:center;" />
					<input type='hidden' id='filename' name='filename' value=' ' />
					<input type='hidden' id='filepath' name='filepath' value=' ' />
				</div>
				<div class="input-prepend">
				<input type='hidden' id='download' name='download'/>
				</div>
				<hr />
				<span id="debug"></span>
 				<button class="btn btn-primary" id="add_submit" type="button"><i class="icon-ok icon-white"></i>  提交</button>
 			</form>
        </div>               
        
    </div>
        <script>
function upload(){
	$.ajaxFileUpload({
			url:"/api/user/uploadfile",
			type: "post",
			secureuri:false,
			fileElementId:['uploadfile'],
			data: {path:"assignment"},
			dataType: "json",
			success: function(data){
				//$('.avatarfile_display').attr('src',filesrc);
				//$('.avatarfile_display').attr('style','display:block');
				//$("#pFileid").attr("value",data.fileid);
				if(data.code){
					$("#add_error").html(data.error);
				}else{
				$('#filename').attr('value',data.filename);
				$('#filepath').attr('value',data.filepath);
				$("#download").replaceWith("<a  id='uploadfile' href='" +data.filepath + "' >"+"下载<a/>");
				}
			},
			error: function (data,status,e){
				alert("error");
			},
			complete: function(){
			
			}
			
		});};
		</script>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>