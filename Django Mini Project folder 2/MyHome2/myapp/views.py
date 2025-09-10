from django.shortcuts import render
from django.http import HttpResponse
import datetime

from myapp.models import Employee,Student,Login,Additem

from .import forms

from myapp.models import Student,Movie
from myapp.forms import StudentForm1,StudentForm,MovieForm,LoginForm,Itemaddform

#for class based view
from django.views.generic import View,ListView



# Create your views here.

def display(request):
    s="<h1>Hello Student welcome to django</h1>"


    return HttpResponse(s)
def date(request):
    time=datetime.datetime.now()
    s1='<h1>Hello current date and time is '+str(time)+'</h1>'

    return HttpResponse(s1)

def wish(request):

    return render(request,'wish.html')

def dt(request):

    date2=datetime.datetime.now()

    mydict={'insert_date':date2}

    return render(request,'datetime.html',mydict)
#----------------------------------------------------


def durga(request):
    return render(request,'index.html')

def movie(request):

    mydict1={
        'head_msg':'Movies Information',
        'sub_msg1':'I am here',
        'sub_msg2':'I am not here',
        'sub_msg3':'i am there',
        'photo':'static/13.jpg'
    }

    return render(request,'news.html',mydict1)
def sport(request):
    mydict2={
        'head_msg':'Sports Information',
        'sub_msg1':'I am jayesh',
        'sub_msg2':'I like chess ',
        'sub_msg3':'i also like cricket',
        'photo':'static/13.jpg'
    }
    return render(request,'news.html',mydict2)
def politic(request):

    mydict3={
        'head_msg':'Politics Information',
        'sub_msg1':'I dont like it',
        'sub_msg2':'narendra modi is prime minister of india ',
        'sub_msg3':'Good Morning',
        'photo':'static/13.jpg'

    }
    return render(request,'news.html',mydict3)


#--------------------------------------------

def empdata(request):

    emplist=Employee.objects.all()

    mydict4={'emp_list':emplist}


    return render(request,'emp.html',context=mydict4)

def stud(request):
    stud=Student.objects.order_by('marks')

    mydict5={'stud':stud}

    return render(request,'student.html',context=mydict5)

def studentinputview(request):
    form=forms.StudentForm()

    mydict6={
        'form':form
    }
    return render(request,'form.html',mydict6)

def studentinputview2(request):

    form=forms.StudentForm1()

    if request.method=='POST':

        form=forms.StudentForm1(request.POST)

        if form.is_valid():

            form.save(commit=True)

    return render(request,'form2.html',{'form':form})


def indexview23(request):

    return render(request,'movieform.html')

def addmovie(request):

    form=MovieForm()

    if  request.method=='POST':
        form=MovieForm(request.POST)


        if form.is_valid():

            form.save()

        return indexview23(request)
    
    return render(request,'addmovie.html',{'form':form})

def listmovie(request):

    movie_list=Movie.objects.all().order_by('-rating')

    return render(request,'listmovie.html',{'movie_list':movie_list})

def countview(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1

    else:

        newcount=1
    response=render(request,'count.html',{'count':newcount})

    response.set_cookie('count',newcount)
    return response

def homeview1(request):
    form=LoginForm()

    return render(request,'homeview.html',{'form':form})


def datetimeview(request):
    name=request.GET['name']

    response=render(request,'datetime12.html',{'name':name})

    response.set_cookie('name',name)

    return response
def resultview(request):
    name1=request.COOKIES['name']
    datetime1=datetime.datetime.now()

    mydict7={'name':name1,'datetime':datetime1}



    return render(request,'resultview.html',mydict7)


def name1(request):
    return render(request,'name1.html')
def age1(request):
    name=request.GET['name']

    response=render(request,'age1.html',{'name':name})

    response.set_cookie('name',name)

    return response
def gf1(request):
    age=request.GET['age']


    name=request.COOKIES['name']
    response=render(request,'gf1.html',{'name':name})
    response.set_cookie('age',age)
    return response
def result1(request):
    gf=request.GET['gf']
    name=request.COOKIES['name']
    age=request.COOKIES['age']

    response=render(request,'result1.html',{'name':name,'age':age,'gf':gf})

    response.set_cookie('gf',gf)

    return response

def indexform(request):

    return render(request,'addform.html')

def additem(request):
    form=Itemaddform()
    response=render(request,'additem.html',{'form':form})

    if request.method=='POST':
        form=Itemaddform(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            quantity=form.cleaned_data['quantity']

            response.set_cookie(name,quantity,180)

    return response
def displayitem(request):

    return render(request,'displayitem.html')



#Class based views

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse("result")
    




