# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
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
    locationid=request.params.get('locationid')
    location = conn.query(Location).filter(Location.id==locationid).first()
    return dict(location=location)    
 
@view_config(route_name='location_save', renderer='location/location_add.mako',permission='admin')
def savelocation(request):
    conn = DBSession()
    params_tuple=['location.id','location.name','location.address',\
                  'location.totalrows','location.perrow','location.area','location.seatnum']
    locationid,name,address,totalrows,perrow,area,seatnum=[request.params.get(x) for x in params_tuple]
    location = conn.query(Location).filter(Location.id==locationid).first()
    if location:
        location.name=name
        location.address=name
        location.totalrows=totalrows
        location.perrow=perrow
        location.area=area
        location.seatnum=seatnum
    else:
        location = Location()
        location.name=name
        location.address=name
        location.totalrows=totalrows
        location.perrow=perrow
        location.area=area
        location.seatnum=seatnum
        conn.add(location)
    conn.flush()
    return HTTPFound(location=request.route_url('location_list'))
 
@view_config(route_name='location_del', renderer='location/location_del.mako',permission='admin')
def dellocation(request):
    conn = DBSession()
    locationid=request.params.get('location.id')
    location = conn.query(Location).filter(Location.id==request.params.get('locationid')).first()
    if location:
        conn.delete(location)
        conn.flush()
    return HTTPFound(location=request.route_url('location_list'))