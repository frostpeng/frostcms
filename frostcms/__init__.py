from pyramid.config import Configurator
from sqlalchemy import engine_from_config,func,desc

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
from .models import initialize_sql,DBSession,User,Lesson,LessonWorkItem,Mentor,Student,Semester
import hashlib
import transaction
from logging import getLogger
import time

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
        lessonscout+=conn.query(Lesson.id).filter(Lesson.state==-2).count()
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
    
    @reify
    def thissemester(self):
        conn=DBSession()
        now = time.time()
        semester = None
        semester = conn.query(Semester).filter(now<=Semester.start+Semester.weeks*7*24*60*60).order_by(desc(Semester.start+Semester.weeks*7*24*60*60-now)).first()
        return semester
    
    @reify
    def thisweek(self):
        now = time.time()
        week = 0
        semester = self.thissemester
        if semester :
            week = int((now - semester.start)/(7*24*60*60) + 1) 
        return week
        
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
