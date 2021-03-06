# coding=utf-8
'''错误代码为14**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import DBSession,Student,Clazz,College,Faculty
import webhelpers.paginate as paginate
from datetime import date

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('clazz_list', '/clazz/list')
    config.add_route('api_clazz_list','/api/clazz/list')
    config.add_route('clazz_add', '/clazz/add')
    config.add_route('clazz_save', '/clazz/save')
    config.add_route('clazz_del', '/clazz/del')
    
@view_config(route_name='clazz_list', renderer='clazz/clazz_list.mako',permission='admin')
def listclazz(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    class infoClazz():
        def __init__(self):
            college = ""
            faculty = ""
            clazz = ""
            collegeNum = 0
            facultyNum = 0
            clazzNum = 0 
             
    infos = []
    info = infoClazz()
    info.college = ""
    info.faculty = ""
    info.clazz = ""
    info.collegeNum = 0
    info.facultyNum = 0
    info.clazzNum = 0
    colleges = conn.query(College).order_by(College.id)
    facultys = conn.query(Faculty).order_by(Faculty.id)
    clazzs = conn.query(Clazz).order_by(Clazz.id)
    if request.method == "POST":
        clazzid = request.params.get('clazzid')
        items = conn.query(Student).filter(Student.clazzid==clazzid)
        clazzs = conn.query(Clazz).filter(Clazz.id==clazzid)
        info.college = clazzs[0].faculty.college.name
        info.faculty = clazzs[0].faculty.name
        info.clazz = str(clazzs[0].year)+"级"+str(clazzs[0].num)+"班"
    else :
        items = []
        for college in colleges :
            if college.id > info.collegeNum :
                info.collegeNum = college.id
        for faculty in facultys :
            if faculty.id > info.facultyNum :
                info.facultyNum = faculty.id
    infos.append(info)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=30,
            url=page_url,
    )
    return dict(items=items,colleges=colleges,facultys=facultys,clazzs=clazzs,infos=infos)
 
@view_config(route_name='api_clazz_list', renderer='jsonp',permission='user')
def api_clazz_list(request):
    conn = DBSession()
    facultyid = request.params.get('facultyid')
    clazzlist = []
    if facultyid:
        clazzes = conn.query(Clazz).filter(Clazz.facultyid==facultyid).order_by(Clazz.id)
        for clazz in clazzes :
            clazzlist.append({'id':clazz.id,'year':clazz.year,'num':clazz.num})
    else :
        clazzes = conn.query(Clazz).order_by(Clazz.id)
    return dict(clazzes=clazzlist) 
 
@view_config(route_name='clazz_add', renderer='clazz/clazz_add.mako',permission='admin')
def addclazz(request):
     conn = DBSession()
     class infoClazz():
         def __init__(self):
             college = ""
             faculty = ""
             clazz = ""
             collegeNum = 0
             facultyNum = 0
             clazzNum = 0 
     infos = []
     info = infoClazz()
     info.college = ""
     info.faculty = ""
     info.clazz = ""
     info.collegeNum = 0
     info.facultyNum = 0
     info.clazzNum = 0 
     clazz = conn.query(Clazz).filter(Clazz.id==request.params.get('facultyid')).first()
     colleges = conn.query(College).order_by(College.id)
     facultys = conn.query(Faculty).order_by(Faculty.id)
     clazz = conn.query(Clazz).order_by(Clazz.id)
     for college in colleges :
         if college.id > info.collegeNum :
             info.collegeNum = college.id
     for faculty in facultys :
         if faculty.id > info.facultyNum :
             info.facultyNum = faculty.id
     infos.append(info)
     time = date.today()
     return dict(clazz=clazz,colleges=colleges,facultys=facultys,infos=infos,time=time)    
 
@view_config(route_name='clazz_save', renderer='clazz/clazz_add.mako',permission='admin')
def saveclazz(request):
    conn = DBSession()
    params_tuple=['clazz.id','clazz.facultyid','clazz.collegeid','clazz.year','clazz.num','clazz.mulfloat']
    clazzid,facultyid,collegeid,year,num,mulfloat=[request.params.get(x) for x in params_tuple]
    clazz = conn.query(Clazz).filter(Clazz.id==clazzid).first()
    if clazz:  
        clazz.collegeid = collegeid
        clazz.facultyid = facultyid
        clazz.year = year
        clazz.num =num
    else:
        clazz = Clazz()
        clazz.collegeid = collegeid
        clazz.facultyid = facultyid
        clazz.year = year
        clazz.num =num
        conn.add(clazz)
    conn.flush()
    return HTTPFound(location=request.route_url('clazz_list'))
 
@view_config(route_name='clazz_del', renderer='clazz/clazz_del.mako',permission='admin')
def delclazz(request):
    conn = DBSession()
    clazzid=request.params.get('clazzid')
    clazz = conn.query(Clazz).filter(Clazz.id==clazzid).first()
    if clazz:
        conn.delete(clazz)
        conn.flush()
    return HTTPFound(location=request.route_url('clazz_list'))