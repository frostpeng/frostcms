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
    config.add_route('mentor_assignment_list','/mentor/assignment/list')
    config.add_route('mentor_assignment_markupload','/mentor/assignment/markupload')
    config.add_route('api_mentor_assignment_markupload','/api/mentor/assignment/markupload')
    config.add_route('api_mentor_assignment_overmark','/api/mentor/assignment/overmark')
    config.add_route('student_assignment_detail','/student/assignment/detail')
    config.add_route('student_assignment_list','/student/assignment/list')
    config.add_route('student_assignment_upload','/student/assignment/upload')
    config.add_route('api_student_assignment_upload','/api/student/assignment/upload')

@view_config(route_name='mentor_assignment_add', renderer='assignment/mentor_assignment_add.mako',permission='mentor')
def mentor_assignment_add(request):
    conn=DBSession()
    lessonid=request.params.get('lessonid')
    lesson=conn.query(Lesson).filter(Lesson.id==lessonid).first()
    if lesson and lesson.assignment:
        return dict(lesson=lesson,assignment=lesson.assignment)
    return dict(lesson=lesson)

@view_config(route_name='api_mentor_assignment_add', renderer='jsonp',permission='mentor')
def api_mentor_assignment_add(request):
    conn=DBSession()
    validators=dict(fsfileid=formencode.validators.String(not_empty=True,min=16,messages=dict(empty=(u'文件不能为空' ))),\
                    title=formencode.validators.String(not_empty=True,messages=dict(empty=(u'标题不能为空'))),\
                    description=formencode.validators.String(not_empty=True,messages=dict(empty=(u'描述不能为空'))),\
                    duedate=formencode.validators.String(not_empty=True,messages=dict(empty=(u'截止时间不能为空'))),
                    lessonid=formencode.validators.Int(not_empty=True),
                    assignmentid=formencode.validators.Int(not_empty=False))
    form=Form(request,validators=validators,state=State(request=request))
    if form.validate():
        try:
            lesson=conn.query(Lesson).filter(Lesson.id==form.data['lessonid'],Lesson.courseid.in_(\
                                conn.query(Course.id).filter(Course.mentorid.in_(\
                                conn.query(Mentor.id).filter(Mentor.userid==request.user.id))))).first()
            if form.data['assignmentid'] and int(form.data['assignmentid']):
                assignment=conn.query(Assignment).filter(Assignment.id==lesson.assignmentid).first()
                assignment.title=form.data['title']
                assignment.fsfileid=form.data['fsfileid']
                assignment.duedate=time.mktime(time.strptime(form.data['duedate'],'%Y-%m-%d'))
                assignment.description=form.data['description']
                conn.flush()
            else:
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
        except Exception,e:
            log.debug(e)
            return dict(code=301,error=u'参数错误')
    return dict(code=101,error=form.errors)

@view_config(route_name='mentor_assignment_list', renderer='assignment/mentor_assignment_list.mako',permission='mentor')
def mentor_assignment_list(request):
    conn=DBSession()
    page = int(request.params.get('page', 1))
    s_courseid=request.params.get('s_courseid')
    userid=request.user.id
    courses=conn.query(Course).filter(Course.mentorid.in_(\
                            conn.query(Mentor.id).filter(Mentor.userid==userid))).all()
    items=conn.query(Assignment,Lesson).filter(Assignment.id==Lesson.assignmentid,
                     Lesson.courseid.in_(conn.query(Course.id).filter(Course.mentorid.in_(\
                            conn.query(Mentor.id).filter(Mentor.userid==userid))))).all()
    if s_courseid:
        items=conn.query(Assignment,Lesson).filter(Assignment.id==Lesson.assignmentid,
                     Lesson.courseid.in_(conn.query(Course.id).filter(Course.mentorid.in_(\
                            conn.query(Mentor.id).filter(Mentor.userid==userid)),\
                            Course.id.in_(courses)))).all()
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,courses=courses)

@view_config(route_name='mentor_assignment_markupload', renderer='assignment/mentor_assignment_markupload.mako',permission='mentor')
def mentor_assignment_markupload(request):
    conn=DBSession()
    page = int(request.params.get('page', 1))
    assignmentid=request.params.get('assignmentid')
    userid=request.user.id
    items=conn.query(AssignmentUpload).filter(AssignmentUpload.assignmentid==assignmentid).all()
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=20,
            url=page_url,
            )
    return dict(items=items)

@view_config(route_name='api_mentor_assignment_markupload', renderer='jsonp',permission='mentor')
def api_mentor_assignment_markupload(request):
    validators=dict(uploadid=formencode.validators.Int(not_empty=True),
                    mark=formencode.validators.Number(not_empty=True))
    form=Form(request,validators=validators,state=State(request=request))
    if form.validate():
        conn=DBSession()
        assignmentupload=conn.query(AssignmentUpload).filter(AssignmentUpload.id==form.data['uploadid']).first()
        if assignmentupload:
            assignmentupload.state=1
            assignmentupload.mark=form.data['mark']
            conn.flush()
            return {}
        return dict(code=1401,error=u'作业已经不存在')
    return dict(code=101,error=form.errors)

