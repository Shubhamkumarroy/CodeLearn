from django.shortcuts import render,HttpResponse
from .models import student,Tag, TestCase, Category, Solution,codelearn,exploreitem,Myubmission
from .models import discussitem,User_detail,Cadmin,Cproblem,Newcontest,Cdate,Cupdatesolution,Cupdatetestcase,SubmitestCase
from .models import Usercontestsub
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
import time
import pytz
# from fnmatch import fnmatch
from re import template
import re
from datetime import datetime
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date,datetime
from django.db import IntegrityError
from django.utils import timezone

# from .forms import CustomUserCreationForm
# from compilex import compile_code, compile_code_with_input, flush
def accountcreate(request):
    return render (request,'signup.html')

def check_login(request):
        # {% if user.is_authenticated %}  this can be used in frontend
        user=request.user
        # good to know this that fn exist for authentication
        if user.is_authenticated:  
            return True
        else :
            return False
       
    
def signup(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            firstname = request.POST['fname']
            lastname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['password']
            
            # Attempt to create a new user
            myuser = User.objects.create_user(username, email, pass1)
            
            # Create and save user details
            user_db = User_detail(user_detail_name=username, user_detail_email=email, user_detail_password=pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            user_db.save()
            
            # Authenticate the user
            user = authenticate(username=username, password=pass1)
            user_status = 1
            user_d = request.user
            obj = codelearn.objects.all()
            context = {
                'obj': obj,
                "user_d": user_d,
                "user_status": user_status
            }
            
            if user is not None:
                # If authentication is successful, log the user in and render a page
                login(request, user)
                id1 = user.id
                return render(request, 'codelearn.html', context)
            else:
                # If authentication fails, render the login page
                return render(request, 'loginpage.html')
        except IntegrityError:
            error_message = "Username or email already taken. Please choose a different username or email."
            return render(request, 'signup.html', {'error_message': error_message})
        except Exception as e:
            # Handle other exceptions by displaying an error page or message
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})
    else:
        return render(request, 'signup.html')
    

def loginuser(request):
    if request.method == "POST":
        try:
            user_d = request.user
            username = request.POST['username']
            pass1 = request.POST['password']
            
            user = authenticate(username=username, password=pass1)
            
            if user is not None:
                login(request, user)
                id1 = user.id
                user_status = 1
                obj = codelearn.objects.all()
                context = {
                    'obj': obj,
                    'user_d': user_d,
                    'user_status': user_status
                }
                return render(request, 'codelearn.html', context)
            else:
                error_message = "Invalid username or password."
                return render(request, 'loginpage.html', {'error_message': error_message})
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error_page.html', {'error_message': error_message})
    else:
        return render(request, 'loginpage.html')


