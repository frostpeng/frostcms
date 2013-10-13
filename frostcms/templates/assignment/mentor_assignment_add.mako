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
			<div class="title_2">作业安排</div>
			% if lesson:
			<a class="btn btn-primary" id="btn_head" href="/mentor/lesson/listbycourse?courseid=${lesson.courseid}"><i class="icon-share-alt icon-white"></i> 课堂列表</a>   			
			% endif
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/lesson/save" class="add" name="course">
        	 	<input type="hidden" id="lessonid" name="lessonid" value="${lesson.id}" />
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
				<fieldset>
            		<div class="control-group">
                		<label class="control-label"></label>
                		<div class="controls input-prepend input-append date form_datetime" id="datetimepicker" data-date="2013-09-01" data-date-format="yyyy-MM-dd">
                   		<span class="add-on">截止时间</span>
                    		<input class="span2" id="duedate" name="duedate" size="16" type="text" value="2013-09-01">
    							<span class="add-on"><i class="icon-remove"></i></span>
   								 <span class="add-on"><i class="icon-th"></i></span>
                		</div>
						<input type="hidden" id="dtp_input1" value="" />
						<span id="checkSemesterStart"></span>
            		</div>		
        		</fieldset>		
				<br />
				<div class="input-prepend">
  					<span class="add-on">附件</span>
					<input class="span2" type="file" id="uploadfile" name="uploadfile" onchange="fileupload()" style="vertical-align:middle;height:20px;width:220px;line-height:30px;margin:0;text-aligin:center;" />
					<input type='hidden' id='fsfileid' name='fsfileid' value=' ' />	
				</div>
				<br />
				<div class="input-prepend" id="download_div" type="hidden">
				</div>
				<hr />
				<span id="debug"></span>
 				<button class="btn btn-primary" id="add_submit" type="button"><i class="icon-ok icon-white"></i>  提交</button>
 			</form>
        </div>               
 <script>
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
				$('#download_div').append("<span class='add-on'>上传完成</span>")
				$('#download_div').append("<span class='add-on'><a href='/user/getfilebyid?fsfileid="+data.fsfileid+"'>附件下载</a></span>");
				}
			},
			error: function (data,status,e){
				alert("error");
			},
			complete: function(){
			
			}
			
		});};
		</script>         
    </div>
   <script type="text/javascript">
    		$('.form_datetime').datetimepicker({
        		language:'zh-CN',
        		weekStart:0,
        		format:'yyyy-mm-dd',
        		todayBtn:0,
        		daysOfWeekDisabled:'',
				autoclose:1,
				todayHighlight:1,
				startView:2,
				minView:2,
				forceParse:0,
        		showMeridian:1
   	 		});
   	 		$(document).ready(function(){
   	 		$("#add_submit").click(function(){	
     	$.ajax({
			url:"/api/mentor/assignment/add",
			type: "post",
			data: {'title': $("#title").val(),'description': $("#description").val(),
				'duedate': $("#duedate").val(),'fsfileid': $("#fsfileid").val(),
				'lessonid': $("#lessonid").val()},
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
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
</body>
</html>