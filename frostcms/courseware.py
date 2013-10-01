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
    config.add_route('mentor_courseware_course_list','/mentor/course/warelist')
    config.add_route('mentor_courseware_course_add','/mentor/course/waraadd')
    config.add_route('mentor_courseware_course_save','/mentor/course/warasave')
    config.add_route('mentor_courseware_course_del','/mentor/course/waradel')
    
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
    conn = DBSession()
    userid = request.user.id
    courses = conn.query(Course).filter(Course.mentorid==userid)
    return dict(code=0,courses=courses)

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

@view_config(route_name='mentor_courseware_course_list', renderer='courseware/mentor_courseware_course_list.mako',permission='mentor')
def mentor_courseware_course_list(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    userid=request.user.id
    courseid=request.params.get('courseid')
    course=None
    items=[]
    if courseid :
        wares = conn.query(Ware_Course).filter(Ware_Course.courseid==courseid)
        course = conn.query(Course).filter(Course.id==courseid).first()
        for ware in wares :
            items.append(ware.courseware)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,course=course)

@view_config(route_name='mentor_courseware_course_add', renderer='courseware/mentor_courseware_course_add.mako',permission='mentor')
def mentor_courseware_course_add(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    userid = request.user.id
    courseid=request.params.get('courseid')
    course=None
    items=[]
    if courseid :
        course = conn.query(Course).filter(Course.id==courseid).first()
        #items=conn.query(Courseware)
        wares=conn.query(Ware_Course.wareid).filter(Ware_Course.courseid==courseid)
        #if wares :
        items=conn.query(Courseware).filter(Courseware.mentorid.in_(conn.query(Mentor.id)\
                .filter(Mentor.userid==userid)),Courseware.id.notin_(wares))
        #else :
        #    items=conn.query(Courseware)
        #"""
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(code=0,course=course,items=items)

@view_config(route_name='mentor_courseware_course_save', renderer='courseware/mentor_courseware_course_add.mako',permission='mentor')
def mentor_courseware_course_save(request):
    conn = DBSession()
    addwares=request.params.getall('addwares')
    courseid=request.params.get('courseid')
    for i in range(0,len(addwares)):
        ware_course=Ware_Course()
        ware_course.courseid=int(courseid)
        ware_course.wareid=int(addwares[i])
        ware_course.state=0
        conn.add(ware_course)
    conn.flush()
    return HTTPFound(location=request.route_url('mentor_courseware_course_list',_query={'courseid':courseid}))


@view_config(route_name='mentor_courseware_course_del', renderer='courseware/mentor_courseware_course_list.mako',permission='mentor')
def mentor_courseware_course_del(request):
    conn = DBSession()
    courseid=request.params.get('courseid')
    wareid=request.params.get('wareid')
    if courseid and wareid :
        ware_course=conn.query(Ware_Course).filter(Ware_Course.wareid==wareid,Ware_Course.courseid==courseid).first()
        conn.delete(ware_course)
    conn.flush()
    return HTTPFound(location=request.route_url('mentor_courseware_course_list',_query={'courseid':courseid})) 