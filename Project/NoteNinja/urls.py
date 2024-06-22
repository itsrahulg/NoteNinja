from django.urls import path
from . import views
urlpatterns = [

    path('',views.homepage,name=""),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('createnote',views.createnote,name="createnote"),
    path('viewnotes',views.viewnotes,name="view-notes"),
    path('updatenotes/<str:pk>',views.updatenote,name="updatenote"),
    path('deletenote/<str:pk>',views.deletenote,name="deletenote"),
]