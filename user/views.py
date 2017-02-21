from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from .models import Information
from .models import Answer
from .models import Questions
from .models import Type
from django.template import loader,RequestContext
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import StreamingHttpResponse
from django.core import serializers
# Create your views here.

def login(request):
    return render(request,'user/login.html')

def dologin(request):
    _username = request.POST['username']
    _pwd = request.POST['password']
    
    try:#判断表中是否存在记录
        #Users.objects.get(username = _username)
        user_in_db = Users.objects.get(username = _username)
        if _pwd == user_in_db.password:
            request.session['username'] = _username
            request.session['userid'] = user_in_db.id
            request.session['realname'] = user_in_db.realname
            user_in_db.LastLogin = datetime.datetime.now()
            user_in_db.TimesLogin +=1
            user_in_db.save()
            return HttpResponseRedirect(reverse('Index:index',args=()))
        else:
            return HttpResponse("You are failed to login")
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('Index:index',args=()))
    
def dologout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('Index:index',args=()))

def regist(request):
    return render(request,'user/register.html')

def doregist(request):

    #return HttpResponse("getthere")
    username = request.POST['id']
    pwd = request.POST['pwd']
    repwd = request.POST['repwd']
    realname = request.POST['realname']
    mail = request.POST['mail']
    phone = request.POST['phone']
    mTime = datetime.datetime.now()

    if pwd == repwd:
        mUser = Users()
        mUser.setUsers(username = username,password = pwd, realname = realname,email = mail,phone = phone,last_log = mTime,times_log = 0)
        mUser.save()
        return HttpResponse("successed to regist")
    else:
        return HttpResponse("password you input is different")

def raisequestion(request):

    if request.POST:
        if request.POST['type'] and request.POST['title'] and request.POST['detail']:
            person = Users.objects.get(id=request.session['userid'])
            question = Questions()
            question.AskUserID = person
            question.TypeID = Type.objects.get(id=request.POST['type'])
            question.Title = request.POST['title']
            question.Detail = request.POST['detail']
            question.Time = datetime.datetime.now()
            question.Solved = False
            question.save()

        return HttpResponse('question save successed')
    else :
        if request.session.has_key('username'):
            type = Type.objects.all()
            context = {'typelist':type}
            context['username'] = request.session['username']
            return render(request,'user/RaiseQuestion.html',context)
        else:
            return HttpResponseRedirect(reverse('User:login'))

def userInfo(request):
    if request.session.has_key('username'):
        context = {}
        person = Users.objects.get(id = request.session['userid'])
        usermessage = person.information_user_id.all()
        questionslist = Questions.objects.filter(AskUserID = request.session['userid'])
        anslist = Answer.objects.filter(UserID = request.session['userid'])
        print(len(anslist))
        messageNumber = 0
        context = {'username':request.session['username'],
                       'realname':request.session['realname'],
                       'messagelist':usermessage ,
                       'messageNumber':messageNumber}
        context['questionslist'] = questionslist
        context['anslist'] = anslist
        return render(request,'user/user.html',context)
    else:
        return HttpResponseRedirect(reverse('User:login'))

def passWordChange(request):
    userid = request.session['userid']
    opwd = request.POST['opwd']
    pwd = request.POST['pwd']

    print(opwd)
    person = Users.objects.get(id = userid)
    if pwd == person.password:
        person.password = pwd
        person.save()
    else:
        #return HttpResponse("Your password is not correct")
        pass

    return HttpResponseRedirect(reverse('User:userinfo'))

def up(request):
    return render(request,'user/up.html')

def doup(request):
    mAns = Answer()
    video = request.FILES['video']
    que = Questions.objects.get(id='1')
    user = Users.objects.get(id='1')
    mAns.QuestionID = que
    mAns.UserID = user
    time = datetime.datetime.now()
    mAns.setAns(Detail = video,time = time,Accepted = False)
    mAns.save()

    return HttpResponse("success to upload")
    pass

def down(request):
    mQue = Answer.objects.get(id='2')

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    filename = mQue.Detail.name[2:]
    the_file_name = "../../Work/Python/DProject/up/" + filename
    #return HttpResponse(the_file_name)
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    #response = FileResponse(open(the_file_name,'rb'))

    return response

def multiplebuy(request):
    return render(request,'user/multipleby.html')

def singlebuy(request):
    return render(request,'user/singlebuy.html')

def quelist(request,id):
    qid = id
    que = Questions.objects.get(id = qid)
    author = que.AskUserID
    context = {}
    print(author)
    ans = Answer.objects.filter(QuestionID = qid)
    for i in range(0,len(ans)):
        ans[i].filename = "/user/up/" + ans[i].Detail.name[2:]
    context['que'] = que
    context['author'] = author
    context['ans'] = ans
    print(type(request.session))
    if request.session.has_key('username'):
        context['username'] = request.session['username']
    return render(request,'user/questionshow.html',context)

def questionslist(request):
    context = {}
    quelist = Questions.objects.all()
    context['questionslist'] = quelist
    return render(request,'user/questionslist.html',context)

def doans(request):
    mAns = Answer()
    video = request.FILES['video']
    print(request.POST['queid'])
    que = Questions.objects.get(id=request.POST['queid'])
    user = Users.objects.get(id=request.session['userid'])
    mAns.QuestionID = que
    mAns.UserID = user
    time = datetime.datetime.now()
    mAns.setAns(Detail=video, time=time, Accepted=False)
    mAns.save()

    return HttpResponse("success to upload")

