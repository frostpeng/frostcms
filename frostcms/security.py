#coding=utf-8
from pyramid.security import Allow
from pyramid.security import Everyone

def groupfinder(userid, request):
    user = request.user
    if user is not None:
        if user.type==1:
            return ['g:admins','g:users']
        return ['g:users']
    return None

class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'customer'),
                (Allow, 'g:users', 'user'),
                (Allow, 'g:admins', 'admin')]
    def __init__(self, request):
        pass