#coding=utf-8
from pyramid.security import Allow
from pyramid.security import Everyone

def groupfinder(userid, request):
    user = request.user
    if user is not None:
        if user.role==0:
            return ['g:admins','g:users']
        elif user.role==1:
            return ['g:mentors','g:users']
        elif user.role==2:
            return ['g:students','g:users']
    return None

class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'everyone'),
                (Allow, 'g:users', 'user'),
                (Allow, 'g:admins', 'admin'),
                (Allow, 'g:mentors', 'mentor'),
                (Allow, 'g:students', 'student')]
    def __init__(self, request):
        pass