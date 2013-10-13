# coding=utf-8
'''错误代码为10**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import DBSession,Faculty,College
import webhelpers.paginate as paginate

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('faculty_list', '/faculty/list')
    config.add_route('api_faculty_list','/api/faculty/list')
    config.add_route('faculty_add', '/faculty/add')
    config.add_route('faculty_save', '/faculty/save')
    config.add_route('faculty_del', '/faculty/del')
    
@view_config(route_name='faculty_list', renderer='faculty/faculty_list.mako',permission='admin')
def listfaculty(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    if request.method == "POST":
        collegeid = request.params.get('collegeid')
        items = conn.query(Faculty).filter(Faculty.collegeid==collegeid)
    else :
        items = conn.query(Faculty).order_by(Faculty.id)
    lis = conn.query(College).order_by(College.id)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,lis=lis)

@view_config(route_name='api_faculty_list', renderer='jsonp',permission='user')
def api_faculty_list(request):
    conn = DBSession()
    collegeid = request.params.get('collegeid')
    facultylist = []
    if collegeid:
        faculties = conn.query(Faculty).filter(Faculty.collegeid==collegeid)
        for faculty in faculties :
            facultylist.append({'id':faculty.id,'name':faculty.name})
    else :
        faculties = conn.query(Faculty).order_by(Faculty.id)
    return dict(faculties=facultylist)
 
@view_config(route_name='faculty_add', renderer='faculty/faculty_add.mako',permission='admin')
def addfaculty(request):
    conn = DBSession()
    faculty = conn.query(Faculty).filter(Faculty.id==request.params.get('facultyid')).first()
    lis = conn.query(College).order_by(College.id)
    return dict(faculty=faculty,lis=lis)    
 
@view_config(route_name='faculty_save', renderer='faculty/faculty_add.mako',permission='admin')
def savefaculty(request):
    conn = DBSession()
    if request.params.get('faculty.id'):
        faculty = conn.query(Faculty).filter(Faculty.id==request.params.get('faculty.id')).first()
        faculty.name = request.params.get('faculty.name')
        faculty.collegeid = request.params.get('faculty.collegeid')
        conn.flush()
        return HTTPFound(location=request.route_url('faculty_list'))
    else:
        faculty = Faculty()
        faculty.name = request.params.get('faculty.name')
        faculty.collegeid = request.params.get('faculty.collegeid')
        conn.add(faculty)
        conn.flush()
        return HTTPFound(location=request.route_url('faculty_list'))
    return HTTPFound(location=request.route_url('faculty_list'))
 
@view_config(route_name='faculty_del', renderer='faculty/faculty_del.mako',permission='admin')
def delfaculty(request):
    conn = DBSession()
    faculty = conn.query(Faculty).filter(Faculty.id==request.params.get('facultyid')).first()
    if request.params.get('faculty.id'):
        faculty = conn.query(Faculty).filter(Faculty.id==request.params.get('faculty.id')).first()
        conn.delete(faculty)
        conn.flush()
        return HTTPFound(location=request.route_url('faculty_list'))
    lis = conn.query(College).order_by(College.id)
    return dict(faculty=faculty,lis=lis)