@view_config(route_name='api_mentor_assignment_overmark', renderer='jsonp',permission='mentor')
def api_mentor_assignment_overmark(request):
    validators=dict(assignmentid=formencode.validators.Int(not_empty=True))
    form=Form(request,validators=validators,state=State(request=request))
    if form.validate():
        conn=DBSession()
        assignment=conn.query(Assignment).filter(Assignment.id==form.data['assignmentid']).first()
        if assignment:
            assignment.state=2
            assignmentuploads=conn.query(AssignmentUpload).filter(AssignmentUpload.assignmentid==form.data['assignmentid']).all()
            for assignmentupload in assignmentuploads:
                assignmentupload.state=2
            conn.flush()
            return dict(return_url="/mentor/assignment/list")
        return dict(code=1401,error=u'作业已经不存在')
    return dict(code=101,error=form.errors)

@view_config(route_name='student_assignment_list', renderer='assignment/student_assignment_list.mako',permission='student')
def student_assignment_list(request):
    conn=DBSession()
    page = int(request.params.get('page', 1))
    s_courseid=request.params.get('s_courseid')
    userid=request.user.id
    student=conn.query(Student).filter(Student.userid==userid).first()
    courses=conn.query(Course).filter(Course.id.in_(\
                            conn.query(Course_Class.courseid).filter(Course_Class.clazzid\
                            ==student.clazzid))).all()
    items=conn.query(Assignment,Lesson).filter(Assignment.id==Lesson.assignmentid,
                     Lesson.courseid.in_(conn.query(Course_Class.courseid).filter(Course_Class.clazzid\
                            ==student.clazzid))).all()
    if s_courseid:
        items=conn.query(Assignment,Lesson).filter(Assignment.id==Lesson.assignmentid,
                     Lesson.courseid.in_(conn.query(Course_Class.courseid).filter(Course_Class.clazzid\
                            ==student.clazzid)),\
                            Course.id.in_(courses)).all()
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,courses=courses)

@view_config(route_name='student_assignment_detail', renderer='assignment/student_assignment_detail.mako',permission='student')
def student_assignment_detail(request):
    conn=DBSession()
    assignmentid=request.params.get('assignmentid')
    userid=request.user.id
    assignment=conn.query(Assignment).filter(Assignment.id==assignmentid).first()
    return dict(assignment=assignment)

@view_config(route_name='student_assignment_upload', renderer='assignment/assignment_upload.mako',permission='student')
def student_assignment_upload(request):
    conn=DBSession()
    assignmentid=request.params.get('assignmentid')
    userid=request.user.id
    student=conn.query(Student).filter(Student.userid==userid).first()
    assignment=conn.query(Assignment).filter(Assignment.id==assignmentid).first()
    assignmentupload=conn.query(AssignmentUpload).filter(AssignmentUpload.assignmentid==assignmentid,\
                    AssignmentUpload.studentid==student.id).first()
    return dict(assignment=assignment,assignmentupload=assignmentupload)

@view_config(route_name='api_student_assignment_upload', renderer='jsonp',permission='student')
def api_student_assignment_upload(request):
    conn=DBSession()
    validators=dict(fsfileid=formencode.validators.String(not_empty=True,min=16,messages=dict(empty=(u'文件不能为空' ))),\
                    title=formencode.validators.String(not_empty=True,messages=dict(empty=(u'标题不能为空'))),\
                    description=formencode.validators.String(not_empty=True,messages=dict(empty=(u'描述不能为空'))),\
                    uploadid=formencode.validators.Int(not_empty=False),
                    assignmentid=formencode.validators.Int(not_empty=True))
    form=Form(request,validators=validators,state=State(request=request))
    student=conn.query(Student).filter(Student.userid==request.user.id).first()
    if form.validate():
        try:
            assignment=conn.query(Assignment).filter(Assignment.id==form.data['assignmentid']).first()
            if form.data['uploadid'] and int(form.data['uploadid']):
                upload=conn.query(AssignmentUpload).filter(AssignmentUpload.id==int(form.data['uploadid'])).first()
                upload.title=form.data['title']
                upload.fsfileid=form.data['fsfileid']
                upload.description=form.data['description']
                upload.updatetime=time.time()
                upload.studentid=student.id
                conn.flush()
            else:
                upload=AssignmentUpload()
                upload.assignmentid=form.data['assignmentid']
                upload.title=form.data['title']
                upload.fsfileid=form.data['fsfileid']
                upload.createtime=time.time()
                upload.updatetime=time.time()
                upload.description=form.data['description']
                upload.studentid=student.id
                conn.add(upload)
                conn.flush()
            return dict(return_url='/student/assignment/list')
        except Exception,e:
            log.debug(e)
            return dict(code=301,error=u'参数错误')
    log.debug(form.errors)
    return dict(code=101,error=form.errors)
    