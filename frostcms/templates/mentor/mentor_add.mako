<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>教师列表</title>
</head>
<body>
<form action="/mentor/save">
 %if mentor:
 <input type="hidden" name="mentor.id" value="${mentor.id}"/>
 <p><input name="mentor.name" value="${mentor.name}"/></p>
 %else:
  <p><input name="mentor.name""/></p>
 %endif
 <button type="submit">提交</button>
 </form>
</body>
</html>