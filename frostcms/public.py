# coding=utf-8
'''错误代码为6**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import *
import webhelpers.paginate as paginate
from utils import md5

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('public_lesson_list', '/public/lesson_list')
    config.add_route('install','/install')
    
    
@view_config(route_name='public_lesson_list', renderer='public/class_list.mako')
def listlesson(request):
    conn = DBSession()
    params_tuple=['week','locationid','area']
    week,locationid,area=[request.params.get(x) for x in params_tuple]
    locationdictionary=conn.query(Location).order_by(Location.id)
    loc = conn.query(Location).filter(Location.id==locationid).first()
    class Acolum():
        def __init__(self):
            self.courses = []
            self.studentnum = 0
    items = []
    seatnum = 0
    courses = []
    if week and locationid:
        locations = conn.query(Lesson_Location).filter(Lesson_Location.locationid==locationid)
        for location in locations:
            if  location.lesson.week == int(week) and location.lesson.state == 1:
                courses.append(location)
                seatnum = location.location.seatnum
        for dow in range(0,7) :
            day = []
            for time in range(0,6) :
                num = 0
                colum = Acolum()
                for course in courses :    
                    if course.lesson.dow == dow and course.lesson.start<=time*2+1 and course.lesson.end>=time*2+1 :
                        num += course.studentnum
                        colum.courses.append(course)
                colum.studentnum = num
                day.append(colum)
            items.append(day)
        """if startweek:
            items=items.filter(Lesson.week>=startweek)
        if endweek:
            items=items.filter(Lesson.week<=endweek) 
        if area:
            items=items.filter(Lesson.id.in_(conn.query(Lesson_Location.lessonid).filter\
                    (Lesson_Location.locationid.in_(conn.query(Location.id).filter(Location.area==area)))))
        if locationid:
            items=items.filter(Lesson.id.in_(conn.query(Lesson_Location.lessonid).filter(Lesson_Location.locationid==locationid)))
        """
    return dict(items=items,week=week,locationid=locationid,area=area,locationdictionary=locationdictionary,seatnum=seatnum,loc=loc)     
    
    
@view_config(route_name='install', renderer='jsonp')
def install(request):
    conn = DBSession()
    admin=conn.query(User).filter(User.name=='admin').first()
    if not admin:
        user=User()
        user.name='admin'
        user.name="admin"
        user.role=0
        user.password=md5("xiaokang") 
        conn.add(user)
        conn.flush()
    return HTTPFound(location=request.route_url('public_lesson_list'))
