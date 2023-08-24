from django.shortcuts import render,HttpResponse
from .models import student,Tag, TestCase, Category, Solution,codelearn,exploreitem
from .models import discussitem,user_detail,Cadmin,Cproblem,Newcontest,Cdate,Cupdatesolution,Cupdatetestcase,SubmitestCase
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os,sys
import subprocess
import requests
import threading,time
import base64
from django.contrib.auth.decorators import login_required
from audioop import reverse
from cmath import log
import email
from fnmatch import fnmatch
from re import template
import re
from sqlite3 import Timestamp
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date,datetime
# from .forms import CustomUserCreationForm
# from compilex import compile_code, compile_code_with_input, flush
def accountcreate(request):
    return render (request,'signup.html')

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Save the form data without committing to the database
#             user.set_password(form.cleaned_data['password1'])  # Set the user's password
#             user.save()  # Save the user instance to the database
#             # Log the user in
#             login(request, user)
#             return redirect('home')  # Redirect to your desired page after signup
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'signup.html', {'form': form})
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname =request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['password']
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        user_db=user_detail(user_detail_name=username,user_detail_email=email,user_detail_password=pass1)
        user_db.save()
        user=authenticate(username=username,password=pass1)
        user_status=1
        user_d=request.user
        obj=codelearn.objects.all()
        context={
            'obj':obj,
            "user_d":user_d,
            "user_status":user_status
        }
        if user is not None:
            login(request,user)
            id1=user.id
            return render(request,'codelearn.html',context)
        else:
            return render(request,'loginpage.html')
    else:
        return render(request,'signup.html')
    
        

def loginuser(request):
    if request.method=="POST":
        user_d=request.user
        username=request.POST['username']
        pass1=request.POST['password']
        print(username)
        print(pass1)
        user=authenticate(username=username,password=pass1)
        print
        if user is not None:
            login(request,user)
            id1=user.id
            user_status=1
            obj=codelearn.objects.all()
            context={
                'obj':obj,
                'user_d':user_d,
                'user_status':user_status
            }
            return render(request,'codelearn.html',context)
        else:
            return render(request,'loginpage.html')
    else:
        return render(request,'loginpage.html')
def logoutuser(request):
    logout(request)
    return render(request,'loginpage.html')


def setTimeout(func, delay):
    time.sleep(delay)
    func()

def btoa(input_string):
    input_bytes = input_string.encode('utf-8')
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def atob(input_string):
    input_bytes = input_string.encode('utf-8')
    decoded_bytes = base64.b64decode(input_bytes)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string


def checkstatus(token):
    url = f"https://judge0-ce.p.rapidapi.com/submissions/{token}"

    querystring = {"base64_encoded":"true","fields":"*"}

    # headers = {
    #     "X-RapidAPI-Key": "8c40f86ee1msh826bcc815c46034p168caajsn97cc615b5a52",
    #     "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
    # }
    headers= {
    'X-RapidAPI-Key': 'b9e1d62e89msh01ceb07d622ba8ap13c7a5jsnc012595cd2f5',
    'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
    }
    # ans_output=[]
    response = requests.get(url, headers=headers, params=querystring).json()
    print(response)
    statusId=response['status']['id']
    if statusId==1 or statusId==2:
        setTimeout(checkstatus(token),2)
        return
    elif statusId==429:
        print("api request overflow")
        return
    else :
        if response['stdout']:
            return [atob(response['stdout']),response['status']['description']]
        else:
            if response['stderr']:
                return [atob(response['stderr']),response['status']['description']]
            else:
                return [atob(response['compile_output']),response['status']['description']]
       



# Example usage

def fn(id,code,ip,ep):
    url = "https://judge0-ce.p.rapidapi.com/submissions"

    querystring = {"base64_encoded":"true","fields":"*"}
    ip=btoa(ip)
    code=btoa(code)
    ep=btoa(ep)
    # ep=btoa(ep)
    # if ip is not None:
    #     if type(ip)==str:
    #         ip=btoa(ip)
    # if code is not None:
    #     if type(code)==str:
    #         code=btoa(code)
    # if id is not None:
    #     if type(id)==str:
    #         id=btoa(id)

        

    payload = {
        "language_id": id,
        "source_code": code,
        "stdin": ip,
        "expected_output":ep



    }
    # headers = {
    #     "content-type": "application/json",
    #     "Content-Type": "application/json",
    #     "X-RapidAPI-Key": "8c40f86ee1msh826bcc815c46034p168caajsn97cc615b5a52",
    #     "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
    # }
    headers= {
        'content-type': 'application/json',
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': 'b9e1d62e89msh01ceb07d622ba8ap13c7a5jsnc012595cd2f5',
        'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
     }
    
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    token=response.json()
    # print(callable(checkstatus))
    # res_ans=[]
    res_ans=checkstatus(token['token'])
    return res_ans

    
    


