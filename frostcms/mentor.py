# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
from frostcms.utils import md5
import cgi, uuid
import webhelpers.paginate as paginate
import os
import xlrd
import cgitb
import time
cgitb.enable()

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('mentor_list', '/mentor/list')
    config.add_route('mentor_add', '/mentor/add')
    config.add_route('mentor_save', '/mentor/save')
    config.add_route('mentor_del', '/mentor/del')
    config.add_route('mentor_upload', '/mentor/upload')
    
@view_config(route_name='mentor_list', renderer='mentor/mentor_list.mako',permission='admin')
def listmentor(request):
    page = int(request.params.get('page', 1))
    collegeid = request.params.get('collegeid')
    conn = DBSession()
    if collegeid:
        items = conn.query(Mentor).filter(Mentor.collegeid==collegeid,Mentor.state!=-1)
    else:
        items=conn.query(Mentor).filter(Mentor.state!=-1)
    lis = conn.query(College).order_by(College.id)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,lis=lis) 
 
@view_config(route_name='mentor_add', renderer='mentor/mentor_add.mako',permission='admin')
def addmentor(request):
    conn = DBSession()
    mentor = conn.query(Mentor).filter(Mentor.id==request.params.get('mentorid')).first()
    lis = conn.query(College).order_by(College.id)
    return dict(mentor=mentor,lis=lis)    
 
@view_config(route_name='mentor_save', renderer='mentor/mentor_add.mako',permission='admin')
def savementor(request):
    conn = DBSession()
    mentor_id=request.params.get('mentor.id')
    param_tuples = ( "mentor.name", "mentor.identity", "mentor.gender", "mentor.collegeid",\
                      "mentor.title" ,"mentor.email","mentor.phone","mentor.description")
    name, identity, gender, collegeid, title,email,phone,description= [request.params.get( x, '' ).strip() for x in param_tuples]
    mentor = conn.query(Mentor).filter(Mentor.id==mentor_id).first()
    if mentor:
        mentor.name=name
        mentor.identity = identity
        mentor.gender = gender
        mentor.collegeid = collegeid
        mentor.title = title
        mentor.email = email
        mentor.phone = phone
        mentor.description = description
        mentor.updatetime=time.time()
    else :
        mentor = Mentor()
        mentor.name=name
        mentor.identity = identity
        mentor.gender = gender
        mentor.collegeid = collegeid
        mentor.title = title
        mentor.email = email
        mentor.phone = phone
        mentor.description = description
        mentor.state=0
        mentor.createtime=time.time()
        mentor.updatetime=time.time()
        user = User()
        user.name = str(identity)
        user.password = md5(identity)
        user.role = 1
        user.regtime=time.time()
        user.logintimes=0
        userid=conn.add(user)
        conn.flush()
        mentor.userid =user.id
        conn.add(mentor)
        
    conn.flush()
    return HTTPFound(location=request.route_url('mentor_list'))
 
@view_config(route_name='mentor_del', renderer='mentor/mentor_del.mako',permission='admin')
def delmentor(request):
    conn = DBSession()
    mentor_id=request.params.get('mentorid')
    mentor = conn.query(Mentor).filter(Mentor.id==mentor_id).first()
    if mentor:
        mentor.state=-1
        conn.flush()
        return HTTPFound(location=request.route_url('mentor_list'))
    return dict(code=0,error=u'不存在该教师')
 
 
@view_config(route_name='mentor_upload', renderer="mentor/mentor_list.mako")
def upload(request):
    upload = request.params.get('file')
    path = "frostcms/upload/exceltmp"
#     if  os.path.exists(path):
#         os.makedirs(path)
#          
    if isinstance(upload, cgi.FieldStorage) and upload.file:
        extension = upload.filename.split('.')[-1:][0]  
        if extension == "xls" or extension == "xlsx":
            filename = "%s.%s" % (uuid.uuid1(), extension)
            filepath = os.path.join(path, filename).replace("\\", "/")
            myfile = open(filepath, 'wb')
            upload.file.seek(0)
            while 1:
                tmp = upload.file.read(2 << 16)
                if not tmp:
                    break
                myfile.write(tmp)
            myfile.close()
#                新开线程处理excel
            operateexcel(filepath)     
    return HTTPFound(location=request.route_url('mentor_list'))

def operateexcel(filepath=None):
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0] 
    conn = DBSession()
    for rownum in range(1,table.nrows):
        identitynum=table.row(rownum)[0].value.strip()
        name=table.row(rownum)[1].value.strip()
        collegename=table.row(rownum)[2].value.strip()
        title=table.row(rownum)[3].value.strip()
        phone=long(table.row(rownum)[4].value)
        email=table.row(rownum)[5].value.strip()
        if(identitynum and name and collegename and title):
            college=conn.query(College).filter(College.name==collegename).first()
            if not college:
                college = College()
                college.name =collegename
                conn.add(college)
            college=conn.query(College).filter(College.name==collegename).first()
            mentor=conn.query(Mentor).filter(and_(and_(Mentor.name==name,Mentor.collegeid==college.id),and_(Mentor.title==Mentor.title,Mentor.identity==identitynum))).first()
            if not mentor:
                user = User()
                user.name = str(identitynum)
                user.password = md5(identitynum)
                user.role = 1
                user.regtime=time.time()
                user.logintimes=0
                conn.add(user)
                conn.flush()
                mentor = Mentor()
                mentor.identity=identitynum
                mentor.name=name
                mentor.userid=user.id
                mentor.collegeid=college.id
                mentor.title=title
                mentor.phone=phone
                mentor.email=email
                mentor.state=0
                mentor.createtime=time.time()
                mentor.updatetime=time.time()
                conn.add(mentor)  
                      
    conn.flush()
    os.remove(filepath)                         
    return None