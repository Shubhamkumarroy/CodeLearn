from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("",views.index,name='index'),
    path("home",views.home,name='home'),
    path("about",views.about,name='about'),
    path("explore",views.explore,name='explore'),
    path("problem",views.problem,name='problem'),
    path("contest",views.contest,name='contest'),
    path("adddiscuss",views.adddiscuss,name='adddiscuss'),
    path("discuss",views.discuss,name='discuss'),
    path("solve/<int:id>/<str:param1>",views.solve,name='solve'),
    path("submit/<int:id>/<str:param1>",views.submit,name='submit'),
    path("submit_ans/<int:id>/<str:param1>",views.submit_ans,name='submit_ans'),
    # path("editor",views.editor,name='editor'),
    path("compile/<int:id>",views.compile,name='compile'),
    path("stat/<int:id>",views.stat,name='stat'),
    path("codelearn_fn",views.codelearn_fn,name='codelearn_fn'),
    path("signup/",views.signup,name="signup"),
    path('loginuser/', views.loginuser, name ='loginuser'),
    path('logoutuser/', views.logoutuser, name ='logoutuser'),
    path('accountcreate/',views.accountcreate,name='accountcreate'),
    path('shubham_admin/',views.shubham_admin,name='shubham_admin'),
    path('dummy_editor/',views.dummy_editor,name='dummy_editor'),
    path('create_contest/',views.create_contest,name='create_contest'),
    path('check/',views.check,name='check'),
    path('addcontestproblem/',views.addcontestproblem,name='addcontestproblem'),
    path('contestenter/<int:id>',views.contestenter,name='contestenter'),
    path('usersubmission/<str:param1>',views.usersubmission,name='usersubmission'),
    path('contestusersubmission/<int:id>/<str:param1>',views.contestusersubmission,name='contestusersubmission'),
    path('othersubmission/<str:param1>',views.othersubmission,name='othersubmission'),
    
    
    # path('contest',views.contest,name='contest'),
   

    
]