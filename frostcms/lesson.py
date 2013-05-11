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
    config.add_route('lesson_list', '/lesson/list')
    config.add_route('lesson_add', '/lesson/add')
    config.add_route('lesson_save', '/lesson/save')
    config.add_route('lesson_del', '/lesson/del')
    
@view_config(route_name='lesson_list', renderer='lesson/lesson_list.mako',permission='admin')
def listlesson(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     semesters = conn.query(Semester).order_by(Semester.id)
     if request.method == "POST":
         semesterid = request.params.get('semesterid')
         items = conn.query(Lesson,Course).filter(and_(Lesson.courseid==Course.id,Course.semesterid==semesterid))
     else :
         items = conn.query(Lesson).order_by(Lesson.id)
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
 
@view_config(route_name='lesson_add', renderer='lesson/lesson_add.mako',permission='admin')
def addlesson(request):
     conn = DBSession()
     lesson = conn.query(Lesson).filter(Lesson.id==request.params.get('lessonid')).first()
     lists = conn.query(Semester).order_by(Semester.id)
     locations = conn.query(Location).order_by(Location.id)
     courses = conn.query(Course).order_by(Course.id)
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
     return dict(lesson=lesson,lis=lis,locations=locations,courses=courses)    
 
@view_config(route_name='lesson_save', renderer='lesson/lesson_add.mako',permission='admin')
def savelesson(request):
     conn = DBSession()
     if request.params.get('lesson.id'):
          lesson = conn.query(Lesson).filter(Lesson.id==request.params.get('Lesson.id')).first()
          lesson.courseid = request.params.get('lesson.courseid')
          lesson.week = request.params.get('lesson.week')
          lesson.dow = request.params.get('lesson.dow')
          lesson.locationid = request.params.get('lesson.locationid')
          lesson.firstrow = request.params.get('lesson.firstrow')
          lesson.lastrow = request.params.get('lesson.lastrow')
          lesson.ext_firstrow = request.params.get('lesson.ext_firstrow')
          lesson.ext_lastrow = request.params.get('lesson.ext_lastrow')
          lesson.ext_location = request.params.get('lesson.ext_location')
          lesson.starttime = request.params.get('lesson.starttime')
          lesson.endtime = request.params.get('lesson.endtime')
          lesson.monopolize = request.params.get('lesson.monopolize')
          conn.flush()
     else:
         lesson = Lesson()
         lesson.courseid = request.params.get('lesson.courseid')
         lesson.week = request.params.get('lesson.week')
         lesson.dow = request.params.get('lesson.dow')
         lesson.locationid = request.params.get('lesson.locationid')
         lesson.firstrow = request.params.get('lesson.firstrow')
         lesson.lastrow = request.params.get('lesson.lastrow')
         lesson.ext_firstrow = request.params.get('lesson.ext_firstrow')
         lesson.ext_lastrow = request.params.get('lesson.ext_lastrow')
         lesson.ext_location = request.params.get('lesson.ext_location')
         lesson.starttime = request.params.get('lesson.starttime')
         lesson.endtime = request.params.get('lesson.endtime')
         lesson.monopolize = request.params.get('lesson.monopolize')
         conn.add(lesson)
         conn.flush()
     return HTTPFound(location=request.route_url('lesson_list'))
 
@view_config(route_name='lesson_del', renderer='lesson/lesson_del.mako',permission='admin')
def dellesson(request):
    conn = DBSession()
    lesson = conn.query(Lesson).filter(Lesson.id==request.params.get('lessonid')).first()
    if request.params.get('lesson.id'):
        lesson = conn.query(Lesson).filter(Lesson.id==request.params.get('lesson.id')).first()
        conn.delete(lesson)
        conn.flush()
        return HTTPFound(location=request.route_url('lesson_list'))
    lists = conn.query(Semester).order_by(Semester.id)
    locations = conn.query(Location).order_by(Location.id)
    courses = conn.query(Course).order_by(Course.id)
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
    return dict(lesson=lesson,lis=lis,locations=locations,courses=courses)