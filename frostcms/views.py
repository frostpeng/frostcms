# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember,forget
from logging import getLogger
from .models import DBSession,User,Mentor,Student
from frostcms.utils import md5
import time

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('home', '/')
    config.add_route('index', '/index')
    config.add_route('login', '/login')
    config.add_route('api_user_login', 'api/user/login')
    config.add_route('logout', '/logout')

@view_config(route_name='login', renderer='login/login.mako')
def login(request):
    return dict(code=1)
#     if request.method == "POST":
#         name, password = [request.params.get(x, '').strip() for x in ['username', 'password']]
#         conn = DBSession()
#         user = conn.query(User).filter(and_(User.name==name, User.password == hashlib.new("md5",password).hexdigest())).first()
#         if user:
#             user.lastlogin=time.time()
#             conn.flush()
#             headers = remember(request, user.id)
#             return HTTPFound(location=request.route_url('public_lesson_list'), headers=headers)
#         else:
#             return HTTPFound(location=request.route_url('public_lesson_list'))
#     return dict(error=u'用户名密码不匹配')
    
@view_config(route_name='api_user_login', renderer='jsonp')
def api_user_login(request):
    """用户登录api验证
          传入：username,password
   返回：code为1 成功，0失败
    """
    if request.method == "POST":
        name, password,remember_value = [request.params.get(x, '').strip() for x in\
                                    ['username', 'password','remember']]
        conn = DBSession()
        user = conn.query(User).filter(User.name==name).first()
        if user:
            if user.role==1:
                mentor=conn.query(Mentor).filter(Mentor.userid==user.id).first()
                if mentor and mentor.state==1:
                    return dict(code=0,error=u'账号已经锁定，请联系管理员')
            elif user.role==2:
                student=conn.query(Student).filter(Student.userid==user.id).first()
                if student and student.state==1:
                    return dict(code=0,error=u'账号已经锁定，请联系管理员')
            if user.password == md5(password):
                user.lastlogin=time.time()
                conn.flush()
                if remember_value=='true':
                    expire_in = time.time()+7*24*60*60
                    headers = remember(request, user.id,max_age=expire_in)
                else:
                    headers=remember(request, user.id)
                request.response_headerlist=headers
                return dict(code=1,return_url="/public/lesson_list")
            else:
                return dict(code=0,error=u'用户名密码不匹配')
        else:
            return dict(code=0,error=u'用户不存在')
    return dict(code=0,error=u'系统错误，请联系管理员')
    

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


