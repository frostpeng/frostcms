#coding=utf-8
import transaction

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base



from zope.sqlalchemy import ZopeTransactionExtension
from webhelpers.html.tags import password

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
    
    def __json__(self,request):
        return dict(id=self.id,name=self.name,password=self.password,role=self.role,\
                    regtime=self.regtime,lastlogin=self.lastlogin,logintimes=self.logintimes)
        
    
class Student(Base):
    """包含id，userid，学号，真名，班级id，用户状态
    """
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    userid = Column(Integer,ForeignKey('user.id',onupdate="CASCADE", ondelete="SET NULL"))
    identity = Column(String(12))
    name = Column(String(20))
    clazzid = Column(Integer,ForeignKey('clazz.id',onupdate="CASCADE", ondelete="SET NULL"))
    state=Column(Integer)
    createtime=Column(Integer)
    updatetime=Column(Integer)
    user = relationship("User")
    clazz = relationship("Clazz")
    
    def __json__(self,request):
        return dict(id=self.id,userid=self.userid,identity=self.identity,name=self.name,\
             clazzid=self.clazzid,state=self.state,createtime=self.createtime,updatetime=\
             self.updatetime)
    
class Mentor(Base):
    """包含id，userid，工号，真名，性别，学院，头衔，邮件，电话，描述,状态（0为正常，1为锁定，-1为删除）
    """
    __tablename__ = 'mentor'
    id = Column(Integer,primary_key=True)
    userid = Column(Integer,ForeignKey('user.id',onupdate="CASCADE", ondelete="SET NULL"))
    identity = Column(String(12))
    name = Column(String(20))
    gender = Column(String(1))
    collegeid = Column(Integer,ForeignKey('college.id',onupdate="CASCADE", ondelete="SET NULL"))
    title = Column(String(15))
    email = Column(String(30))
    phone = Column(String(15))
    description = Column(String(1000))
    state=Column(Integer)
    createtime=Column(Integer)
    updatetime=Column(Integer)
    user = relationship("User")
    college = relationship("College")
    
    def __json__(self,request):
        return dict(id=self.id,userid=self.userid,identity=self.identity,name=self.name,\
             gender=self.gender,collegeid=self.collegeid,title=self.title,email=self.email,\
             phone=self.phone,description=self.description,state=self.state,createtime=self.createtime,updatetime=\
             self.updatetime)
    

class Assignment(Base):     #Assignment
    """作业包含id，描述，提交时间，对应课堂
    """
    __tablename__ = 'assignment'
    id = Column(Integer, primary_key=True)
    description = Column(String(2000))
    duedate = Column(Integer)
    lessonid = Column(Integer,ForeignKey('lesson.id',onupdate="CASCADE", ondelete="SET NULL"))
    lesson = relationship("Lesson")
    
    def __json__(self,request):
        return dict(id=self.id,description=self.description,duedate=self.duedate,lessonid=self.lessonid)
    
class AssignUpload(Base):   #AssignmentUpload
    """作业提交包含作业id，学生id，文件路径，提交时间，最后修改时间，修改次数，分数
    """
    __tablename__ = 'assignupload'
    id = Column(Integer, primary_key=True)
    assignmentid = Column(Integer,ForeignKey('assignment.id',onupdate="CASCADE", ondelete="SET NULL"))
    studentid = Column(Integer,ForeignKey('student.id',onupdate="CASCADE", ondelete="SET NULL"))
    filepath = Column(String(300))
    subtime = Column(Integer)
    lastmodified = Column(Integer)
    modifiedtimes = Column(Integer)
    grade = Column(Integer)
    assignment = relationship("Assignment")
    student = relationship("Student")
    
    def __json__(self,request):
        return dict(id=self.id,studentid=self.studentid,filepath=self.filepath,subtime=self.subtime,\
             lastmodified=self.lastmodified,modifiedtimes=self.modifiedtimes,grade=self.grade)

class Clazz(Base):  #Class
    """班级包含班级号，年级，院系id,浮动率
    """
    __tablename__ = 'clazz'
    id = Column(Integer,primary_key=True)
    num = Column(Integer)
    year = Column(Integer)
    mulfloat=Column(Float,default=1)
    facultyid = Column(Integer,ForeignKey('faculty.id',onupdate="CASCADE", ondelete="SET NULL"))
    faculty = relationship("Faculty")
    
    def __json__(self,request):
        return dict(id=self.id,num=self.num,year=self.year,mulfloat=self.mulfloat,facultyid=self.facultyid)

class Course(Base):
    """课程包含id，课程名，老师名，学期名
    """
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    mentorid = Column(Integer,ForeignKey('mentor.id',onupdate="CASCADE", ondelete="SET NULL"))
    semesterid = Column(Integer,ForeignKey('semester.id',onupdate="CASCADE", ondelete="SET NULL"))
    mentor = relationship("Mentor")
    semester = relationship("Semester")
    
    def __json__(self,request):
        return dict(id=self.id,name=self.name,mentorid=self.mentorid,semesterid=self.semesterid)
 
