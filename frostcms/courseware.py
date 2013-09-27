# coding=utf-8
from pyramid.view import view_config
import formencode
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
import time
import webhelpers.paginate as paginate
from datetime import date  
import os
import cgi, uuid

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('mentor_courseware_list', '/mentor/courseware/list')
    config.add_route('mentor_courseware_add', '/mentor/courseware/add')
    config.add_route('mentor_courseware_del', '/mentor/courseware/del')
    config.add_route('mentor_courseware_save', '/mentor/courseware/save')
    
@view_config(route_name='mentor_courseware_list', renderer='courseware/mentor_courseware_list.mako',permission='mentor')
def mentor_courseware_list(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    userid=request.user.id
    items=conn.query(Courseware).filter(Courseware.mentorid.in_(conn.query(Mentor.id)\
                .filter(Mentor.userid==userid))).all()
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
    return dict(code=0)

@view_config(route_name='mentor_courseware_del', renderer='courseware/mentor_courseware_add.mako',permission='mentor')
def mentor_courseware_del(request):
    coursewareid=request.params.get('coursewareid')
    conn=DBSession()
    courseware=conn.query(Courseware).filter(Courseware.id==coursewareid).first()
    mentor=conn.query(Mentor).filter(Mentor.userid==request.user.id).first()
    if courseware and mentor and mentor.id==courseware.mentorid:
        if os.path.exists(courseware.filepath):
            os.remove(courseware.filepath)
        conn.delete(courseware)
        conn.flush()
    return HTTPFound(location=request.route_url('mentor_courseware_list'))

@view_config(route_name='mentor_courseware_save', renderer='courseware/mentor_courseware_add.mako',permission='mentor')
def mentor_courseware_save(request):
    conn=DBSession()
    params_tuple=['title','description']
    title,description=[request.params.get(x) for x in params_tuple]
    userid=request.user.id
    coursefile=request.params.get('coursefile')
    mentor=conn.query(Mentor).filter(Mentor.userid==userid).first()
    try:
        if isinstance(coursefile, cgi.FieldStorage) and coursefile.file:
            path = "frostcms/upload/courseware"
            if not os.path.exists(path):
                os.makedirs(path)
                 
            extension = coursefile.filename.split('.')[-1:][0]  
            filename = "%s.%s" % (uuid.uuid1(), extension)
            filepath = os.path.join(path, filename).replace("\\", "/")
            myfile = open(filepath, 'wb')
            coursefile.file.seek(0)
            while 1:
                tmp = coursefile.file.read(2 << 16)
                if not tmp:
                    break
                myfile.write(tmp)
            myfile.close()
            courseware=Courseware()
            courseware.title=title
            courseware.description=description
            courseware.createtime=time.time()
            courseware.filepath=filepath
            courseware.mentorid=mentor.id
            courseware.filename=coursefile.filename
            conn.add(courseware)
            conn.flush()
            return dict(code=1)
    except Exception,e:
        log.debug(str(e))
    return dict(code=0)
        