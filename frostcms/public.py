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
    config.add_route('public_class_list', '/public/class_list')
    
    
@view_config(route_name='public_class_list', renderer='public/class_list.mako')
def listsemester(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     startWeek=request.params.get('startweek')
     endWeek=request.params.get('endweek')
     locationid=request.params.get('locationid')
     locationdictionary=conn.query(Location).order_by(Location.id)
     maxWeek=conn.query(Semester).filter((Semester.start+Semester.weeks*7*60*60*24)>time.time()).first()  
     print time.time()
     if startWeek and endWeek and locationid:
         items=conn.query(Lesson)
         if startWeek:
             items=items.filter(Lesson.week>startWeek)
         if endWeek:
             items=items.filter(Lesson.week<endWeek)
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
     return dict(items=items,startWeek=startWeek,endWeek=endWeek,locationid=locationid,
                 maxWeek=maxWeek,locationdictionary=locationdictionary)     
    
    
