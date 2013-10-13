# coding=utf-8
'''错误代码为12**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
#DBSession,Course,Semester,Mentor
import time
import webhelpers.paginate as paginate
from datetime import date  

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('course_list', '/course/list')
    config.add_route('mentor_course_list', '/mentor/course/list')
    config.add_route('student_course_list', '/student/course/list')
    config.add_route('course_add','/course/add')
    config.add_route('mentor_course_add','/mentor/course/add')
    config.add_route('course_save','/course/save')
    config.add_route('mentor_course_save','/mentor/course/save')
    config.add_route('course_del','/course/del')
    config.add_route('mentor_course_del','/mentor/course/del')
    
    
class List_semester():
    def __init__(self):
        self.id = 0
        self.name = ""
        self.time = ""
        self.weeks = 0
    
@view_config(route_name='course_list', renderer='course/course_list.mako',permission='admin')
def listcourse(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    if request.method == "POST":
        semesterid = request.params.get('semesterid')
        items = conn.query(Course).filter(Course.semesterid==semesterid).order_by(Course.id)
    else :
        items = conn.query(Course).order_by(Course.id)
    semesters = conn.query(Semester).order_by(Semester.id)
    lis = []
    for semester in semesters:
        t = List_semester()
        t.id = semester.id
        t.time = date.fromtimestamp(semester.start)
        t.weeks = semester.weeks
        time = t.time
        name = str(time.year)
        mon = time.month
        if  mon >7 :
            name += u"年秋季"
        else :
            name += u"年春季"
        t.name = name 
        lis.append(t)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,lis=lis)

@view_config(route_name='student_course_list', renderer='course/student_course_list.mako',permission='student')
def student_course_list(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    semesterid = request.params.get('semesterid')
    userid=request.user.id
    student=conn.query(Student).filter(Student.userid==userid).first()
    if semesterid:
        items = conn.query(Course).filter(Course.semesterid==semesterid,Course.id.in_
                (conn.query(Course_Class.courseid).filter(Course_Class.clazzid==student.clazzid))).order_by(Course.id)
    else :
        items = conn.query(Course).filter(Course.id.in_(conn.query(Course_Class.courseid).filter(\
                    Course_Class.clazzid==student.clazzid))).order_by(Course.id)
    semesters = conn.query(Semester).order_by(Semester.id)
    lis = []
    for semester in semesters:
        t = List_semester()
        t.id = semester.id
        t.time = date.fromtimestamp(semester.start)
        t.weeks = semester.weeks
        time = t.time
        name = str(time.year)
        mon = time.month
        if  mon >7 :
            name += u"年秋季"
        else :
            name += u"年春季"
        t.name = name 
        lis.append(t)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,lis=lis)

@view_config(route_name='mentor_course_list', renderer='course/mentor_course_list.mako',permission='mentor')
def mentor_course_list(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    semesterid = request.params.get('semesterid')
    if semesterid:
        items = conn.query(Course).filter(Course.semesterid==semesterid,Course.mentorid.in_
                (conn.query(Mentor.id).filter(Mentor.userid==request.user.id).first())).order_by(Course.id)
    else :
        items = conn.query(Course).filter(Course.mentorid.in_(conn.query(Mentor.id).filter(Mentor.userid==request.user.id).first())).order_by(Course.id)
    semesters = conn.query(Semester).order_by(Semester.id)
    lis = []
    for semester in semesters:
        t = List_semester()
        t.id = semester.id
        t.time = date.fromtimestamp(semester.start)
        t.weeks = semester.weeks
        time = t.time
        name = str(time.year)
        mon = time.month
        if  mon >7 :
            name += u"年秋季"
        else :
            name += u"年春季"
        t.name = name 
        lis.append(t)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,lis=lis)
 
 
@view_config(route_name='course_add', renderer='course/course_add.mako',permission='admin')
def addcourse(request):
    conn = DBSession()
    #colleges = conn.query(College).order_by(College.id)
    #facultys = conn.query(Faculty).order_by(Faculty.id)
    #clazzs = conn.query(Clazz).order_by(Clazz.id)
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
    course = conn.query(Course).filter(Course.id==request.params.get('courseid')).first()
    semesters = conn.query(Semester).order_by(Semester.id)
    mentordictionary=conn.query(Mentor).order_by(Mentor.id)
    lis = []
    for semester in semesters:
        t = List_semester()
        t.id = semester.id
        t.time = date.fromtimestamp(semester.start)
        t.weeks = semester.weeks
        time = t.time
        name = str(time.year)
        mon = time.month
        if  mon >7 :
            name += u"年秋季"
        else :
            name += u"年春季"
        t.name = name 
        lis.append(t)
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
    if request.method == "GET":
        courseid = request.params.get('courseid')
        ClassInCourse = conn.query(Course_Class).filter(Course_Class.courseid==courseid).order_by(Course_Class.id)
    else :
        ClassInCourse = []
    return dict(course=course,mentordictionary=mentordictionary,lis=lis,colleges=colleges, facultys=facultys, clazzs=clazzs, infos=infos,ClassInCourse=ClassInCourse)    

@view_config(route_name='mentor_course_add', renderer='course/mentor_course_add.mako',permission='mentor')
def mentor_course_add(request):
    conn = DBSession()
    #colleges = conn.query(College).order_by(College.id)
    #facultys = conn.query(Faculty).order_by(Faculty.id)
    #clazzs = conn.query(Clazz).order_by(Clazz.id)
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
    course = conn.query(Course).filter(Course.id==request.params.get('courseid')).first()
    semesters = conn.query(Semester).order_by(Semester.id)
    mentordictionary=conn.query(Mentor).order_by(Mentor.id)
    lis = []
    for semester in semesters:
        t = List_semester()
        t.id = semester.id
        t.time = date.fromtimestamp(semester.start)
        t.weeks = semester.weeks
        time = t.time
        name = str(time.year)
        mon = time.month
        if  mon >7 :
            name += u"年秋季"
        else :
            name += u"年春季"
        t.name = name 
        lis.append(t)
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
    if request.method == "GET":
        courseid = request.params.get('courseid')
        ClassInCourse = conn.query(Course_Class).filter(Course_Class.courseid==courseid).order_by(Course_Class.id)
    else :
        ClassInCourse = []
    return dict(course=course,mentordictionary=mentordictionary,lis=lis,colleges=colleges, facultys=facultys, clazzs=clazzs, infos=infos,ClassInCourse=ClassInCourse)  
 
 
 
@view_config(route_name='course_save', renderer='course/course_add.mako',permission='admin')
def savecourse(request):
    conn = DBSession()
    courseid=request.params.get('course.id')
    clazzlist=request.params.getall('clazzid')
    course = conn.query(Course).filter(Course.id==courseid).first()
    if course:
        course.name = request.params.get('course.name')
        course.mentorid = request.params.get('course.mentorid')
        course.semesterid=request.params.get('course.semesterid')
        conn.query(Course_Class).filter(Course_Class.courseid==courseid).delete()
    else:
        course = Course()
        course.name = request.params.get('course.name')
        course.mentorid = request.params.get('course.mentorid')
        course.semesterid = request.params.get('course.semesterid')
        conn.add(course)
        
    conn.flush()
    #add clazz
    for clazzid in clazzlist:
        course_class=Course_Class()
        course_class.courseid=course.id
        course_class.clazzid=clazzid
        conn.add(course_class)
        
    conn.flush()
    return HTTPFound(location=request.route_url('course_list'))

@view_config(route_name='mentor_course_save', renderer='course/mentor_course_add.mako',permission='mentor')
def mentor_course_save(request):
    conn = DBSession()
    params_tuple=['course.id','course.name','course.semesterid']
    courseid,name,semesterid=[request.params.get(x) for x in params_tuple]
    clazzlist=request.params.getall('clazzid')
    course = conn.query(Course).filter(Course.id==courseid).first()
    mentor=conn.query(Mentor).filter(Mentor.userid==request.user.id).first()
    if course:
        course.name = name
        course.mentorid = mentor.id
        course.semesterid=semesterid
        conn.query(Course_Class).filter(Course_Class.courseid==courseid).delete()
    else:
        course = Course()
        course.name = name
        course.mentorid = mentor.id
        course.semesterid=semesterid
        conn.add(course)
        
    conn.flush()
    #add clazz
    for clazzid in clazzlist:
        course_class=Course_Class()
        course_class.courseid=course.id
        course_class.clazzid=clazzid
        conn.add(course_class)
        
    conn.flush()
    return HTTPFound(location=request.route_url('mentor_course_list'))

@view_config(route_name='mentor_course_del', renderer='course/mentor_course_del.mako',permission='mentor')
def mentor_course_del(request):
    conn=DBSession()
    courseid=request.params.get('courseid')
    course=conn.query(Course).filter(Course.id==courseid,Course.mentorid.in_(\
                    conn.query(Mentor.id).filter(Mentor.userid==request.user.id))).first()
    if course:
        conn.query(Course).filter(Course.id==courseid).delete()
    return HTTPFound(location=request.route_url('mentor_course_list'))

