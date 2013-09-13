# coding=utf-8
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
    config.add_route('course_add','/course/add')
    config.add_route('course_save','/course/save')
    
    
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
    return dict(course=course,mentordictionary=mentordictionary,lis=lis,colleges=colleges, facultys=facultys, clazzs=clazzs, infos=infos)    
 
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
