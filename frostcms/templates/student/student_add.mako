<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>学生列表</title>
</head>
<body>
学生信息修改
<form action="/sudent/save">
 %if student:
 <input type="hidden" name="sudent.id" value="${student.id}"/>
 <p><input name="student.name" value="${student.name}"/></p>
 %else:
  <p><input name="mentor.name""/></p>
 %endif
 <button type="submit">提交</button>
 </form>
</body>
</html>