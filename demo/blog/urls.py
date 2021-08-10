from django.urls import path
from .views import listed_post
urlpatterns = [
    path('',listed_post,name ="home"),
]