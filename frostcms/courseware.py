# coding=utf-8
'''错误代码为11**
'''
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
from formencode import Schema, validators
from pyramid_simpleform import Form, State
from pyramid_simpleform.renderers import FormRenderer

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('mentor_courseware_list', '/mentor/courseware/list')
    config.add_route('mentor_courseware_add', '/mentor/courseware/add')
    config.add_route('mentor_courseware_del', '/mentor/courseware/del')
    config.add_route('api_mentor_courseware_add', '/api/mentor/courseware/add')
    config.add_route('courseware_course_list','/courseware/warelist')
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
        if os.path.exists(courseware.fsfile.filepath):
            os.remove(courseware.fsfile.filepath)
        conn.delete(courseware.fsfile)
        conn.delete(courseware)
        conn.flush()
    return HTTPFound(location=request.route_url('mentor_courseware_list'))

@view_config(route_name='api_mentor_courseware_add', renderer='jsonp',permission='mentor')
def api_mentor_courseware_add(request):
    conn=DBSession()
    validators=dict(fsfileid=formencode.validators.String(not_empty=True,min=16,messages=dict(empty=(u'文件不能为空' ))),\
                    title=formencode.validators.String(not_empty=True,messages=dict(empty=(u'标题不能为空'))),\
                    description=formencode.validators.String(not_empty=True,messages=dict(empty=(u'描述不能为空'))))
    form=Form(request,validators=validators,state=State(request=request))
    if form.validate():
        mentor=conn.query(Mentor).filter(Mentor.userid==request.user.id).first()
        courseware=Courseware()
        courseware.title=form.data['title']
        courseware.description=form.data['description']
        courseware.createtime=time.time()
        courseware.mentorid=mentor.id
        courseware.fsfileid=form.data['fsfileid']
        conn.add(courseware)
        conn.flush()
        return dict(return_url='/mentor/courseware/list')
    return dict(code=101,error=form.errors)

@view_config(route_name='courseware_course_list', renderer='courseware/mentor_courseware_course_list.mako')
def courseware_course_list(request):
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
    return HTTPFound(location=request.route_url('courseware_course_list',_query={'courseid':courseid}))


@view_config(route_name='mentor_courseware_course_del', renderer='courseware/mentor_courseware_course_list.mako',permission='mentor')
def mentor_courseware_course_del(request):
    conn = DBSession()
    courseid=request.params.get('courseid')
    wareid=request.params.get('wareid')
    if courseid and wareid :
        ware_course=conn.query(Ware_Course).filter(Ware_Course.wareid==wareid,Ware_Course.courseid==courseid).first()
        conn.delete(ware_course)
    conn.flush()
    return HTTPFound(location=request.route_url('courseware_course_list',_query={'courseid':courseid})) 