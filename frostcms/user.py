# coding=utf-8
'''错误为3**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound,HTTPNotFound
from logging import getLogger
from .models import DBSession,User
import webhelpers.paginate as paginate
from formencode import Schema, validators
from pyramid_simpleform import Form, State
from pyramid_simpleform.renderers import FormRenderer
import formencode
from frostcms.utils import md5
from frostcms.models import Courseware
import os,urllib, uuid
import mimetypes

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('user_list', '/user/list')
    config.add_route('user_resetpsd', '/user/resetpsd')
    config.add_route('user_change_psd', '/user/change_password')
    config.add_route('api_user_change_password', '/api/user/change_password')
    config.add_route('api_user_uploadfile','/api/user/uploadfile')
    config.add_route('user_courseware_getfilebyid','/user/courseware/getfilebyid')
    

@view_config(route_name='user_list', renderer='user/user_list.mako',permission='admin')
def listuser(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    items = conn.query(User).order_by(User.regtime)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items)
 
       
@view_config(route_name='user_resetpsd', renderer='user/user_list.mako',permission='admin')
def resetpsd(request):
    """密码重置
    """
    conn = DBSession();
    user = conn.query(User).filter(User.id == request.params.get('userid')).first()
    user.password=md5(user.name)
    conn.flush()
    return HTTPFound(location=request.route_url('user_list'))

@view_config(route_name='user_change_psd', renderer='user/user_changepsd.mako',permission='user')
def  user_change_psd(request):
    return dict(code=1)

class PasswordIsMatched(formencode.FancyValidator):
    """密码是否匹配
    pxk
    """
    def _to_python(self, value, state):
        if state.request.user.password==md5(value):
            return value
        else:
            raise formencode.Invalid(u'输入原密码有误', value, state)

class ChangePasswordSchema(Schema):
    """修改密码schema，提供公司所有变量的验证
    """
    allow_extra_fields = True
    filter_extra_fields = True
    oldpassword = formencode.All(validators.String(not_empty=True,min=8,max=30,
            messages=dict(empty=(u'旧密码不能为空' ),tooLong=(u'密码最长不能超过 %(max)i'),\
            tooShort=(u'密码最短不能少于 %(min)i'))),PasswordIsMatched())
    newpassword = validators.String(not_empty=True,min=8,max=30,messages=dict(empty=\
            (u'新密码不能为空' ),tooLong=(u'密码最长不能超过 %(max)i'),tooShort=(u'密码最短不能少于 %(min)i')))

@view_config(route_name='api_user_change_password',renderer='jsonp',permission='user')
def api_user_change_password(request):
    """用户修改密码api
    """
    form = Form(request,defaults={},schema=ChangePasswordSchema(),state=State(request=request)) 
    if form.validate():
        conn=DBSession()
        request.user.password=md5(form.data['newpassword'])
        conn.flush()
        return {}
    return dict(code=101,error=FormRenderer(form).errorlist())

@view_config(route_name='api_user_uploadfile',permission='user')
def api_user_uploadfile(request):
    """用户上传文件，需要传入路径和
    """
    validators=dict(uploadfile=formencode.validators.FieldStorageUploadConverter(\
            not_empty=True,messages=dict(empty=(u'文件不能为空' ))),path=formencode.validators.String\
                    (not_empty=True,messages=dict(empty=(u'路径不能为空' ))))
    form=Form(request,validators=validators,state=State(request=request))
    if form.validate():
        try:
            path = "frostcms/upload/"+form.data['path']
            if not os.path.exists(path):
                os.makedirs(path)
                 
            extension = form.data['uploadfile'].filename.split('.')[-1:][0]  
            filename = "%s.%s" % (uuid.uuid1(), extension)
            filepath = os.path.join(path, filename).replace("\\", "/")
            myfile = open(filepath, 'wb')
            form.data['uploadfile'].file.seek(0)
            while 1:
                tmp = form.data['uploadfile'].file.read(2 << 16)
                if not tmp:
                    break
                myfile.write(tmp)
            myfile.close()
            result=dict(filename=form.data['uploadfile'].filename,filepath=filepath.replace("/","\\"))
#             result=dict(filename=form.data['uploadfile'].filename,filepath=filepath)
            returnStr=str(result)
            returnStr=returnStr.replace("u'","'")
            #returnStr="<body><pre>"+str(result)+"</pre></body>"
            response = request.response
            response.headers['Pragma']='no-cache'
            response.headers['Cache-Control']='no-cache'
            response.headers['Expires']='0'
            response.headers['Content-Type']="text/html"
            response.write(returnStr)
            log.debug(result)
            return response
        except Exception,e:
            log.debug(str(e))
            return dict(code=301,error=u'参数错误')
    return dict(code=101,error=form.errors)

@view_config(route_name='user_courseware_getfilebyid',permission='user')
def user_courseware_getfilebyid(request):
    """获取文件
    """
    conn=DBSession()
    coursewareid = request.params.get('coursewareid')
    courseware=conn.query(Courseware).filter(Courseware.id==coursewareid).first()
    if os.path.exists(courseware.filepath): 
        extension = courseware.filename.split('.')[-1:][0]  
        content_type= mimetypes.types_map['.'+extension]
        file=open(courseware.filepath)
        response = request.response
        response.headers['Pragma']='no-cache'
        response.headers['Cache-Control']='no-cache'
        response.headers['Content-Disposition']=str("attachment; filename="+courseware.filename)
        response.headers['Content-Type']=content_type
        response.headers['Expires']='0'
        response.write(file.read())
        return response
    return HTTPNotFound()
        
 
