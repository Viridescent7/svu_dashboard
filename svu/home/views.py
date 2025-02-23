from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.


def index(request):
    # active_users = os.popen('users').read()
    # active_users_list = []
    # for active_user in active_users.strip().split('\n'):
    #         active_users_list.append(active_user)

    # all_users = os.popen('cat /etc/passwd').read()
    # all_users_list = []
    # for user in all_users.strip().split('\n'):
    #         if ('/home/' and ':/bin/bash') in user:
    #                 if 'root' not in user:
    #                         all_users_list.append(user.split(":")[0])

    services = {'service1':'port1', 'service2':'port2', 'service3':'port3', 
                'service4':'port4', 'service5':'port5', 'service6':'port6',
                'service7':'port7', 'service8':'port8', 'service9':'port9'}
    ip_addr = '1.2.3.4' #os.popen().read

    return render(request, 'index.html', context={'active_users': [chr(i) for i in range(65, 91)], 
                                                  'all_users': ['deathstar107', 'SaiDen', 'Duckdarsh', 'Kabutozect', 'sgtstringplucker', 'viridescent'], 
                                                  'services': services,
                                                  'ip_addr': ip_addr})  


    #uncomment above lines and replace [chr(i) for i in range(65, 91)] with active_users_list 
    #                              and [] with all_user_list

    

def render_sign_up(request):
    return render(request, 'sign_up.html' )