def logoutuser(request):
    try:
        logout(request)
    except Exception as e:
        # Handle exceptions by displaying an error page or message
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})
    
    return render(request, 'loginpage.html')




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

 
@csrf_exempt
def checkstatus(token):
    try:
        print(token)
        url = f"https://judge0-ce.p.rapidapi.com/submissions/{token}"

        querystring = {"base64_encoded": "true", "fields": "*"}

        # headers = {
        #     "X-RapidAPI-Key": "8c40f86ee1msh826bcc815c46034p168caajsn97cc615b5a52",
        #     "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
        # }
        headers= {
        'X-RapidAPI-Key': 'b9e1d62e89msh01ceb07d622ba8ap13c7a5jsnc012595cd2f5',
        'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
        }

        response_data = requests.get(url, headers=headers, params=querystring).json()
        print(response_data)
        status_object = response_data.get("status", {})
        status_id = status_object.get("id", None)
        status_description = status_object.get("description", "")

        if status_id == 1 or status_id == 2:
            time.sleep(2)
            return checkstatus(token)
        elif status_id == 429:
            return {"error": "API request overflow"}
        else:
            timetaken = response_data.get("time", "")
            memorytaken = response_data.get("memory", "")
            if response_data['stdout']:
                encoded_stdout = response_data.get("stdout", "")
                decoded_stdout = base64.b64decode(encoded_stdout).decode("utf-8")
                result_dict = {
                "status_id": status_id,
                "status_description": status_description,
                "stdoutput": decoded_stdout,
                "timetaken": timetaken,
                "memorytaken": memorytaken
            }              
            else:
                if response_data['stderr']:
                    result_dict = {
                    "status_id": status_id,
                    "status_description": status_description,
                    "stdoutput": status_description,
                    "timetaken": timetaken,
                    "memorytaken": memorytaken
                    }
                elif response_data['compile_output'] :
                    encoded_stdout = response_data.get("compile_output", "")
                    decoded_stdout = base64.b64decode(encoded_stdout).decode("utf-8")
                    result_dict = {
                    "status_id": status_id,
                    "status_description": status_description,
                    "stdoutput": decoded_stdout,
                    "timetaken": timetaken,
                    "memorytaken": memorytaken
                    }     
                else :
                    result_dict = {
                    "status_id": status_id,
                    "status_description": status_description,
                    "stdoutput": "Time Limit Exceeded",
                    "timetaken": timetaken,
                    "memorytaken": memorytaken
                    }     

            return result_dict

    except requests.RequestException as req_err:
        return {"error": f"Request Exception: {str(req_err)}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
       
# Example usage

def caloutput(id, code, ip, ep):
    try:
        url = "https://judge0-ce.p.rapidapi.com/submissions"

        querystring = {"base64_encoded": "true", "fields": "*"}
        ip = btoa(ip)
        code = btoa(code)
        ep = btoa(ep)
        payload = {
            "language_id": id,
            "source_code": code,
            "stdin": ip,
            "expected_output": ep
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
        dataj = response.json()
        print(dataj)
        print(dataj['token'])
        intermediates = checkstatus(dataj['token'])
        return intermediates
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return {"error": error_message}

  

    
@csrf_exempt  
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

def explore(request):
    if check_login(request):
        obj=exploreitem.objects.all()
        context={
            "obj":obj,
        }
        return render(request,'explore.html',context)
    else:
        return render(request,'loginpage.html')

@csrf_exempt 
def adddiscuss(request):
    return render(request,'adddiscuss.html')
@csrf_exempt
def discuss(request):
    if check_login(request):
        if request.method=="POST":
            title=request.POST['title']
            description=request.POST['description']
            obj=discussitem(title=title,description=description)
            obj.save()

        obj=discussitem.objects.all().order_by('-timestamp')
        context={
            "obj":obj
        }
        return render(request,'discuss.html',context)
    else:
        return redirect('/loginuser')


@csrf_exempt
def solve(request, id, param1):
    try:
        if check_login(request):
            print(param1)
            problem = Cproblem.objects.filter(pk=id)
            testcase = Cupdatetestcase.objects.filter(cproblem=problem[0])
            soln = Cupdatesolution.objects.filter(cproblem=problem[0])
            contestid = problem[0].newcontest.id
            total_count = testcase.count()
            id = id
            context = {
                "problem": problem,
                "testcase": testcase[0],
                "ip1": testcase[0].input_data,
                "op1": testcase[0].expected_output,
                "total_count": total_count,
                "soln": soln[0].code,
                "id": id,
                "contestid": contestid,
                "param1": param1,
            }
            return render(request, 'solve.html', context)
        else:
            return redirect('/loginuser')
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})



@csrf_exempt
def submit(request,id,param1):
    problem=Cproblem.objects.filter(pk=id)
    testcase=Cupdatetestcase.objects.filter(cproblem=problem[0])
    total_count=testcase.count()
    context={
        "problem":problem,
        "input":testcase[0].input_data,
        "total_count":total_count,
        "id":id,
        "param1":param1
    }
    return render(request,'editor.html',context)

def editor(request):
    return render(request,'editor.html')


    

