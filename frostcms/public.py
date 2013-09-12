# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
import webhelpers.paginate as paginate
from utils import md5

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('public_lesson_list', '/public/lesson_list')
    config.add_route('install','/install')
    
    
@view_config(route_name='public_lesson_list', renderer='public/class_list.mako')
def listlesson(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    startweek=request.params.get('startweek')
    endweek=request.params.get('endweek')
    locationid=request.params.get('locationid')
    area=request.params.get("area")
    locationdictionary=conn.query(Location).order_by(Location.id)
    items=conn.query(Lesson,Location)
    if startweek or endweek or locationid or area:
        if startweek:
            items=items.filter(Lesson.week>=startweek)
        if endweek:
            items=items.filter(Lesson.week<=endweek) 
        if area:
            items=items.filter(and_(Lesson.locationid==Location.id,Location.area==area))
        if locationid:
            items=items.filter(Lesson.locationid==locationid)
        else:
            items=None
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,startweek=startweek,endweek=endweek,
                 locationid=locationid,locationdictionary=locationdictionary)     
    
    
@view_config(route_name='install', renderer='jsonp')
def install(request):
    conn = DBSession()
    admin=conn.query(User).filter(User.name=='admin').first()
    if not admin:
        user=User()
        user.name='admin'
        user.name="admin"
        user.role=0
        user.password=md5("xiaokang") 
        conn.add(user)
        conn.flush()
    return HTTPFound(location=request.route_url('public_lesson_list'))
