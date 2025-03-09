from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.


def index(request):
    # active_users = os.popen('users').read()
    # active_users_list = []
    # for active_user in active_users.strip().split():
    #     if active_user not in active_users_list:
    #         active_users_list.append(active_user)

    # all_users = os.popen('cat /etc/passwd').read()
    # all_users_list = []
    # for user in all_users.strip().split('\n'):
    #         if ('/home/' and ':/bin/bash') in user:
    #                 if 'root' not in user:
    #                         all_users_list.append(user.split(":")[0])

    services = {'Dnote':'3000', 'Jellyfin':'8096', 'Jellyseer':'5055',
            'Hacktricks':'3337', 'Hacktricks Cloud':'3377', 'KASM (Dynamic workspaces)':'8141',
            'service7':'port7', 'service8':'port8', 'service9':'port9'}


    # get_ip = os.popen("ip addr | grep 'inet 100'").read()
    # ip_address = get_ip.strip().split()[1].split('/')[0]

    # return render(request, 'index.html', context={'active_users': active_users_list,
    #                                             'all_users': all_users_list,
    #                                             'services': services,
    #                                             'ip_addr': ip_address})

    # uncomment above lines and replace and remove below lines in this function.

    ip_addr = '192.168.0.102'
    return render(request, 'index.html', context={'active_users': [chr(i) for i in range(65, 91)], 
                                                  'all_users': ['deathstar107', 'SaiDen', 'Duckdarsh', 'Kabutozect', 'sgtstringplucker', 'niffler'], 
                                                  'services': services,
                                                  'ip_addr': ip_addr})  


   

def render_sign_up(request):
    return render(request, 'sign_up.html' )


