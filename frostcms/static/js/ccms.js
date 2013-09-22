// JavaScript Document
$("div").ready(function(){
  		$("#btn_close").click(function(){
  			$("#login").hide(600);
  		});
  		$("#btn_login").click(function(){
  			$("#login").show(600);
  		});
	});

function notice_page(workid){
	window.location.href="/lesson/notice/watch?workid="+workid;
}