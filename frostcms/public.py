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
    params_tuple=['startweek','endweek','locationid',"area"]
    startweek,endweek,locationid,area=[request.params.get(x) for x in params_tuple]
    locationdictionary=conn.query(Location).order_by(Location.id)
    items=None
    if startweek or endweek or locationid or area:
        items=conn.query(Lesson)
        if startweek:
            items=items.filter(Lesson.week>=startweek)
        if endweek:
            items=items.filter(Lesson.week<=endweek) 
        if area:
            items=items.filter(Lesson.id.in_(conn.query(Lesson_Location.lessonid).filter\
                    (Lesson_Location.locationid.in_(conn.query(Location.id).filter(Location.area==area)))))
        if locationid:
            items=items.filter(Lesson.id.in_(conn.query(Lesson_Location.lessonid).filter(Lesson_Location.locationid==locationid)))
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
