# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.security import remember, forget
from logging import getLogger
from .models import *
from .token import Token
import time
import cgi, uuid
import webhelpers.paginate as paginate

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('user_list', '/user/list')
    config.add_route('user_resetpsd', '/user/resetpsd')
    

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
    conn = DBSession();
    user = conn.query(User).filter(User.id == request.params.get('userid')).first()
    user.password=user.name
    conn.flush()
    return HTTPFound(location=request.route_url('user_list'))
        
 
