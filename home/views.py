from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):

    active_users = []
    all_users = []

    # Active users 
    tmp_users = os.popen("last -w | grep logged | awk '{print $1}'").readlines()
    [ active_users.append(user.strip('\n')) for user in tmp_users if user.strip('\n') not in active_users ]

    # All users 
    tmp_users = os.popen('ls /home').readlines()
    all_users = [ user.strip('\n') for user in tmp_users ]

    # Running services 
    services = {
        'Dnote':'3000', 'Jellyfin':'8096', 'Jellyseer':'5055',
        'Hacktricks':'3337', 'Hacktricks Cloud':'3377', 'KASM':'8141',
        }

    return render(request, 'index.html', context={'active_users': active_users,
                                                'all_users': all_users,
                                                'services': services,
                                                'ip_addr': '127.0.0.1'})

def render_sign_up(request):
    return render(request, 'sign_up.html' )