@csrf_exempt
def compile(request, id):
    try:
        if request.method == "POST":
            language = request.POST['language']
            code = request.POST['code']
            input_data = request.POST['input']
            output_data = request.POST['output']
            verdict = ""
            time_taken = ""
            memory_used = ""
            expected_data = ""

            context = {
                'code': code,
                'input': input_data,
                'language': language,
                'id': id,
                'output': "",
                'verdict': "",
                'timetaken': "",
                'memorytaken': ""
            }
            context['timeofsub'] = datetime.now().time()

            if language == 'Cpp':
                final_ans1 = caloutput(52, code, input_data, expected_data)
                context['output'] = final_ans1["stdoutput"]
                context['verdict'] = final_ans1["status_description"]
                context['timetaken'] = final_ans1["timetaken"]
                context['memorytaken'] = final_ans1["memorytaken"]
            elif language == 'Java':
                final_ans2 = caloutput(91, code, input_data, expected_data)
                context['output'] = final_ans2["stdoutput"]
                context['verdict'] = final_ans2["status_description"]
                context['timetaken'] = final_ans2["timetaken"]
                context['memorytaken'] = final_ans2["memorytaken"]

            elif language == 'Python':
                final_ans3 = caloutput(92, code, input_data, expected_data)
                context['output'] = final_ans3["stdoutput"]
                context['verdict'] = final_ans3["status_description"]
                context['timetaken'] = final_ans3["timetaken"]
                context['memorytaken'] = final_ans3["memorytaken"]

            return render(request, 'editor.html', context)
        else:
            return render(request, 'editor.html')

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})


    
# @csrf_exempt
def submit_ans(request, id , param1):

    try:
        if request.method == "POST":
            problem = Cproblem.objects.filter(pk=id)
            user = request.user
            username = user.username
            print(username)
            user_detail = User_detail.objects.filter(user_detail_name=username)
            print(user_detail)
            conname = problem[0].newcontest
            # print(conname)
            submitestcase = SubmitestCase.objects.filter(cproblem=problem[0])
            title = problem[0].title
            total_count = submitestcase.count()
            id = id
            language = request.POST['language']
            code = request.POST['code']
            input_testcase = ""
            output_testcase = ""
            
            if submitestcase.count() != 0:
                input_testcase = submitestcase[0].submitinput_data
                output_testcase = submitestcase[0].submitexpected_output

            context = {
                'code': code,
                'input_testcase': input_testcase,
                'output_testcase': output_testcase,
                'language': language,
                'id': id,
                'output': "",
                'verdict': "",
                'timetaken': "",
                'memorytaken': "",
                'param1': param1,
                'contestid':conname.id
            }
            utc_time = datetime.utcnow()

            utc_timezone = pytz.timezone('UTC')
            ist_timezone = pytz.timezone('Asia/Kolkata')  # 'Asia/Kolkata' is the time zone for IST
            ist_time = utc_time.replace(tzinfo=utc_timezone).astimezone(ist_timezone)         
            context['timeofsub'] = ist_time
            context['title'] = title
            context['username'] = username

            if language == 'Cpp':
                final_ans1 = caloutput(52, code, input_testcase, output_testcase)
                context['output'] = final_ans1["stdoutput"]
                context['verdict'] = final_ans1["status_description"]
                context['timetaken'] = final_ans1["timetaken"]
                context['memorytaken'] = final_ans1["memorytaken"]
            elif language == 'Java':
                final_ans2 = caloutput(91, code, input_testcase, output_testcase)
                context['output'] = final_ans2["stdoutput"]
                context['verdict'] = final_ans2["status_description"]
                context['timetaken'] = final_ans2["timetaken"]
                context['memorytaken'] = final_ans2["memorytaken"]

            elif language == 'Python':
                final_ans3 = caloutput(92, code, input_testcase, output_testcase)
                context['output'] = final_ans3["stdoutput"]
                context['verdict'] = final_ans3["status_description"]
                context['timetaken'] = final_ans3["timetaken"]
                context['memorytaken'] = final_ans3["memorytaken"]
            
            mysub = Myubmission(user_detail=user_detail[0], cproblem=problem[0], code=code, language=language,timetaken=context['timetaken'], memorytaken=context['memorytaken'],verdict=context['verdict'], output=context['output'])
            
            usesub = Usercontestsub(user_detail=user_detail[0], newcontest=conname, cproblem=problem[0], code=code,language=language, timetaken=context['timetaken'], memorytaken=context['memorytaken'],verdict=context['verdict'], output=context['output'])
            
            mysub.save()
            usesub.save()
            return render(request, 'stat.html', context)
        
        else:
            return render(request, 'editor.html')

    except Exception as e:
        # Handle exceptions by displaying an error page or message
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

    
    
@csrf_exempt
def stat(request, id):
    try:
        problem = Cproblem.objects.filter(pk=id)
        testcase = Cupdatetestcase.objects.filter(cproblem=problem[0])
        title = problem[0].title
        print(title)
        total_count = testcase.count()
        id = id
        language = request.POST['language']
        code = request.POST['code']
        input_data = request.POST['input']
        output_data = request.POST['output']
        verdict = "Accepted"
        
        context = {
            "problem": problem,
            "testcase": testcase,
            "title": title,
            "total_count": total_count,
            "id": id,
            'code': code,
            'input': input_data,
            'output': output_data,
            'lang': language,
            "verdict": verdict,
        }
        return render(request, 'stat.html', context)
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

@csrf_exempt
def codelearn_fn(request):
    obj=codelearn.objects.all()
    context={
        'obj':obj,
    }
    if check_login(request):
        return render(request,'codelearn.html',context)
    else:
        return render(request,'landing.html',context)

@csrf_exempt
def contest(request):
    if check_login(request):

        today_date=datetime.today()
        # obj=Newcontest.objects.all()
        upcoming_contest=Newcontest.objects.filter(ndate__gte=today_date).order_by('-pk')

        past_contest=Newcontest.objects.filter(ndate__lt=today_date).order_by('-pk')
        context={
            'obj1':upcoming_contest,
            'obj2':past_contest
        }
        return render(request,'contest.html',context)
    else:
        return redirect('/loginuser')


