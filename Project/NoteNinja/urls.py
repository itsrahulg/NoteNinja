from django.urls import path
from . import views
urlpatterns = [

    path('',views.homepage),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('createnote',views.createnote,name="creatnote"),
    path('viewnotes',views.viewnotes,name="view-notes"),
    path('updatenotes',views.updatenote,name="updatenote"),
    path('deletenote',views.deletenote,name="deletenote")
]