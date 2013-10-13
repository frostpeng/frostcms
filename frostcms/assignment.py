# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
#DBSession,Course,Semester,Mentor
import time
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
    