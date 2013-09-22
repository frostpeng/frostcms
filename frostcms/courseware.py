# coding=utf-8
from pyramid.view import view_config
import formencode
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
import time
import webhelpers.paginate as paginate
from datetime import date  

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('mentor_courseware_list', '/mentor/courseware/list')
    config.add_route('mentor_courseware_add', '/mentor/courseware/add')
    
@view_config(route_name='mentor_courseware_list', renderer='courseware/mentor_courseware_list.mako',permission='mentor')
def mentor_courseware_list(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    userid=request.user.id
    items=conn.query(Courseware).filter(Courseware.mentorid in (conn.query(Mentor.id)\
                .filter(Mentor.userid==userid).all()))
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items)

@view_config(route_name='mentor_courseware_add', renderer='courseware/mentor_courseware_add.mako',permission='mentor')
def mentor_courseware_add(request):
    conn=DBSession()
    params_tuple=['title','description']
    title,description=[request.params.get(x) for x in params_tuple]
    userid=request.user.id
    validator=formencode.validators.FieldStorageUploadConverter()
    coursefile=validator._to_python(request.params.get('coursefile'))
    mentor=conn.query(Mentor).filter(Mentor.userid==userid).first()
    if coursefile:
        courseware=Courseware()
        courseware.title=title
        courseware.description=description
        courseware.createtime=time.time()
        courseware.mentorid=mentor.id
        conn.add(courseware)
        conn.flush()
        return dict(code=1)
    return dict(code=0)
        