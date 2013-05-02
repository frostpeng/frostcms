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
    config.add_route('location_list', '/location/list')
    config.add_route('location_add', '/location/add')
    config.add_route('location_save', '/location/save')
    config.add_route('location_del', '/location/del')
    
@view_config(route_name='location_list', renderer='location/location_list.mako',permission='admin')
def listlocation(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     items = conn.query(Location).order_by(Location.id)
     page_url = paginate.PageURL_WebOb(request)
     items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
     return dict(items=items) 
 
@view_config(route_name='location_add', renderer='location/location_add.mako',permission='admin')
def addlocation(request):
     conn = DBSession()
     location = conn.query(Location).filter(Location.id==request.params.get('locationid')).first()
     return dict(location=location)    
 
@view_config(route_name='location_save', renderer='location/location_add.mako',permission='admin')
def savelocation(request):
     conn = DBSession()
     if request.params.get('location.id'):
          location = conn.query(Location).filter(Location.id==request.params.get('location.id')).first()
          location.name=request.params.get('location.name')
          location.address=request.params.get('location.address')
          location.totalrows=request.params.get('location.totalrows')
          location.perrow=request.params.get('location.perrow')
          conn.flush()
          return HTTPFound(location=request.route_url('location_list'))
     else:
         location = Location()
         location.name = request.params.get('location.name')
         location.address = request.params.get('location.address')
         location.totalrows = request.params.get('location.totalrows')
         location.perrow = request.params.get('location.perrow')
         conn.add(location)
         return HTTPFound(location=request.route_url('location_list'))
     return HTTPFound(location=request.route_url('location_list'))
 
@view_config(route_name='location_del', renderer='location/location_del.mako',permission='admin')
def dellocation(request):
    conn = DBSession()
    location = conn.query(Location).filter(Location.id==request.params.get('locationid')).first()
    if request.params.get('location.id'):
        location = conn.query(Location).filter(Location.id==request.params.get('location.id')).first()
        conn.delete(location)
        return HTTPFound(location=request.route_url('location_list'))
    return dict(location=location)

         