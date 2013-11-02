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
    params_tuple=['week','locationid','area','dow']
    week,locationid,area,dayofweek=[request.params.get(x) for x in params_tuple]
    locationdictionary=conn.query(Location).order_by(Location.id)
    loc = conn.query(Location).filter(Location.id==locationid).first()
    class Acolum():
        def __init__(self):
            self.courses = []
            self.studentnum = 0
    class Aroom():
        def __init__(self):
            self.location = None
            self.lessons = [Acolum(),Acolum(),Acolum(),Acolum(),Acolum(),Acolum()]
    items = []
    if loc :
        seatnum = loc.seatnum
    else:
        seatnum = 0
   
    courses = []
    if dayofweek and int(dayofweek)>=7 and week and locationid:
        locations = conn.query(Lesson_Location).filter(Lesson_Location.locationid==locationid)
        for location in locations:
            if  location.lesson.week == int(week) and location.lesson.state == 1 and location.lesson.course.semesterid==request.thissemester.id:
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
    elif dayofweek and 0<=int(dayofweek)<=6 and week :
        cours = conn.query(Course.id).filter(Course.semesterid==request.thissemester.id).all()
        if locationid and int(locationid)!=-1 :
            lots = conn.query(Location).filter(Location.id==int(locationid))
        elif area and int(area)!=-1:
            lots = conn.query(Location).filter(Location.area==int(area))
        else :
            lots = []
        locations = []
        for lot in lots:
            locations.append(lot.id)
        courses = []
        les = []
        lessons = []
        lols = []
        def cmpid(lol):
            return lol.locationid
        for cour in cours:
            courses.append(cour.id)
        for course in courses :
            les += conn.query(Lesson).filter(Lesson.state==1,Lesson.week==week,Lesson.dow==int(dayofweek),Lesson.courseid==course).all()
        for le in les :
            lessons.append(le.id)
        for lesson in lessons :
            if (locationid and int(locationid)!=-1) or (area and int(area)!=-1):
                for location in locations :
                    lols += conn.query(Lesson_Location).filter(Lesson_Location.lessonid==lesson,Lesson_Location.locationid==location).all()
            else:
                lols += conn.query(Lesson_Location).filter(Lesson_Location.lessonid==lesson).all()
        lols.sort(key=cmpid)
        sign = 0
        num = 0
        room = None
        for lol in lols :
            if sign!=lol.locationid :
                if room :
                    items.append(room)
                sign=lol.locationid
                room = Aroom()
                room.location = lol.location
            if lol.lesson.start%2!=0:
                start = lol.lesson.start/2
            else :
                start = (lol.lesson.start-1)/2
            if lol.lesson.end%2!=0:
                end = lol.lesson.end/2
            else:
                end = (lol.lesson.end-1)/2
            for time in range(start,end+1) :
                room.lessons[time].courses.append(lol.lesson.course)
                room.lessons[time].studentnum += lol.studentnum
        if room :
            items.append(room)                
    return dict(items=items,week=week,locationid=locationid,area=area,locationdictionary=locationdictionary,seatnum=seatnum,loc=loc,dayofweek=dayofweek)     
    
    
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
