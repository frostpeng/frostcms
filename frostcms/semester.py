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
    config.add_route('semester_list', '/semester/list')
    config.add_route('semester_add', '/semester/add')
    config.add_route('semester_save', '/semester/save')
    config.add_route('semester_del', '/semester/del')
    
@view_config(route_name='semester_list', renderer='semester/semester_list.mako',permission='admin')
def listsemester(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     items = conn.query(Semester).order_by(Semester.id)
     page_url = paginate.PageURL_WebOb(request)
     items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
     return dict(items=items) 
 
@view_config(route_name='semester_add', renderer='semester/semester_add.mako',permission='admin')
def addsemester(request):
     conn = DBSession()
     semester = conn.query(Semester).filter(Semester.id==request.params.get('semesterid')).first()
     return dict(semester=semester)    
 
@view_config(route_name='semester_save', renderer='semester/semester_add.mako',permission='admin')
def savesemester(request):
     conn = DBSession()
     if request.params.get('semester.id'):
          semester = conn.query(Semester).filter(Semester.id==request.params.get('semester.id')).first()
          semester.name=request.params.get('semester.name')
          conn.flush()
          return HTTPFound(location=request.route_url('semester_list'))
     else:
         semester = Semester()
         semester.name = request.params.get('semester.name')

         conn.add(semester)
         return HTTPFound(location=request.route_url('semester_list'))
     return HTTPFound(location=request.route_url('semester_list'))
 
@view_config(route_name='semester_del', renderer='semester/semester_del.mako',permission='admin')
def dellocation(request):
    conn = DBSession()
    semester = conn.query(Semester).filter(Semester.id==request.params.get('semesterid')).first()
    if request.params.get('semester.id'):
        semester = conn.query(Semester).filter(Semester.id==request.params.get('semester.id')).first()
        conn.delete(semester)
        return HTTPFound(location=request.route_url('semester_list'))
    return dict(semester=semester)
