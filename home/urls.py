from django.urls import path, re_path
from .views import *


urlpatterns = [  
    path('', index, name="index"),
    path('signup', render_sign_up, name="signup"),
    path('chat', render_chat, name="chat"),
    re_path(r'wiki(?:/(?P<path>.*))?$', render_wiki, name="wiki"),
]
