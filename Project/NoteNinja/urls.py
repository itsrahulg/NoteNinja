from django.urls import path
from . import views
urlpatterns = [

    path('',views.homepage),
    path('view-notes',views.viewnotes,name="view-notes")
]