# @login_required
def index(request):

    obj=codelearn.objects.all()
    context={
        'obj':obj,
    }
    return render(request,'landing.html',context)
def home(request):
    return render(request,'home.html')
def about(request):
    return HttpResponse("this is about")
def service(request):
    return HttpResponse("this is service")
@login_required
def explore(request):
    user=request.user
    username=user.username
    u=user_detail.objects.filter(user_detail_name=username)

    # u_name=u[0].user_detail_name
    # u_pass=u[0].user_detail_password
    # user=authenticate(username=u_name,password=u_pass)
    # return render(request,'explore.html')
    if u.count()!=0 :
        u_pass=u[0].user_detail_password
        user=authenticate(username=username,password=u_pass)
        if user is not None:

            obj=exploreitem.objects.all()
            context={
                "obj":obj,
                # "u":u
            }
            return render(request,'explore.html',context)
        else:
            return render(request,'loginpage.html')
    else:
        return render(request,'loginpage.html',{'username':username})
def discuss(request):
    obj=discussitem.objects.all()
    context={
        "obj":obj
    }
    return render(request,'discuss.html',context)


  



def solve(request,id):
    problem=Cproblem.objects.filter(pk=id)
    testcase=Cupdatetestcase.objects.filter(cproblem=problem[0])
    len=testcase.count()
    id=id
    context={
        "problem":problem,
        "testcase":testcase,
        "len":len,
        "id":id
    }
    print(problem)
    # testcase=problem.input_data
    
    # print(testcase)
    return render(request,'solve.html',context)





# def create_prob(request):
#     if request.method=="POST":
def submit(request,id):
    # return render(request,'codeed.html')
    problem=Cproblem.objects.filter(pk=id)
    testcase=Cupdatetestcase.objects.filter(cproblem=problem[0])
    len=testcase.count()
    id=id
    context={
        "problem":problem,
        "testcase":testcase,
        "len":len,
        "id":id
    }
    return render(request,'editor.html',context)

    # return render(request,'problem.html')
def editor(request):
    return render(request,'editor.html')


    
@csrf_exempt
def compile(request, id):
    if request.method == "POST":
        language = request.POST['language']
        code = request.POST['code']
        input_data = request.POST['input']
        output_data = request.POST['output']
        verdict = ""
        time_taken = ""
        memory_used = ""
        expected_data=""
        final_ans=[]


       

        try:
            if language == 'Cpp':
                try:
                    
                    final_ans = fn(52, code, input_data, expected_data)
                except Exception as e:
                    print(e)
                
            elif language == 'Java':
                try:
                    final_ans = fn(91, code, input_data,expected_data)
                except Exception as e:
                    print(e)
               
            elif language == 'Python':
                try:
                    aa=5
                    final_ans = fn(92, code, input_data,expected_data)
                except Exception as e:
                    print(e)

            # if len(output_data) !=0:  # Check if output_data has been assigned before using it
            #     output_data = output_data[0]
            #     verdict = output_data[1]
                # time_taken = output_data[2]
                # memory_used = output_data[3]

        except Exception as e:
            print("Error:", e)
        # verdict="Accepted"
        context = {
            'code': code,
            'input': input_data,
            'output': final_ans[0],
            'lang': language,
            'id': id,
            'verdict': final_ans[1],
        }

        return render(request, 'editor.html', context)
    else:
        return render(request, 'editor.html')

    
@csrf_exempt
def submit_ans(request,id):
    
    if request.method=="POST":
        problem=Cproblem.objects.filter(pk=id)
        submitestcase=SubmitestCase.objects.filter(cproblem=problem[0])
        title=problem[0].title
        print(title)
        len=submitestcase.count()
        id=id
        language=request.POST['language']
        code=request.POST['code']
        input_testcase=submitestcase[1].submitinput_data
        output_testcase=submitestcase[1].submitexpected_output
        print(input_testcase)
        print(output_testcase)
        final_ans_res=[]
        # verdict="Accepted"
        # context={
        #     "problem":problem,
        #     "testcase":testcase,
        #     "title":title,
        #     "len":len,
        #     "id":id,
        #     'code':code,
        #     'input':input,
        #     'output':output,
        #     'lang':language,
        #     "verdict":verdict,
            
        # }
        # return render(request,'codelearn.html')
        # context={

        # }
        # return render(request,'stat.html',context)
        try:
            if language == 'Cpp':
                try:
                    
                    final_ans_res = fn(52, code, input_testcase, output_testcase)
                except Exception as e:
                    print(e)
                
            elif language == 'Java':
                try:
                    final_ans_res = fn(91, code, input_testcase,output_testcase)
                except Exception as e:
                    print(e)
               
            elif language == 'Python':
                try:
                    aa=5
                    final_ans_res = fn(92, code, input_testcase,output_testcase)
                except Exception as e:
                    print(e)

        except Exception as e:
            print("Error:", e)
        # verdict="Accepted"
        context = {
            'code': code,
            'input': input_testcase,
            'output': final_ans_res[0],
            'lang': language,
            'id': id,
            'verdict': final_ans_res[1],
        }

        return render(request, 'editor.html', context)
    else:
        return render(request, 'editor.html')

        return render(request,'editor.html',context)
    # else:
    
    #     return render(request,'codelearn.html')
    

