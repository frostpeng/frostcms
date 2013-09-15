# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from .models import DBSession,Semester,Lesson,Course,and_,Location
import webhelpers.paginate as paginate
from datetime import date  
from frostcms.models import Lesson_Location, Course_Class
from frostcms.utils import getStudentnumOfCourse,getLeftSeatByLocation
import time

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('lesson_listbycourse', '/lesson/listbycourse')
    config.add_route('lesson_list', '/lesson/list')
    config.add_route('lesson_addtocourse', '/lesson/addtocourse')
    config.add_route('lesson_save', '/lesson/save')
    config.add_route('lesson_del', '/lesson/del')
    config.add_route('api_location_studentnum_list','api/location_studentnum/list')
    
@view_config(route_name='lesson_listbycourse', renderer='lesson/lesson_listbycourse.mako',permission='admin')
def listlessonsbycourse(request):
    page = int(request.params.get('page', 1))
    courseid=request.params.get('courseid')
    conn = DBSession()
    course=conn.query(Course).filter(Course.id==courseid).first()
    course_classes=conn.query(Course_Class).filter(Course_Class.courseid==courseid)
    course.course_classes=course_classes
    items=conn.query(Lesson).filter(Lesson.courseid==courseid)
    for item in items:
        lesson_locations=conn.query(Lesson_Location).filter(Lesson_Location.lessonid==item.id)
        item.lesson_locations=lesson_locations
        
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,course=course)
    
@view_config(route_name='lesson_list', renderer='lesson/lesson_list.mako',permission='admin')
def listlesson(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    semesters = conn.query(Semester).order_by(Semester.id)
    if request.method == "POST":
        semesterid = request.params.get('semesterid')
        items = conn.query(Lesson,Course).filter(and_(Lesson.courseid==Course.id,Course.semesterid==semesterid))
    else :
        items = conn.query(Lesson).order_by(Lesson.id)
    semesters = conn.query(Semester).order_by(Semester.id)
    lis = []
    class List_semester():
        def __init__(self):
            self.id = 0
            self.name = ""
            self.time = ""
            self.weeks = 0
    for semester in semesters:
        t = List_semester()
        t.id = semester.id
        t.time = date.fromtimestamp(semester.start)
        t.weeks = semester.weeks
        time = t.time
        name = str(time.year)
        mon = time.month
        if  mon >7 :
            name += u"年秋季"
        else :
            name += u"年春季"
        t.name = name 
        lis.append(t)
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,lis=lis)
 
@view_config(route_name='lesson_addtocourse', renderer='lesson/lesson_add.mako',permission='admin')
def lesson_addtocourse(request):
    conn = DBSession()
    courseid=request.params.get('courseid')
    course=conn.query(Course).filter(Course.id==courseid).first()
    studentnum=getStudentnumOfCourse(courseid)
    return dict(course=course,studentnum=studentnum)    
 
@view_config(route_name='lesson_save', renderer='lesson/lesson_add.mako',permission='admin')
def savelesson(request):
    conn = DBSession()
    locations=request.params.getall('locationid')
    studentnums=request.params.getall('studentnum')
    params_tuple=['lesson.id','lesson.courseid','lesson.week','lesson.dow','lesson.starttime','lesson.endtime']
    lesson_id,courseid,week,dow,start,end=[request.params.get(x) for x in params_tuple]
    lesson = conn.query(Lesson).filter(Lesson.id==lesson_id).first()
    if lesson:
        lesson.courseid = courseid
        lesson.week = week
        lesson.dow = dow
        lesson.start = start
        lesson.end = end
        lesson.state = 1
        lesson.updatetime=time.time()
        conn.flush()
    else:
        lesson = Lesson()
        lesson.courseid = courseid
        lesson.week = week
        lesson.dow = dow
        lesson.start = start
        lesson.end = end
        lesson.state = 1
        lesson.createtime=time.time()
        lesson.updatetime=time.time()
        conn.add(lesson)
    conn.flush()
    for i in range(0,len(locations)):
        lesson_location=Lesson_Location()
        lesson_location.lessonid=lesson.id
        lesson_location.locationid=int(locations[i])
        lesson_location.studentnum=int(studentnums[i])
        conn.add(lesson_location)
    conn.flush()
    return HTTPFound(location=request.route_url('lesson_listbycourse',_query={'courseid':courseid}))
 
@view_config(route_name='lesson_del', renderer='lesson/lesson_del.mako',permission='admin')
def dellesson(request):
    conn = DBSession()
    lessonid=request.params.get('lessonid')
    lesson = conn.query(Lesson).filter(Lesson.id==lessonid).first()
    courseid=lesson.courseid
    if lesson:
        conn.delete(lesson)
        conn.flush()
        return HTTPFound(location=request.route_url('lesson_list'))
    return HTTPFound(location=request.route_url('lesson_listbycourse',_query={'courseid':courseid}))

@view_config(route_name='api_location_studentnum_list', renderer='jsonp',permission='admin')
def api_location_studentnum_list(request):
    """返回位置学生总数，需要传入week,dow,start,end
    """
    params_tuple=['week','dow','start','end']
    week,dow,start,end=[request.params.get(x) for x in params_tuple]
    conn = DBSession()
    loclist=[]
    locations=conn.query(Location).all()
    if int(end)-int(start)>2:
        lessonnum1=int(start)/2
        lessonnum2=int(end)/2-1
        
        for location in locations:
            location.leftnum=min(getLeftSeatByLocation(location.id, lessonnum1, week, dow),\
                                 getLeftSeatByLocation(location.id, lessonnum2, week, dow))
            loclist.append({'id':location.id,'leftnum':location.leftnum,'name':location.name})
            
    else:
        lessonnum=int(end)/2-1
        for location in locations:
            location.leftnum=getLeftSeatByLocation(location.id, lessonnum, week, dow)
            loclist.append({'id':location.id,'leftnum':location.leftnum,'name':location.name})
    return dict(locations=loclist)

    