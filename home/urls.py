from django.urls import path
from .views import *


urlpatterns = [  
    path('', index, name="index"),
    path('signup', render_sign_up, name="signup"),
]