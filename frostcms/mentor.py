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
    config.add_route('mentor_list', '/mentor/list')
    config.add_route('mentor_add', '/mentor/add')
    config.add_route('mentor_save', '/mentor/save')
    
@view_config(route_name='mentor_list', renderer='mentor/mentor_list.mako',permission='admin')
def listmentor(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     if request.method == "POST":
         collegeid = request.params.get('collegeid')
         items = conn.query(Mentor).filter(Mentor.collegeid==collegeid)
     else :
         items = conn.query(Mentor).order_by(Mentor.id)
     lis = conn.query(College).order_by(College.id)
     page_url = paginate.PageURL_WebOb(request)
     items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
     return dict(items=items,lis=lis) 
 
@view_config(route_name='mentor_add', renderer='mentor/mentor_add.mako',permission='admin')
def addmentor(request):
     conn = DBSession()
     mentor = conn.query(Mentor).filter(Mentor.id==request.params.get('mentorid')).first()
     return dict(mentor=mentor)    
 
@view_config(route_name='mentor_save', renderer='mentor/mentor_add.mako',permission='admin')
def savementor(request):
     conn = DBSession()
     if request.params.get('mentor.id'):
          mentor = conn.query(Mentor).filter(Mentor.id==request.params.get('mentor.id')).first()
          mentor.name=request.params.get('mentor.name')
          conn.flush()
          return HTTPFound(location=request.route_url('mentor_add'))
     return HTTPFound(location=request.route_url('mentor_add'))
 