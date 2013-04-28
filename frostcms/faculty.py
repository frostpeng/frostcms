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
    config.add_route('faculty_list', '/faculty/list')
    config.add_route('faculty_add', '/faculty/add')
    config.add_route('faculty_save', '/faculty/save')
    
@view_config(route_name='faculty_list', renderer='faculty/faculty_list.mako',permission='admin')
def listmentor(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     items = conn.query(Faculty).order_by(Faculty.id)
     colleges = conn.query(College).order_by(College.id)
     page_url = paginate.PageURL_WebOb(request)
     items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
     return dict(items=items) 
 
@view_config(route_name='faculty_add', renderer='faculty/faculty_add.mako',permission='admin')
def addmentor(request):
     conn = DBSession()
     faculty = conn.query(Faculty).filter(Faculty.id==request.params.get('mentorid')).first()
     return dict(faculty=faculty)    
 
@view_config(route_name='faculty_save', renderer='faculty/faculty_add.mako',permission='admin')
def savementor(request):
     conn = DBSession()
     if request.params.get('mentor.id'):
          faculty = conn.query(Faculty).filter(Faculty.id==request.params.get('faculty.id')).first()
          faculty.name=request.params.get('faculty.name')
          conn.flush()
          return HTTPFound(location=request.route_url('faculty_add'))
     return HTTPFound(location=request.route_url('facultyr_add'))