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
    config.add_route('public_lesson_list', '/public/lesson_list')
    
    
@view_config(route_name='public_lesson_list', renderer='public/class_list.mako')
def listlesson(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     startweek=request.params.get('startweek')
     endweek=request.params.get('endweek')
     locationid=request.params.get('locationid')
     area=request.params.get("area")
     locationdictionary=conn.query(Location).order_by(Location.id)
     items=conn.query(Lesson)
     if startweek or endweek or locationid:
        if startweek:
             items=items.filter(Lesson.week>=startweek)
        if endweek:
            items=items.filter(Lesson.week<=endweek) 
        if area:
            items=items.filter(Lesson.location.area==area)
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
    
    
