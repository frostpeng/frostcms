# coding=utf-8
'''错误代码为5**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import DBSession,Semester
import time
import webhelpers.paginate as paginate
from datetime import date 

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('semester_list', '/semester/list')
    config.add_route('semester_add', '/semester/add')
    config.add_route('semester_save', '/semester/save')
    config.add_route('semester_del', '/semester/del')
    
@view_config(route_name='semester_list', renderer='semester/semester_list.mako',permission='admin')
def listsemester(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    semesters = conn.query(Semester).order_by(Semester.id)
    page_url = paginate.PageURL_WebOb(request)
    items = []
    class List_semester():
        def __init__(self):
            self.id = 0
            self.name = ""
            self.time = ""
            self.weeks = 0
    for semester in semesters:
        t = List_semester()
        t.id = semester.id
        t.time = date.fromtimestamp(semester.start)
        t.weeks = semester.weeks
        time = t.time
        name = str(time.year)
        mon = time.month
        if  mon >7 :
            name += u"年秋季"
        else :
            name += u"年春季"
        t.name = name 
        items.append(t)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items) 
 
@view_config(route_name='semester_add', renderer='semester/semester_add.mako',permission='admin')
def addsemester(request):
    conn = DBSession()
    get = conn.query(Semester).filter(Semester.id==request.params.get('semesterid')).first()
    class List_semester():
        def __init__(self):
            self.id = 0
            self.name = ""
            self.time = ""
            self.weeks = 0
    if get :
        semester = List_semester()
        semester.id = get.id
        semester.time = date.fromtimestamp(get.start)
        semester.weeks = get.weeks
    else :
        semester = get
    return dict(semester=semester)    
 
@view_config(route_name='semester_save', renderer='semester/semester_add.mako',permission='admin')
def savesemester(request):
    conn = DBSession()
    getStart = request.params.get('semester.start')
    getWeeks = request.params.get('semester.weeks')
    start = time.mktime(time.strptime(getStart,'%Y-%m-%d'))
    if request.params.get('semester.id'):
        semester = conn.query(Semester).filter(Semester.id==request.params.get('semester.id')).first()
        semester.start=start
        semester.weeks=getWeeks
        conn.flush()
    else:
        semester = Semester()
        semester.start=start
        semester.weeks=getWeeks
        conn.add(semester)
        conn.flush()
    return HTTPFound(location=request.route_url('semester_list'))
 
@view_config(route_name='semester_del', renderer='semester/semester_del.mako',permission='admin')
def dellocation(request):
    conn = DBSession()
    get = conn.query(Semester).filter(Semester.id==request.params.get('semesterid')).first()
    class List_semester():
        def __init__(self):
            self.id = 0
            self.name = ""
            self.time = ""
            self.weeks = 0
    if get :
        semester = List_semester()
        semester.id = get.id
        semester.time = date.fromtimestamp(get.start)
        semester.weeks = get.weeks
        time = semester.time
        name = str(time.year)
        mon = time.month
        if  mon >7 :
            name += u"年秋季"
        else :
            name += u"年春季"
        semester.name = name
    else :
        semester = get
    if request.params.get('semester.id'):
        semester = conn.query(Semester).filter(Semester.id==request.params.get('semester.id')).first()
        conn.delete(semester)
        conn.flush()
        return HTTPFound(location=request.route_url('semester_list'))
    return dict(semester=semester)
