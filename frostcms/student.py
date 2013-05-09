# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.security import remember, forget
from logging import getLogger
from .models import *
from .token import Token
import time
import cgi, uuid, os
import webhelpers.paginate as paginate
import xlrd
import thread
import hashlib 
import cgitb
cgitb.enable()

log = getLogger(__name__)


def includeme(config):
    config.scan(__name__)
    config.add_route('student_list', '/student/list')
    config.add_route('student_add', '/student/add')
    config.add_route('student_save', '/student/save')
    config.add_route('student_del', '/student/del')
    config.add_route('student_upload', '/student/upload')
    
@view_config(route_name='student_list', renderer='student/student_list.mako', permission='admin')
def liststudent(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     if request.method == "POST":
         clazz, identity = [request.params.get(x, '').strip() for x in ['search_clazz', 'search_identity']]
         if len(identity) > 0 :
             items = conn.query(Student).filter(Student.identity == identity)
         elif len(clazz) > 0 :
             items = conn.query(Student).filter(Student.clazzid == clazz)
     else :
         items = conn.query(Student).order_by(Student.identity)
     page_url = paginate.PageURL_WebOb(request)
     items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
     return dict(items=items) 
 
@view_config(route_name='student_add', renderer='student/student_add.mako', permission='admin')
def addstudent(request):
     conn = DBSession()
     class infoClazz():
         def __init__(self):
             college = ""
             faculty = ""
             clazz = ""
             collegeNum = 0
             facultyNum = 0
             clazzNum = 0 
     infos = []
     info = infoClazz()
     info.college = ""
     info.faculty = ""
     info.clazz = ""
     info.collegeNum = 0
     info.facultyNum = 0
     info.clazzNum = 0 
     student = conn.query(Student).filter(Student.id == request.params.get('studentid')).first()
     colleges = conn.query(College).order_by(College.id)
     facultys = conn.query(Faculty).order_by(Faculty.id)
     clazzs = conn.query(Clazz).order_by(Clazz.id)
     for college in colleges :
         if college.id > info.collegeNum :
             info.collegeNum = college.id
     for faculty in facultys :
         if faculty.id > info.facultyNum :
             info.facultyNum = faculty.id
     infos.append(info)
     return dict(student=student, colleges=colleges, facultys=facultys, clazzs=clazzs, infos=infos)    
 
@view_config(route_name='student_save', renderer='student/student_add.mako', permission='admin')
def savestudent(request):
     conn = DBSession()
     if request.params.get('student.id'):
          student = conn.query(Student).filter(Student.id == request.params.get('student.id')).first()
          student.name = request.params.get('student.name')
          student.identity = request.params.get('student.identity')
          student.clazzid = request.params.get('clazzid')
          conn.flush()
     else :
          student = Student()
          student.name = request.params.get('student.name')
          student.identity = request.params.get('student.identity')
          student.clazzid = request.params.get('clazzid')
          user = User()
          user.name = student.identity
#md5加密           
          user.password = hashlib.new("md5",student.identity).hexdigest()
          user.role = 2
          conn.add(user)
          conn.flush()
          cc = conn.query(User).filter(User.name == student.identity).first()
          student.account = cc.id
          conn.add(student)
          conn.flush()
     return HTTPFound(location=request.route_url('student_list'))
 
@view_config(route_name='student_del', renderer='student/student_del.mako', permission='admin')
def delstudent(request):
     conn = DBSession()
     student = conn.query(Student).filter(Student.id == request.params.get('studentid')).first()
     if request.params.get('student.id'):
         student = conn.query(Student).filter(Student.id == request.params.get('student.id')).first()
         conn.delete(student)
         conn.flush()
         return HTTPFound(location=request.route_url('student_list'))
     return dict(student=student)



@view_config(route_name='student_upload', renderer="student/student_list.mako")
def upload(request):
    upload = request.params.get('file')
    path = "frostcms/upload/exceltmp"
    if isinstance(upload, cgi.FieldStorage) and upload.file:
        extension = upload.filename.split('.')[-1:][0]  
        if extension == "xls" or extension == "xlsx":
               filename = "%s.%s" % (uuid.uuid1(), extension)
               filepath = os.path.join(path, filename).replace("\\", "/")
               myfile = open(filepath, 'wb')
               upload.file.seek(0)
               while 1:
                   tmp = upload.file.read(2 << 16)
                   if not tmp:
                       break
                   myfile.write(tmp)
               myfile.close()
#                新开线程处理excel
               thread.start_new_thread(operateexcel, (filepath,))     
    return HTTPFound(location=request.route_url('student_list'))

#excel处理
def operateexcel(filepath=None):
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0] 
    conn = DBSession()
    for rownum in range(0,table.nrows):
        identitynum=table.row(rownum)[0].value.strip()
        name=table.row(rownum)[1].value.strip()
        clazzname=table.row(rownum)[2].value.strip()
        collegename=table.row(rownum)[4].value.strip()
        log.debug(identitynum+" "+name+" "+clazzname+" "+collegename)
        if(identitynum and name and clazzname and collegename):
            clazznum=clazzname[len(clazzname)-3:len(clazzname)-1]
            grade=clazzname[len(clazzname)-7:len(clazzname)-3]
            facultyname=clazzname[0:len(clazzname)-7]
            college=conn.query(College).filter(College.name==collegename).first()
            if not college:
                 college = College()
                 college.name =collegename
                 conn.add(college)

            college=conn.query(College).filter(College.name==collegename).first()
            
           
            faculty=conn.query(Faculty).filter(and_(Faculty.name==facultyname,Faculty.collegeid==college.id)).first()
            if not faculty:
                 faculty = Faculty()
                 faculty.name = facultyname
                 faculty.collegeid=college.id
                 conn.add(faculty)
                   
            faculty=conn.query(Faculty).filter(and_(Faculty.name==facultyname ,Faculty.collegeid==college.id)).first()
            clazz=conn.query(Clazz).filter(and_(and_(Clazz.grade==grade 
                                           , Clazz.num==clazznum),Clazz.facultyid==faculty.id)).first()
            if not clazz:
                
                clazz=Clazz()
                clazz.grade=grade
                clazz.num=clazznum
                clazz.facultyid=faculty.id
                conn.add(clazz)
                 
            clazz=conn.query(Clazz).filter(and_(and_(Clazz.grade==grade,Clazz.num==clazznum),Clazz.facultyid==faculty.id)).first()
            
            student=conn.query(Student).filter(and_(and_(Student.clazzid==clazz.id ,
                                               Student.name==name),Student.identity==identitynum)).first()
            if not student:
                user=conn.query(User).filter(and_(User.name==identitynum,User.role==2)).first()
                if not user:
                    user=User()
                    user.name=identitynum
                    user.password=hashlib.new("md5",identitynum).hexdigest()
                    user.regtime=time.time()
                    user.logintimes=0
                    user.lastlogin=time.time()
                    user.role=2
                    conn.add(user)
                    
                user=conn.query(User).filter(and_(User.name==identitynum,User.role==2)).first()
                student=Student()
                student.clazzid=clazz.id
                student.name=name
                student.identity=identitynum
                student.account=user.id
                conn.add(student)
    
    conn.flush()                  
    return None
    
    
