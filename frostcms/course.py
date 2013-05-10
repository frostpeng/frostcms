# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.security import remember, forget
from logging import getLogger
from .models import *
from .token import Token
import time
import cgi, uuid
import webhelpers.paginate as paginate
from datetime import *  
import time

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('course_list', '/course/list')
    config.add_route('course_add','/course/add')
    config.add_route('course_save','/course/save')
    
@view_config(route_name='course_list', renderer='course/course_list.mako',permission='admin')
def listcourse(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     semesters = conn.query(Semester).order_by(Semester.id)
     if request.method == "POST":
         semesterid = request.params.get('semesterid')
         items = conn.query(Course).filter(Course.semesterid==semesterid).order_by(Course.id)
     else :
         items = conn.query(Course).order_by(Course.id)
     lists = conn.query(Semester).order_by(Semester.id)
     lis = []
     class List_semester():
         def __init__(self):
             self.id = 0
             self.name = ""
             self.time = ""
             self.weeks = 0
     for list in lists:
         t = List_semester()
         t.id = list.id
         t.time = date.fromtimestamp(list.start)
         t.weeks = list.weeks
         time = t.time
         name = str(time.year)
         mon = time.month
         if  mon >7 :
             name += "年秋季"
         else :
             name += "年春季"
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
     course = conn.query(Course).filter(Course.id==request.params.get('courseid')).first()
     lists = conn.query(Semester).order_by(Semester.id)
     mentordictionary=conn.query(Mentor).order_by(Mentor.id)
     lis = []
     class List_semester():
         def __init__(self):
             self.id = 0
             self.name = ""
             self.time = ""
             self.weeks = 0
     for list in lists:
         t = List_semester()
         t.id = list.id
         t.time = date.fromtimestamp(list.start)
         t.weeks = list.weeks
         time = t.time
         name = str(time.year)
         mon = time.month
         if  mon >7 :
             name += "年秋季"
         else :
             name += "年春季"
         t.name = name 
         lis.append(t)
     return dict(course=course,mentordictionary=mentordictionary,lis=lis)    
 
@view_config(route_name='course_save', renderer='course/course_add.mako',permission='admin')
def savecourse(request):
     conn = DBSession()
     if request.params.get('course.id'):
          course = conn.query(Course).filter(Course.id==request.params.get('course.id')).first()
          course.name = request.params.get('course.name')
          course.mentorid = request.params.get('course.mentorid')
          course.semesterid=request.params.get('course.semesterid')
          conn.flush()
     else:
         course = Course()
         course.name = request.params.get('course.name')
         course.mentorid = request.params.get('course.mentorid')
         course.semesterid = request.params.get('course.semesterid')
         conn.add(course)
         conn.flush()
     return HTTPFound(location=request.route_url('course_list'))