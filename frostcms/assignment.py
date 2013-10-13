# coding=utf-8
'''错误代码为14**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
#DBSession,Course,Semester,Mentor
from formencode import Schema, validators
from pyramid_simpleform import Form, State
from pyramid_simpleform.renderers import FormRenderer
import time,formencode
import webhelpers.paginate as paginate
from datetime import date  

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('mentor_assignment_add','/mentor/assignment/add')
    config.add_route('api_mentor_assignment_add','/api/mentor/assignment/add')

@view_config(route_name='mentor_assignment_add', renderer='assignment/mentor_assignment_add.mako',permission='mentor')
def mentor_course_add(request):
    conn=DBSession()
    lessonid=request.params.get('lessonid')
    lesson=conn.query(Lesson).filter(Lesson.id==lessonid).first()
    return dict(lesson=lesson)

@view_config(route_name='api_mentor_assignment_add', renderer='jsonp',permission='mentor')
def api_mentor_assignment_add(request):
    conn=DBSession()
    validators=dict(fsfileid=formencode.validators.String(not_empty=True,messages=dict(empty=(u'文件不能为空' ))),\
                    title=formencode.validators.String(not_empty=True,messages=dict(empty=(u'标题不能为空'))),\
                    description=formencode.validators.String(not_empty=True,messages=dict(empty=(u'描述不能为空'))),\
                    duedate=formencode.validators.String(not_empty=True,messages=dict(empty=(u'截止时间不能为空'))),
                    lessonid=formencode.validators.Int(not_empty=True))
    form=Form(request,validators=validators,state=State(request=request))
    if form.validate():
#         try:
        lesson=conn.query(Lesson).filter(Lesson.id==form.data['lessonid'],Lesson.courseid.in_(\
                            conn.query(Course.id).filter(Course.mentorid.in_(\
                            conn.query(Mentor.id).filter(Mentor.userid==request.user.id))))).first()
        assignment=Assignment()
        assignment.title=form.data['title']
        assignment.fsfileid=form.data['fsfileid']
        assignment.duedate=time.mktime(time.strptime(form.data['duedate'],'%Y-%m-%d'))
        assignment.description=form.data['description']
        conn.add(assignment)
        conn.flush()
        lesson.assignmentid=assignment.id
        conn.flush()
        return dict(return_url='/mentor/lesson/listbycourse?courseid='+str(lesson.courseid))
#         except Exception,e:
#             log.debug(e)
#             return dict(code=301,error=u'参数错误')
    log.debug('3')
    return dict(code=101,error=form.errors)
    