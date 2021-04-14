from django.urls import path
from . import views

urlpatterns =[
    path('',views.homepageofwebsite,name="homepageofwebsite"),
    path('registerrequest',views.ajaxregisterrequest,name="ajaxregisterrequest"),
    path('loginrequest',views.ajaxloginrequest,name="ajaxloginrequest"),
    path('gh',views.homepageform,name="homepageform"),
    path('abc',views.ajaxform,name="ajaxform"),
    path('abcd',views.showcontent,name="showcontent"),
    path('edit',views.edit,name="edit"),
    path('delete',views.delete,name="delete"),
    path('usersideform',views.usersideform,name="usersideform"),
    path('ajaxresponse',views.ajaxresponse,name="ajaxresponse"),
    path('showresponse',views.showresponse,name="showresponse"),
    path('sendmail',views.sendmail,name="sendmail"),
    path('loginformforsurveybuilder',views.loginformforsurveybuilder,name="loginformforsurveybuilder"),
    path('Registerforsurveybuilder',views.Registerforsurveybuilder,name="Registerforsurveybuilder")
]