def stat(request,id):
    problem=Cproblem.objects.filter(pk=id)
    testcase=Cupdatetestcase.objects.filter(cproblem=problem[0])
    title=problem[0].title
    print(title)
    len=testcase.count()
    id=id
    language=request.POST['language']
    code=request.POST['code']
    input=request.POST['input']
    output=request.POST['output']
    verdict="Accepted"
    context={
        "problem":problem,
        "testcase":testcase,
        "title":title,
        "len":len,
        "id":id,
        'code':code,
        'input':input,
        'output':output,
        'lang':language,
        "verdict":verdict,
        
    }
    return render(request,'stat.html',context)


def codelearn_fn(request):
    obj=codelearn.objects.all()
    context={
        'obj':obj,
    }
    return render(request,'codelearn.html',context)

def contest(request):
    today_date=datetime.today()
    print(today_date)
    # obj=Newcontest.objects.all()
    upcoming_contest=Newcontest.objects.filter(ndate__gte=today_date).order_by('-pk')

    past_contest=Newcontest.objects.filter(ndate__lt=today_date).order_by('-pk')
    context={
        'obj1':upcoming_contest,
        'obj2':past_contest
    }
    return render(request,'contest.html',context)


# under review this section
def create_contest(request):
    if request.method=='POST':
        nname=request.POST['contest_name']
        nauthor=request.POST['contest_author']
        date=request.POST['contest_date']
        obj=Newcontest(nname=nname,ndate=date,nauthor=nauthor)
        obj.save()
        context={
            'obj':obj
        }
        return render(request,'shubham_admin.html',context)
    
    
def shubham_admin(request):
    return render(request,'shubham_admin.html')

def addcontestproblem(request):
    if request.method=="POST":
        c_name=request.POST['contest_name']
        p_title=request.POST['problem_title']
        comp=request.POST['complexity']
        constraints=request.POST['constraints']
        code=request.POST['code']
        des=request.POST['des']
        input_data=request.POST['input_data']
        expected_output=request.POST['expected_output']
        newcontest=Newcontest.objects.filter(nname=c_name)
        tag="math"
        cat="nkdcdc"
        diff="Hard"
        obj=Cproblem(newcontest=newcontest[0],title=p_title,description=des,difficulty=diff,categories=cat,compexity=comp,constraints=constraints,pdate=newcontest[0].ndate)
        obj.save()
        lang="C++"
        sol_p=Cupdatesolution(cproblem=obj,language=lang,code=code)
        sol_p.save()
        c_testcase_inp=input_data
        c_testcase_out=expected_output
        p_testcase=Cupdatetestcase(cproblem=obj,input_data=input_data,expected_output=expected_output)
        p_testcase.save()
        newcontest=newcontest[0]
        context={
            'obj':newcontest
        }
        # return render(request,'index.html')
        return render(request,'shubham_admin.html',context)



def dummy_editor(request):
    return render(request,'dummy_editor_statement.html')

# this is for creating contest
def check(request):
    return render(request,'check.html')  

def contestenter(request,id):
    print(-1111)
    newcontest=Newcontest.objects.filter(pk=id)
    newcontest=newcontest[0]   #list ke form me rahega
    cproblem=Cproblem.objects.filter(newcontest=newcontest)   #all problem related to that contest
    context={
        'obj':cproblem
    }
    # print(cproblem[0].title)
    return render(request,'contestproblem.html', context)

# all contest problem will be shown here
def problem(request):
    date=datetime.today()
    obj=Cproblem.objects.filter(pdate__lt=date)
    print(obj.count())
    context={
        "obj":obj,
    }
    return render(request,'problem.html',context)







    
    
        
    
