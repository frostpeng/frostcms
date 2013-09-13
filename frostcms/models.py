#coding=utf-8
import transaction

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base



from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class User(Base):   #Account
    """包含id，name，密码，注册时间，最后一次登录，用户状态，登录时间
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    password = Column(String(50),nullable=False)
    role = Column(Integer, default=0)
    regtime=Column(Integer)
    lastlogin=Column(Integer)
    logintimes=Column(Integer)
    
class Student(Base):
    """包含id，userid，学号，真名，班级id，用户状态
    """
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    userid = Column(Integer,ForeignKey('user.id'))
    identity = Column(String(12))
    name = Column(String(20))
    clazzid = Column(Integer,ForeignKey('clazz.id'))
    state=Column(Integer)
    createtime=Column(Integer)
    updatetime=Column(Integer)
    user = relationship("User")
    clazz = relationship("Clazz")
    
class Mentor(Base):
    """包含id，userid，工号，真名，性别，学院，头衔，邮件，电话，描述,状态（0为正常，1为锁定，-1为删除）
    """
    __tablename__ = 'mentor'
    id = Column(Integer,primary_key=True)
    userid = Column(Integer,ForeignKey('user.id'))
    identity = Column(String(12))
    name = Column(String(20))
    gender = Column(String(1))
    collegeid = Column(Integer,ForeignKey('college.id'))
    title = Column(String(15))
    email = Column(String(30))
    phone = Column(String(15))
    description = Column(String(1000))
    state=Column(Integer)
    createtime=Column(Integer)
    updatetime=Column(Integer)
    user = relationship("User")
    college = relationship("College")
    

class Assignment(Base):     #Assignment
    """作业包含id，描述，提交时间，对应课堂
    """
    __tablename__ = 'assignment'
    id = Column(Integer, primary_key=True)
    description = Column(String(2000))
    duedate = Column(Integer)
    lessonid = Column(Integer,ForeignKey('lesson.id'))
    lesson = relationship("Lesson")
    
class AssignUpload(Base):   #AssignmentUpload
    """作业提交包含作业id，学生id，文件路径，提交时间，最后修改时间，修改次数，分数
    """
    __tablename__ = 'assignupload'
    id = Column(Integer, primary_key=True)
    assignmentid = Column(Integer,ForeignKey('assignment.id'))
    studentid = Column(Integer,ForeignKey('student.id'))
    filepath = Column(String(300))
    subtime = Column(Integer)
    lastmodified = Column(Integer)
    modifiedtimes = Column(Integer)
    grade = Column(Integer)
    assignment = relationship("Assignment")
    student = relationship("Student")

class Clazz(Base):  #Class
    """班级包含班级号，年级，院系id,浮动率
    """
    __tablename__ = 'clazz'
    id = Column(Integer,primary_key=True)
    num = Column(Integer)
    year = Column(Integer)
    mulfloat=Column(Float,default=1)
    facultyid = Column(Integer,ForeignKey('faculty.id'))
    faculty = relationship("Faculty")

class Course(Base):
    """课程包含id，课程名，老师名，学期名
    """
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    mentorid = Column(Integer,ForeignKey('mentor.id'))
    semesterid = Column(Integer,ForeignKey('semester.id'))
    mentor = relationship("Mentor")
    semester = relationship("Semester")
 
class Course_Class(Base):   #CourseClassMap
    """课程与班级对应关系包含id，课程id，班级id
    """
    __tablename__ = 'course_class'
    id = Column(Integer,primary_key=True)
    courseid = Column(Integer,ForeignKey('course.id'))
    clazzid = Column(Integer,ForeignKey('clazz.id')) 
    course = relationship("Course")
    clazz = relationship("Clazz")
    
class Faculty(Base):    #Faculty
    __tablename__ = 'faculty'
    """院系包含院系名和学院id
    """
    id = Column(Integer,primary_key=True)
    name = Column(String(30))
    collegeid = Column(Integer,ForeignKey('college.id')) #SchoolID
    college = relationship("College")
    
class Lesson(Base):     #Lesson
    """课堂包含课程id，周次，周几，(实验室id，第一行，最后一行,人数)的数组，开始节数，结束节数,课程状态(包括申请中，申请结束，被拒绝)
       课程可以提供所有的班级信息，课程与课堂的多个对应也是相当于一对多的形式，如果是mongodb的话可能会方便很多，但是目前也不影响实现细节
    """
    __tablename__ = 'lesson'
    id = Column(Integer,primary_key=True)
    courseid = Column(Integer,ForeignKey('course.id'))
    week = Column(Integer)
    dow = Column(Integer) #DayOfWeek
    start = Column(Integer)
    end = Column(Integer)
    state=Column(Integer,default=0)
    createtime=Column(Integer)
    updatetime=Column(Integer)
    course = relationship("Course")
    
class Lesson_Location(Base):
    """课堂和位置对应关系包含课程id，locationid以及需要占用的位置数量
    """
    __tablename__ = 'lesson_location'
    id = Column(Integer,primary_key=True)
    lessonid = Column(Integer,ForeignKey('lesson.id'))
    locationid = Column(Integer,ForeignKey('location.id'))
    studentnum=Column(Integer)
    lesson = relationship("Lesson")
    location = relationship("location")
    firstrow = Column(Integer)
    lastrow = Column(Integer)
    lesson = relationship("Lesson")
    location = relationship("Location")

    
class Location(Base):   #Location
    """实验室
    """
    __tablename__ = 'location'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    address = Column(String(50))
    perrow = Column(Integer)
    totalrows = Column(Integer)
    seatnum=Column(Integer,nullable=False,default=0)
    area = Column(Integer)
    

    
class College(Base):    #School
    """学院包括id和名字
    """
    __tablename__ = 'college'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    
class Semester(Base):
    """学期包括开始时间和周数，需要自动生成为最佳，凡是查找不到或者需要依靠的地方都会自动生成
    """
    __tablename__ = 'semester'
    id = Column(Integer,primary_key=True)
    start = Column(Integer)
    weeks = Column(Integer)
    
    

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)