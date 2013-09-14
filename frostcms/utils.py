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
    classlist=conn.query(Course_Class.clazzid).filter(Course_Class.courseid==courseid)
    studentnum=0
    for clazzid in classlist:
        students=conn.query(Student).filter(Student.clazzid==clazzid)
        mulfloat=conn.query(Clazz.mulfloat).filter_by(id==clazzid)
        studentnum=studentnum+students.count()*mulfloat    
    return studentnum

def getLeftSeatByLocation(locationid,lessonnum,week,dow):
    """由位置和开始结束时间获取座位数,lessonnum为课堂的节数
    """
    conn=DBSession()
    startclass=lessonnum*2+1
    endclass=lessonnum*2+2
    seatnum=conn.query(Location.seatnum).filter_by(id==locationid).first()
    studentnums=conn.query(Lesson_Location.studentnum).filter(Lesson_Location.lessonid.in_
                    (conn.query(Lesson.id).filter(Lesson.start<=startclass,\
                    Lesson.end>=endclass,Lesson.week==week,Lesson.dow==dow)),\
                    Lesson_Location.locationid==locationid).all()
    usedseat=0
    for studentnum in studentnums:
        usedseat=usedseat+studentnum
    return(seatnum-usedseat)
        
    
    
