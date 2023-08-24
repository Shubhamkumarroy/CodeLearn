from django.contrib import admin

# Register your models here.
from .models import student,Problem, Tag, TestCase, Category, Solution,codelearn,discussitem,exploreitem
from .models import Cdate,user_detail,Cadmin,Cproblem,Csolution,CtestCase,Newcontest,Cupdatesolution,Cupdatetestcase,SubmitestCase
admin.site.register(student)
admin.site.register(Problem)
admin.site.register(Tag)
admin.site.register(TestCase)
admin.site.register(Category)
admin.site.register(Solution)
admin.site.register(codelearn)
admin.site.register(discussitem)
admin.site.register(exploreitem)
admin.site.register(user_detail)
admin.site.register(Cadmin)
admin.site.register(CtestCase)
admin.site.register(Cproblem)
admin.site.register(Csolution)
admin.site.register(Newcontest)
admin.site.register(Cdate)
admin.site.register(Cupdatetestcase)
admin.site.register(Cupdatesolution)
admin.site.register(SubmitestCase)