class Course_Class(Base):   #CourseClassMap
    """课程与班级对应关系包含id，课程id，班级id
    """
    __tablename__ = 'course_class'
    id = Column(Integer,primary_key=True)
    courseid = Column(Integer,ForeignKey('course.id',onupdate="CASCADE", ondelete="SET NULL"))
    clazzid = Column(Integer,ForeignKey('clazz.id',onupdate="CASCADE", ondelete="SET NULL")) 
    course = relationship("Course")
    clazz = relationship("Clazz")
    
    def __json__(self,request):
        return dict(id=self.id,courseid=self.courseid,clazzid=self.clazzid)
    
class Faculty(Base):    #Faculty
    __tablename__ = 'faculty'
    """院系包含院系名和学院id
    """
    id = Column(Integer,primary_key=True)
    name = Column(String(30))
    collegeid = Column(Integer,ForeignKey('college.id',onupdate="CASCADE", ondelete="SET NULL")) #SchoolID
    college = relationship("College")
    
    def __json__(self,request):
        return dict(id=self.id,name=self.name,collegeid=self.collegeid)
    
class Lesson(Base):     #Lesson
    """课堂包含课程id，周次，周几，(实验室id，第一行，最后一行,人数)的数组，开始节数，结束节数,课程状态(包括申请中，申请结束，被拒绝)
       课程可以提供所有的班级信息，课程与课堂的多个对应也是相当于一对多的形式，如果是mongodb的话可能会方便很多，但是目前也不影响实现细节
    """
    __tablename__ = 'lesson'
    id = Column(Integer,primary_key=True)
    courseid = Column(Integer,ForeignKey('course.id',onupdate="CASCADE", ondelete="SET NULL"))
    week = Column(Integer)
    dow = Column(Integer) #DayOfWeek
    start = Column(Integer)
    end = Column(Integer)
    state=Column(Integer,default=0)
    createtime=Column(Integer)
    updatetime=Column(Integer)
    course = relationship("Course")
    
    def __json__(self,request):
        return dict(id=self.id,courseid=self.courseid,week=self.week,dow=self.dow,start=self.start,\
            end=self.end,state=self.state,createtime=self.createtime,updatetime=self.updatetime)
    
class Lesson_Location(Base):
    """课堂和位置对应关系包含课程id，locationid以及需要占用的位置数量
    """
    __tablename__ = 'lesson_location'
    id = Column(Integer,primary_key=True)
    lessonid = Column(Integer,ForeignKey('lesson.id',onupdate="CASCADE", ondelete="SET NULL"))
    locationid = Column(Integer,ForeignKey('location.id',onupdate="CASCADE", ondelete="SET NULL"))
    studentnum=Column(Integer,default=0)
    firstrow = Column(Integer,default=0)
    lastrow = Column(Integer,default=0)
    lesson = relationship("Lesson")
    location = relationship("Location")
    
    def __json__(self,request):
        return dict(id=self.id,lessonid=self.lessonid,locationid=self.locationid,studentnum=\
            self.studentnum,firstrow=self.firstrow,lastrow=self.lastrow)

    
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
    
    def __json__(self,request):
        return dict(id=self.id,name=self.name,address=self.address,perrow=self.perrow,\
                    totalrows=self.totalrows,seatnum=self.seatnum,area=self.area)

    
class College(Base):    #School
    """学院包括id和名字
    """
    __tablename__ = 'college'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    
    def __json__(self,request):
        return dict(id=self.id,name=self.name)
    
class Semester(Base):
    """学期包括开始时间和周数，需要自动生成为最佳，凡是查找不到或者需要依靠的地方都会自动生成
    """
    __tablename__ = 'semester'
    id = Column(Integer,primary_key=True)
    start = Column(Integer)
    weeks = Column(Integer)
    
    def __json__(self,request):
        return dict(id=self.id,start=self.start,weeks=self.weeks)
    
class LessonWorkItem(Base):
    """用于记录lesson的处理情况，需要包括lessonid,请求处理人的userid，处理人的id，操作，阅读状态(0为未读，1为已读)，处理时间
        action状态定义为0为申请行为（mentor->admin），1为批准(admin->mentor)，2为拒绝(admin->mentor),3为编辑并批准(admin->mentor)
    """
    __tablename__ = 'lessonworkitem'
    id = Column(Integer,primary_key=True)
    lessonid = Column(Integer,ForeignKey('lesson.id',onupdate="CASCADE", ondelete="SET NULL"))
    acceptuserid=Column(Integer,ForeignKey('user.id',onupdate="CASCADE", ondelete="SET NULL"))
    senduserid=Column(Integer,ForeignKey('user.id',onupdate="CASCADE", ondelete="SET NULL"))
    viewstate=Column(Integer,default=0)
    action=Column(Integer,default=0)
    actiontime=Column(INTEGER)
    lesson = relationship("Lesson")
    acceptuser=relationship("User",foreign_keys=[acceptuserid])
    senduser=relationship("User",foreign_keys=[senduserid])
    
    def __json__(self,request):
        return dict(id=self.id,lessonid=self.lessonid,acceptuserid=self.acceptuserid,senduserid\
                    =self.senduserid,viewstate=self.viewstate,action=self.action,actiontime=\
                    self.actiontime)
    

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)