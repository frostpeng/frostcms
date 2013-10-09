# coding=utf-8
'''错误代码为4**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
import time
import cgi, uuid
import webhelpers.paginate as paginate
import xlrd
from utils import md5
import cgitb
import os
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
    clazzid, identity = [request.params.get(x,None) for x in ['search_clazz', 'search_identity']]
    items = DBSession().query(Student)
    if identity:
        items = items.filter(Student.identity == identity)
    if clazzid :
        items = items.filter(Student.clazzid == clazzid)
        
    items = items.order_by(Student.identity)
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
    params_tuple=['student.id','student.name','student.identity','student.clazzid']
    student_id,name,identity,clazzid=[request.params.get(x) for x in params_tuple]
    student = conn.query(Student).filter(Student.id == student_id).first()
    if student:
        student.name = name
        student.identity = identity
        student.clazzid = clazzid
        student.updatetime=time.time()
    else :
        student = Student()
        student.name = name
        student.identity = identity
        student.clazzid = clazzid
        student.state=0
        student.createtime=time.time()
        student.updatetime=time.time()
        user = User()
        user.name = identity
#md5加密           
        user.password = md5(identity)
        user.role = 2
        user.regtime=time.time()
        user.logintimes=0
        conn.add(user)
        conn.flush()
        student.userid = user.id
        conn.add(student)
        
    conn.flush()
    return HTTPFound(location=request.route_url('student_list'))
 
@view_config(route_name='student_del', renderer='student/student_add.mako', permission='admin')
def delstudent(request):
    conn = DBSession()
    studentid=request.params.get('studentid',None)
    student = conn.query(Student).filter(Student.id == studentid).first()
    if studentid:
        student = conn.query(Student).filter(Student.id == studentid).first()
        conn.delete(student)
        conn.flush()
        return HTTPFound(location=request.route_url('student_list'))
    return dict(student=student)



@view_config(route_name='student_upload', renderer="student/student_list.mako")
def upload(request):
    upload = request.params.get('file')
    path = "frostcms/upload/exceltmp"
    if not os.path.exists(path):
        os.makedirs(path)
         
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
            operateexcel(filepath)      
    return HTTPFound(location=request.route_url('student_list'))

#excel处理
def operateexcel(filepath=None):
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0] 
    conn = DBSession()
    for rownum in range(1,table.nrows):
        identitynum=table.row(rownum)[0].value.strip()
        name=table.row(rownum)[1].value.strip()
        clazzname=table.row(rownum)[5].value.strip()
        collegename=table.row(rownum)[3].value.strip()
        if(identitynum and name and clazzname and collegename):
            clazznum=clazzname[len(clazzname)-3:len(clazzname)-1]
            year=clazzname[len(clazzname)-7:len(clazzname)-3]
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
            clazz=conn.query(Clazz).filter(and_(and_(Clazz.year==year 
                                           , Clazz.num==clazznum),Clazz.facultyid==faculty.id)).first()
            if not clazz:
                
                clazz=Clazz()
                clazz.year=year
                clazz.num=clazznum
                clazz.facultyid=faculty.id
                clazz.mulfloat=1
                conn.add(clazz)
                 
            clazz=conn.query(Clazz).filter(and_(and_(Clazz.year==year,Clazz.num==clazznum),Clazz.facultyid==faculty.id)).first()
            
            student=conn.query(Student).filter(and_(and_(Student.clazzid==clazz.id ,
                                               Student.name==name),Student.identity==identitynum)).first()
            if not student:
                user=User()
                user.name=identitynum
                user.password=md5(identitynum)
                user.regtime=time.time()
                user.logintimes=0
                user.lastlogin=time.time()
                user.role=2
                conn.add(user)  
                conn.flush()
                student=Student()
                student.clazzid=clazz.id
                student.name=name
                student.identity=identitynum
                student.userid=user.id
                student.state=0
                student.createtime=time.time()
                student.updatetime=time.time()
                conn.add(student)
    conn.flush()
    os.remove(filepath)
#     for root, dirs, files in os.walk("frostcms/upload/exceltmp", topdown=False): 
#          for name in files:
#              os.remove(os.path.join(root, name))
#          for name in dirs:
#              os.rmdir(os.path.join(root, name))
                              
    return None
    
    
