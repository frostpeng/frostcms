# coding=utf-8
'''错误代码为9**
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from logging import getLogger
from frostcms.models import *
import webhelpers.paginate as paginate
from datetime import date  
from frostcms.utils import getStudentnumOfCourse,getLeftSeatByLocation
import time

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('admin_lesson_undolist', '/admin/lesson/undolist')
    config.add_route('admin_lesson_agree', '/admin/lesson/agree')
    config.add_route('admin_lesson_disagree', '/admin/lesson/disagree')
    config.add_route('lesson_listbycourse', '/lesson/listbycourse')
    config.add_route('mentor_lesson_listbycourse', '/mentor/lesson/listbycourse')
    config.add_route('student_lesson_listbycourse', '/student/lesson/listbycourse')
    config.add_route('lesson_list', '/lesson/list')
    config.add_route('lesson_addtocourse', '/lesson/addtocourse')
    config.add_route('mentor_lesson_addtocourse', '/mentor/lesson/addtocourse')
    config.add_route('admin_lesson_edit', '/admin/lesson/edit')
    config.add_route('lesson_save', '/lesson/save')
    config.add_route('mentor_lesson_save', '/mentor/lesson/save')
    config.add_route('lesson_del', '/lesson/del')
    config.add_route('mentor_lesson_del', '/mentor/lesson/del')
    config.add_route('api_location_studentnum_list','api/location_studentnum/list')
    config.add_route('lesson_notice_list','/lesson/notice/list')
    config.add_route('lesson_notice_watch','/lesson/notice/watch')
    config.add_route('lesson_notice_del','/lesson/notice/del')
    
@view_config(route_name='lesson_listbycourse', renderer='lesson/lesson_listbycourse.mako',permission='admin')
def listlessonsbycourse(request):
    page = int(request.params.get('page', 1))
    courseid=request.params.get('courseid')
    conn = DBSession()
    course=conn.query(Course).filter(Course.id==courseid).first()
    course_classes=conn.query(Course_Class).filter(Course_Class.courseid==courseid).all()
    course.course_classes=course_classes
    items=conn.query(Lesson).filter(Lesson.courseid==courseid,Lesson.state!=-1).all()
    for item in items:
        lesson_locations=conn.query(Lesson_Location).filter(Lesson_Location.lessonid==item.id).all()
        item.lesson_locations=lesson_locations
        
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items,course=course)

@view_config(route_name='admin_lesson_undolist', renderer='lesson/admin_lesson_undolist.mako',permission='admin')
def admin_lesson_undolist(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    items=conn.query(Lesson).filter(Lesson.state==0).all()
    for item in items:
        lesson_locations=conn.query(Lesson_Location).filter(Lesson_Location.lessonid==item.id).all()
        item.lesson_locations=lesson_locations
        
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
    return dict(items=items)

@view_config(route_name='admin_lesson_agree', renderer='lesson/lesson_add.mako',permission='admin')
def admin_lesson_agree(request):
    conn = DBSession()
    lessonid=request.params.get('lessonid')
    lesson = conn.query(Lesson).filter(Lesson.id==lessonid).first()
    if lesson:
        lesson.state=1
        lwi = LessonWorkItem()
        lwi.lessonid = lesson.id
        lwi.senduserid = request.user.id
        lwi.acceptuserid = lesson.course.mentor.user.id
        lwi.action = 1
        lwi.actiontime = time.time()
        conn.add(lwi)
        conn.flush()
        return HTTPFound(location=request.route_url('admin_lesson_undolist'))                  
    return HTTPFound(location=request.route_url('admin_lesson_undolist'))

@view_config(route_name='admin_lesson_disagree', renderer='lesson/lesson_add.mako',permission='admin')
def admin_lesson_disagree(request):
    conn = DBSession()
    lessonid=request.params.get('lessonid')
    lesson = conn.query(Lesson).filter(Lesson.id==lessonid).first()
    if lesson:
        lesson.state=2
        lwi = LessonWorkItem()
        lwi.lessonid = lesson.id
        lwi.senduserid = request.user.id
        lwi.acceptuserid = lesson.course.mentor.user.id
        lwi.action = 2
        lwi.actiontime = time.time()
        conn.add(lwi)
        conn.flush()
        return HTTPFound(location=request.route_url('admin_lesson_undolist'))                  
    return HTTPFound(location=request.route_url('admin_lesson_undolist'))

@view_config(route_name='mentor_lesson_listbycourse', renderer='lesson/mentor_lesson_listbycourse.mako',permission='mentor')
def mentor_lesson_listbycourse(request):
    page = int(request.params.get('page', 1))
    courseid=request.params.get('courseid')
    conn = DBSession()
    course=conn.query(Course).filter(Course.id==courseid,Course.mentorid.in_(\
            conn.query(Mentor.id).filter(Mentor.userid==request.user.id))).first()
    if course:
        course_classes=conn.query(Course_Class).filter(Course_Class.courseid==course.id).all()
        course.course_classes=course_classes
        items=conn.query(Lesson).filter(Lesson.courseid==course.id,Lesson.state!=-1).all()
        for item in items:
            lesson_locations=conn.query(Lesson_Location).filter(Lesson_Location.lessonid==item.id).all()
            item.lesson_locations=lesson_locations
            
        page_url = paginate.PageURL_WebOb(request)
        items = paginate.Page(items,page=int(page),items_per_page=10,url=page_url,)
        return dict(items=items,course=course)
    return dict(code=0,error=u"课程不存在")

@view_config(route_name='student_lesson_listbycourse', renderer='lesson/student_lesson_listbycourse.mako',permission='student')
def student_lesson_listbycourse(request):
    page = int(request.params.get('page', 1))
    courseid=request.params.get('courseid')
    conn = DBSession()
    course=conn.query(Course).filter(Course.id==courseid).first()
    if course:
        course_classes=conn.query(Course_Class).filter(Course_Class.courseid==course.id).all()
        course.course_classes=course_classes
        items=conn.query(Lesson).filter(Lesson.courseid==course.id,Lesson.state==1).all()
        for item in items:
            lesson_locations=conn.query(Lesson_Location).filter(Lesson_Location.lessonid==item.id).all()
            item.lesson_locations=lesson_locations
        page_url = paginate.PageURL_WebOb(request)
        items = paginate.Page(items,page=int(page),items_per_page=10,url=page_url,)
        return dict(items=items,course=course)
    return dict(code=0,error=u"课程不存在")


    
@view_config(route_name='lesson_list', renderer='lesson/lesson_list.mako',permission='admin')
def listlesson(request):
    page = int(request.params.get('page', 1))
    conn = DBSession()
    semesters = conn.query(Semester).order_by(Semester.id)
    if request.method == "POST":
        semesterid = request.params.get('semesterid')
        items = conn.query(Lesson,Course).filter(Lesson.courseid==Course.id,Course.semesterid==semesterid).all()
    else :
        items = conn.query(Lesson).order_by(Lesson.id).all()
    semesters = conn.query(Semester).order_by(Semester.id).all()
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

@view_config(route_name='mentor_lesson_addtocourse', renderer='lesson/mentor_lesson_addtocourse.mako',permission='mentor')
def mentor_lesson_addtocourse(request):
    conn = DBSession()
    courseid=request.params.get('courseid')
    course=conn.query(Course).filter(Course.id==courseid,Course.mentorid.in_(\
            conn.query(Mentor.id).filter(Mentor.userid==request.user.id))).first()
    if course:
        studentnum=getStudentnumOfCourse(courseid)
        return dict(course=course,studentnum=studentnum)
    else :
        lessonid = request.params.get('lessonid')
        lesson = conn.query(Lesson).filter(Lesson.id==lessonid).first()
        course = conn.query(Course).filter(Course.id==lesson.courseid).first()
        studentnum=getStudentnumOfCourse(lesson.courseid)
        locations = conn.query(Lesson_Location).filter(Lesson_Location.lessonid==lessonid)
        studenthave = 0
        for location in locations :
            studenthave += location.studentnum
        return dict(lesson=lesson,course=course,studentnum=studentnum,locations=locations,studenthave=studenthave)
    return dict(code=0,error=u'课程不存在')   

@view_config(route_name='admin_lesson_edit', renderer='lesson/lesson_add.mako',permission='admin')
def admin_lesson_edit(request):
    conn = DBSession()
    lessonid=request.params.get('lessonid')
    lesson=conn.query(Lesson).filter(Lesson.id==lessonid).first()
    if lesson:
        lessonlocations=conn.query(Lesson_Location).filter(Lesson_Location.lessonid==lessonid).all()
        lesson.lessonlocations=lessonlocations
        studentnum=getStudentnumOfCourse(lesson.courseid)
        return dict(lesson=lesson,studentnum=studentnum,course=lesson.course) 
    return dict(code=0,error=u'课堂不存在')   
 
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
        conn.query(Lesson_Location).filter(Lesson_Location.lessonid==lesson.id).delete()
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

@view_config(route_name='mentor_lesson_save', renderer='lesson/mentor_lesson_addtocourse.mako',permission='mentor')
def mentor_lesson_save(request):
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
        lesson.state = 0
        lesson.updatetime=time.time()
        conn.query(Lesson_Location).filter(Lesson_Location.lessonid==lesson.id).delete()
    else:
        lesson = Lesson()
        lesson.courseid = courseid
        lesson.week = week
        lesson.dow = dow
        lesson.start = start
        lesson.end = end
        lesson.state = 0
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
    return HTTPFound(location=request.route_url('mentor_lesson_listbycourse',_query={'courseid':courseid}))
 
@view_config(route_name='lesson_del', renderer='lesson/lesson_del.mako',permission='admin')
def dellesson(request):
    conn = DBSession()
    lessonid=request.params.get('lessonid')
    lesson = conn.query(Lesson).filter(Lesson.id==lessonid).first()
    courseid=lesson.courseid
    if lesson:
        lesson.state = -1
        lwi = LessonWorkItem()
        lwi.lessonid = lesson.id
        lwi.senduserid = request.user.id
        lwi.acceptuserid = lesson.course.mentor.user.id
        lwi.action = -1
        lwi.actiontime = time.time()
        conn.add(lwi)
        conn.flush()
        return HTTPFound(location=request.route_url('lesson_listbycourse',_query={'courseid':courseid}))
    return HTTPFound(location=request.route_url('lesson_listbycourse',_query={'courseid':courseid}))

@view_config(route_name='mentor_lesson_del', renderer='lesson/lesson_add.mako',permission='mentor')
def mentor_lesson_del(request):
    conn = DBSession()
    lessonid=request.params.get('lessonid')
    lesson = conn.query(Lesson).filter(Lesson.id==lessonid,Lesson.courseid.in_(\
            conn.query(Course.id).filter(Course.mentorid.in_(\
                conn.query(Mentor.id).filter(Mentor.userid==request.user.id))))).first()
    courseid=lesson.courseid
    if lesson:
        lesson.state = -1
        lwi = LessonWorkItem()
        lwi.lessonid = lesson.id
        lwi.senduserid = request.user.id
        lwi.acceptuserid = 1 #admin.id
        lwi.action = -1
        lwi.actiontime = time.time()
        conn.add(lwi)
        conn.flush()
        return HTTPFound(location=request.route_url('mentor_lesson_listbycourse',_query={'courseid':courseid}))
    return HTTPFound(location=request.route_url('mentor_lesson_listbycourse',_query={'courseid':courseid}))

@view_config(route_name='api_location_studentnum_list', renderer='jsonp',permission='user')
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


@view_config(route_name='lesson_notice_list', renderer='notice/notice_lesson_list.mako',permission='user')
def notice_lesson_list(request):
    conn = DBSession()
    page = int(request.params.get('page', 1))
    userid = request.user.id
    items = conn.query(LessonWorkItem).filter(LessonWorkItem.acceptuserid==userid).order_by(LessonWorkItem.viewstate,desc(LessonWorkItem.actiontime))
    page_url = paginate.PageURL_WebOb(request)
    items = paginate.Page(
            items,
            page=int(page),
            items_per_page=12,
            url=page_url,
            )
    return dict(items=items)
    
@view_config(route_name='lesson_notice_watch', renderer='notice/notice_lesson_watch.mako',permission='user')
def notice_lesson_watch(request):
    conn = DBSession()
    workid=request.params.get('workid')
    userid = request.user.id
    if workid :
        notice = conn.query(LessonWorkItem).filter(LessonWorkItem.id==workid,LessonWorkItem.acceptuserid==userid).first()
        notice.viewstate = 1
        conn.flush()
    else :
        notice = None
    return dict(notice=notice)

@view_config(route_name='lesson_notice_del', renderer='notice/notice_lesson_watch.mako',permission='user')
def notice_lesson_del(request):
    conn = DBSession()
    workid=request.params.get('workid')
    userid = request.user.id
    if workid :
        notice = conn.query(LessonWorkItem).filter(LessonWorkItem.id==workid,LessonWorkItem.acceptuserid==userid).first()
        conn.delete(notice)
        conn.flush()
    return HTTPFound(location=request.route_url('lesson_notice_list'))