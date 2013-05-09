# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound,HTTPNotFound
from pyramid.security import remember,forget
from logging import getLogger
from .models import *
from .token import Token
import time
import cgi,uuid
import hashlib 

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('home', '/')
    config.add_route('index', '/index')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

@view_config(route_name='login', renderer='login/login.mako')
def login(request):
    if request.method == "POST":
        name, password = [request.params.get(x, '').strip() for x in ['username', 'password']]
        conn = DBSession()
        user = conn.query(User).filter(and_(User.name==name, User.password == hashlib.new("md5",password).hexdigest())).first()
        if user:
            user.lastlogin=time.time()
            conn.flush()
            headers = remember(request, user.id)
            return HTTPFound(location=request.route_url('public_lesson_list'), headers=headers)
        else:
            return HTTPFound(location=request.route_url('public_lesson_list'))
    return dict(error=u'用户名密码不匹配')

@view_config(route_name='index', renderer='public/class_list.mako')
@view_config(route_name='home', renderer='public/class_list.mako')
def index(request):
    if  request.user:
        #管理员
        if request.user.role==0:
            return HTTPFound(location=request.route_url('public_lesson_list'))
        #教师
        elif request.user.role==1:
            return HTTPFound(location=request.route_url('public_lesson_list'))
        #学生
        elif request.user.role==2:
            return HTTPFound(location=request.route_url('public_lesson_list'))
    return HTTPFound(location=request.route_url('public_lesson_list'))

@view_config(route_name='logout',permission='user')
def logout(request):
    headers=forget(request)
    request.session.clear()
    return HTTPFound(location=request.route_url('public_lesson_list'),
                     headers=headers)


