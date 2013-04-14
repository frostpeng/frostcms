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
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    password = Column(String(50),nullable=False)
    role = Column(Integer, default=0)
    regtime=Column(Integer)
    lastlogin=Column(Integer)
    logintimes=Column(Integer)

class Assignment(Base):     #Assignment
    __tablename__ = 'assignment'
    id = Column(Integer, primary_key=True)
    description = Column(String(2000))
    duedate = Column(Integer)
    lessonid = Column(Integer,ForeignKey('lesson.id'))
    lesson = relationship("Lesson")
    
class AssignUpload(Base):   #AssignmentUpload
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
    __tablename__ = 'clazz'
    id = Column(Integer,primary_key=True)
    num = Column(Integer)
    grade = Column(Integer)
    faculty = Column(Integer)

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True)
    classnum = Column(Integer)
    grade = Column(Integer)
    faculty = Column(Integer)
 
class Course_Class(Base):   #CourseClassMap
    __tablename__ = 'course_class'
    id = Column(Integer,primary_key=True)
    courseid = Column(Integer,ForeignKey('course.id'))
    clazzid = Column(Integer,ForeignKey('clazz.id')) 
    course = relationship("Course")
    clazz = relationship("Clazz")
    
class Faculty(Base):    #Faculty
    __tablename__ = 'faculty'
    id = Column(Integer,primary_key=True)
    name = Column(String(30))
    collegeid = Column(Integer,ForeignKey('college.id')) #SchoolID
    college = relationship("College")
    
class Lesson(Base):     #Lesson
    __tablename__ = 'lesson'
    id = Column(Integer,primary_key=True)
    courseid = Column(Integer,ForeignKey('course.id'))
    week = Column(Integer)
    dow = Column(Integer) #DayOfWeek
    locationid = Column(Integer,ForeignKey('location.id'))
    firstrow = Column(Integer)
    lastrow = Column(Integer)
    ext_location = Column(Integer)
    ext_firstrow = Column(Integer)
    ext_lastrow = Column(Integer)
    starttime = Column(Integer)
    endtime = Column(Integer)
    monopolize = Column(Boolean)
    course = relationship("Course")
    location = relationship("Location")
    
class LessonRequest(Base):      #LessonRequest
    __tablename__ = 'lessonrequest'
    id = Column(Integer,primary_key=True)
    courseid = Column(Integer,ForeignKey('course.id'))
    mentorid = Column(Integer,ForeignKey('mentor.id'))
    week = Column(Integer)
    dow = Column(Integer)
    locationid = Column(Integer,ForeignKey('location.id'))
    firstrow = Column(Integer)
    lastrow = Column(Integer)
    ext_location = Column(Integer)
    ext_firstrow = Column(Integer)
    ext_lastrow = Column(Integer)
    starttime = Column(Integer)
    endtime = Column(Integer)
    approved = Column(Boolean)
    requesttime = Column(Integer)
    closedtime = Column(Integer)
    monopolize = Column(Boolean)
    course = relationship("Course")
    mentor = relationship("Mentor")
    location = relationship("Location")
    
class Location(Base):   #Location
    __tablename__ = 'location'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    address = Column(String(50))
    perrow = Column(Integer)
    totalrows = Column(Integer)
    
class Mentor(Base):
    __tablename__ = 'mentor'
    id = Column(Integer,primary_key=True)
    account = Column(Integer,ForeignKey('user.id'))
    identity = Column(String(12))
    name = Column(String(20))
    gender = Column(String(1))
    collegeid = Column(Integer,ForeignKey('college.id'))
    title = Column(String(15))
    email = Column(String(30))
    phone = Column(String(15))
    decription = Column(String(1000))
    user = relationship("User")
    college = relationship("College")
    
class College(Base):    #School
    __tablename__ = 'college'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    
class Semester(Base):
    __tablename__ = 'semester'
    id = Column(Integer,primary_key=True)
    start = Column(Integer)
    weeks = Column(Integer)
    
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    account = Column(Integer,ForeignKey('user.id'))
    identity = Column(String(12))
    name = Column(String(20))
    clazzid = Column(Integer,ForeignKey('clazz.id'))
    user = relationship("User")
    clazz = relationship("Clazz")
    
    

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)