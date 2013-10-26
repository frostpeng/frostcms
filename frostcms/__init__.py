from pyramid.config import Configurator
from sqlalchemy import engine_from_config,func

from pyramid.renderers import JSONP
from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid
from pyramid.events import NewRequest
from pyramid.httpexceptions import HTTPForbidden
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from .authentication import AuthenticationPolicy
from .security import groupfinder
from .models import initialize_sql,DBSession,User,Lesson,LessonWorkItem,Mentor,Student
import hashlib
import transaction
from logging import getLogger

log = getLogger(__name__)

class MainRequest(Request):
    @reify
    def user(self):
        id = unauthenticated_userid(self)
        if id:
            conn=DBSession()
            user=conn.query(User).get(id)
            return user
        else:
            return None
        
    @reify
    def undocount(self):
        conn=DBSession()
        lessonscout=conn.query(Lesson.id).filter(Lesson.state==0).count()
        return lessonscout
    
    @reify
    def noticenum(self):
        conn=DBSession()
        noticenum = conn.query(LessonWorkItem).filter(LessonWorkItem.acceptuserid==self.user.id,LessonWorkItem.viewstate==0).count()
        return noticenum
    
    @reify
    def getusername(self):
        conn=DBSession()
        if self.user.role == 1 :
            ur = conn.query(Mentor).filter(Mentor.userid == self.user.id).first() 
        elif self.user.role == 2 :
            ur = conn.query(Student).filter(Student.userid == self.user.id).first()
        else:
            ur = self.user
        return ur


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    authentication_policy = AuthenticationPolicy(
        settings['auth.secret'], cookie_name='frostcms', callback = groupfinder)
    authorization_policy = ACLAuthorizationPolicy() 
    my_session_factory = UnencryptedCookieSessionFactoryConfig('1@3$msT')
    config = Configurator(settings=settings,
                          root_factory='frostcms.security.RootFactory',
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy,
                          session_factory = my_session_factory,
                          request_factory=MainRequest)
    jsonp_renderer = JSONP(param_name='callback')
    config.add_renderer('jsonp', jsonp_renderer)
    config.add_static_view('static', 'frostcms:static', cache_max_age=3600)
    config.add_static_view('upload', 'frostcms:upload')
    config.include("frostcms.views")
    config.include("frostcms.assignment")
    config.include("frostcms.user")
    config.include("frostcms.mentor")
    config.include("frostcms.student")
    config.include("frostcms.faculty")
    config.include("frostcms.location")
    config.include("frostcms.college")
    config.include("frostcms.semester")
    config.include("frostcms.clazz")
    config.include("frostcms.public")
    config.include("frostcms.lesson")
    config.include("frostcms.course")
    config.include("frostcms.courseware")
    return config.make_wsgi_app()
