from django.db import models
from django import forms

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20)
    realname = models.CharField(default='无',max_length=20)
    email = models.CharField(max_length = 255 , default= '无')
    phone =  models.CharField(max_length = 30,default = '无')
    password = models.CharField(max_length=10)
    LastLogin = models.DateTimeField()
    TimesLogin = models.IntegerField(4)
    
    def setUsers(self , username , realname , email , phone , password , last_log , times_log):
        self.username = username
        self.realname = realname
        self.email = email
        self.phone = phone
        self.password = password
        self.LastLogin = last_log
        self.TimesLogin = times_log

    def getRealname(self):
        return self.realname;

    def getID(self):
        return self.id
        
    def __str__(self):
        return self.username

class Type(models.Model):
    Detail = models.CharField(max_length=255)

    def __str__(self):
        return self.Detail;

class UserInfo(models.Model):
    UserID = models.ForeignKey(Users,related_name='userinfo_user_id')
    TypeFocus = models.CharField(max_length=255)
    scores = models.IntegerField(default='100')

    def __str__(self):
        return self.TypeFocus;

class Questions(models.Model):
    AskUserID = models.ForeignKey(Users,related_name='question_user_id')#提问者id
    TypeID = models.ForeignKey(Type,related_name='question_type_id')  # 问题类型
    Title = models.CharField(max_length=30,default='这是一个问题的描述')#问题标题
    Detail = models.CharField(max_length=255)#问题描述
    Time = models.DateTimeField()
    Solved = models.BooleanField()

    def __str__(self):
        return self.Detail

    def setQue(self,Detail,Time,Solved):
        self.Detail = Detail
        self.Time = Time
        self.Solved = Solved

class Answer(models.Model):
    QuestionID = models.ForeignKey(Questions,related_name = 'answer_question_id')
    UserID = models.ForeignKey(Users,related_name = 'answer_user_id')
    Detail = models.FileField()
    Time = models.DateTimeField()
    Accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.Detail

    def setAns(self,Detail,time,Accepted):
        self.Detail = Detail
        self.Time = time
        self.Accepted = Accepted

class Information(models.Model):
    UserID = models.ForeignKey(Users,related_name='information_user_id')
    Detail = models.TextField()
    Time = models.DateTimeField()

    def __str__(self):
        return self.Detail