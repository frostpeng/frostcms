#encoding=utf-8
'''
Created on 2013年9月10日

@author: frost
'''
from frostcms.models import DBSession,Course_Class,Student,Location,Course,Lesson,Lesson_Location,\
    Clazz
from logging import getLogger
from sqlalchemy import func
from test.test_threading_local import Weak

log = getLogger(__name__)


def md5(str):
    import md5 
    m = md5.new()
    m.update(str) 
    return m.hexdigest() 

def getStudentnumOfCourse(courseid):
    """获得某门课程所有学生总数
    """
    conn=DBSession()
    courseclasslist=conn.query(Course_Class).filter(Course_Class.courseid==courseid).all()
    studentnum=0
    for courseclazz in courseclasslist:
        students=conn.query(Student).filter(Student.clazzid==courseclazz.clazzid)
        clazz=conn.query(Clazz).filter(Clazz.id==courseclazz.clazzid).first()
        studentnum=studentnum+students.count()*(clazz.mulfloat)
    return int(studentnum)

def getLeftSeatByLocation(locationid,lessonnum,week,dow):
    """由位置和开始结束时间获取座位数,lessonnum为课堂的节数
    """
    conn=DBSession()
    startclass=lessonnum*2+1
    endclass=lessonnum*2+2
    location=conn.query(Location).filter(Location.id==locationid).first();
    seatnum=location.seatnum;
    lessonlocations=conn.query(Lesson_Location).filter(Lesson_Location.lessonid.in_
                    (conn.query(Lesson.id).filter(Lesson.start<=startclass,\
                    Lesson.end>=endclass,Lesson.week==week,Lesson.dow==dow)),\
                    Lesson_Location.locationid==locationid).all()
    usedseat=0
    for lessonlocation in lessonlocations:
        usedseat=usedseat+lessonlocation.studentnum
    return(seatnum-usedseat)
        
    
    
