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
     student = conn.query(Student).filter(Student.id==request.params.get('mentorid')).first()
     return dict(student=student)    
 
@view_config(route_name='student_save', renderer='student/student_add.mako',permission='admin')
def savestudent(request):
     conn = DBSession()
     if request.params.get('student.id'):
          student = conn.query(Student).filter(Student.id==request.params.get('student.id')).first()
          student.name=request.params.get('student.name')
          conn.flush()
          return HTTPFound(location=request.route_url('student_add'))
     return HTTPFound(location=request.route_url('student_add'))