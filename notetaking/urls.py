from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.hello),
    path('create-note/<str:tag>/<str:title>/<str:content>/', views.createNote),
    path('get-list/', views.getList),
]
