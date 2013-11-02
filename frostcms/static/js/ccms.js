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

function delete_con(text,href){
	if (confirm(text))
		window.location.href=href;
}

function UnicodeToUTF8(strInUni){
	  if(null==strInUni)
	    returnnull;
	  var strUni=String(strInUni);
	  var strUTF8=String();
	  for(var i=0;i<strUni.length;i++){
	    var wchr=strUni.charCodeAt(i);
	    if(wchr<0x80){
	      strUTF8+=strUni.charAt(i);
	      }
	    else if(wchr<0x800){
	      var chr1=wchr&0xff;
	      var chr2=(wchr>>8)&0xff;
	      strUTF8+=String.fromCharCode(0xC0|(chr2<<2)|((chr1>>6)&0x3));
	      strUTF8+=String.fromCharCode(0x80|(chr1&0x3F));
	      }
	    else{
	      var chr1=wchr&0xff;
	      var chr2=(wchr>>8)&0xff;
	      strUTF8+=String.fromCharCode(0xE0|(chr2>>4));
	      strUTF8+=String.fromCharCode(0x80|((chr2<<2)&0x3C)|((chr1>>6)&0x3));
	      strUTF8+=String.fromCharCode(0x80|(chr1&0x3F));
	      }
	    }
	  return strUTF8;
	  }