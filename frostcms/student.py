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

log = getLogger(__name__)


def includeme(config):
    config.scan(__name__)
    config.add_route('student_list', '/student/list')
    config.add_route('student_add', '/student/add')
    config.add_route('student_save', '/student/save')
    config.add_route('student_del', '/student/del')
    
@view_config(route_name='student_list', renderer='student/student_list.mako',permission='admin')
def liststudent(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     if request.method == "POST":
         clazz, identity = [request.params.get(x, '').strip() for x in ['search_clazz', 'search_identity']]
         if len(identity)>0 :
             items = conn.query(Student).filter(Student.identity==identity)
         elif len(clazz)>0 :
             items = conn.query(Student).filter(Student.clazzid==clazz)
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
 
@view_config(route_name='student_add', renderer='student/student_add.mako',permission='admin')
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
     student = conn.query(Student).filter(Student.id==request.params.get('studentid')).first()
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
     return dict(student=student,colleges=colleges,facultys=facultys,clazzs=clazzs,infos=infos)    
 
@view_config(route_name='student_save', renderer='student/student_add.mako',permission='admin')
def savestudent(request):
     conn = DBSession()
     if request.params.get('student.id'):
          student = conn.query(Student).filter(Student.id==request.params.get('student.id')).first()
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
          user.password = student.identity
          user.role = 2
          conn.add(user)
          cc = conn.query(User).filter(User.name==student.identity).first()
          student.account = cc.id
          conn.add(student)
     return HTTPFound(location=request.route_url('student_list'))
 
@view_config(route_name='student_del', renderer='student/student_del.mako',permission='admin')
def delstudent(request):
     conn = DBSession()
     student = conn.query(Student).filter(Student.id==request.params.get('studentid')).first()
     if request.params.get('student.id'):
         student = conn.query(Student).filter(Student.id==request.params.get('student.id')).first()
         conn.delete(student)
         return HTTPFound(location=request.route_url('student_list'))
     return dict(student=student)