# under review this section
@csrf_exempt
def create_contest(request):
    try:
        if request.method == 'POST':
            nname = request.POST['contest_name']
            nauthor = request.POST['contest_author']
            date = request.POST['contest_date']
            obj = Newcontest(nname=nname, ndate=date, nauthor=nauthor)
            obj.save()
            context = {'obj': obj}
            return render(request, 'shubham_admin.html', context)
        else:
            return render(request, 'create_contest.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

    
@csrf_exempt   
def shubham_admin(request):
    return render(request,'shubham_admin.html')

@csrf_exempt
def addcontestproblem(request):
    try:
        if request.method == "POST":
            c_name = request.POST['contest_name']
            p_title = request.POST['problem_title']
            comp = request.POST['complexity']
            constraints = request.POST['constraints']
            code = request.POST['code']
            des = request.POST['des']
            input_data = request.POST['input_data']
            expected_output = request.POST['expected_output']
            final_input = request.POST['final_input']
            final_output = request.POST['final_output']
            tag = request.POST['Tag']
            diff = request.POST['Difficulty']
            
            newcontest = Newcontest.objects.filter(nname=c_name)
            
            if newcontest.exists():
                newcontest = newcontest[0]
                cat = "C++"
                obj = Cproblem(
                    newcontest=newcontest, title=p_title, tags=tag, description=des, difficulty=diff,
                    categories=cat, compexity=comp, constraints=constraints, pdate=newcontest.ndate
                )
                obj.save()
                
                lang = "C++"
                sol_p = Cupdatesolution(cproblem=obj, language=lang, code=code)
                sol_p.save()
                
                p_testcase = Cupdatetestcase(cproblem=obj, input_data=input_data, expected_output=expected_output)
                p_testcase.save()
                
                s_testcase = SubmitestCase(cproblem=obj, submitinput_data=final_input, submitexpected_output=final_output)
                s_testcase.save()
                
                context = {'obj': newcontest}
                return render(request, 'shubham_admin.html', context)
            
            else:
                error_message = "Contest not found."
                return render(request, 'error_page.html', {'error_message': error_message})
        else:
            return render(request, 'shubham_admin.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})


@csrf_exempt
def dummy_editor(request):
    return render(request,'dummy_editor_statement.html')

@csrf_exempt
def check(request):
    return render(request,'check.html')  

@csrf_exempt
def contestenter(request, id):
    try:
        if check_login(request):
            newcontest = Newcontest.objects.filter(pk=id)
            if newcontest.exists():
                newcontest = newcontest[0]  
                cproblem = Cproblem.objects.filter(newcontest=newcontest) 
                
                context = {
                    'obj': cproblem,
                    'id': id,
                    'contestid': newcontest.id
                }
                
                return render(request, 'contestproblem.html', context)
            
            else:
                error_message = "Contest not found."
                return render(request, 'error_page.html', {'error_message': error_message})
            
        else:
            return redirect('/loginuser')
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

# all contest problem will be shown here
@csrf_exempt
def problem(request):
    try:
        if check_login(request):
            date = datetime.today()
            obj = Cproblem.objects.filter(pdate__lt=date)
            print(obj.count())
            context = {
                "obj": obj,
            }
            return render(request, 'problem.html', context)
        else:
            return redirect('/loginuser')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

def usersubmission(request, param1):
    try:
        if check_login(request):
            user = request.user
            username = user.username
            print(username)
            
            user_detail = User_detail.objects.filter(user_detail_name=username)
            
            if user_detail.exists():
                user_detail = user_detail[0]
                usersub = Myubmission.objects.filter(user_detail=user_detail)
                
                context = {
                    'usersub': usersub,
                    "param1": param1
                }
                
                return render(request, 'usersuball.html', context)
            
            else:
                error_message = "User detail not found."
                return render(request, 'error_page.html', {'error_message': error_message})
        
        else:
            return redirect('/loginuser')
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

    
        

def contestusersubmission(request, id, param1):
    try:
        if check_login(request):
            user = request.user
            username = user.username
            print(username)
            
            user_detail = User_detail.objects.filter(user_detail_name=username)
            
            if user_detail.exists():
                user_detail = user_detail[0]
                coname = Newcontest.objects.filter(pk=id)
                
                if coname.exists():
                    coname = coname[0]
                    usersub = Usercontestsub.objects.filter(newcontest=coname, user_detail=user_detail)
                    
                    context = {
                        'usersub': usersub,
                        'param1': param1,
                        'contestid': id
                    }
                    
                    return render(request, 'usersuball.html', context)
                
                else:
                    error_message = "Contest not found."
                    return render(request, 'error_page.html', {'error_message': error_message})
            
            else:
                error_message = "User detail not found."
                return render(request, 'error_page.html', {'error_message': error_message})
        
        else:
            return redirect('/loginuser')
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

    

    
    
# def usercontestsubmission
# def usercontestsub(re)


    








    
    
        
    
