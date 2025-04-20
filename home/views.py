from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import random 
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
        'Dnote': ['3000', 'bi bi-journal', 'http'], 
        'Jellyfin': ['8096', 'bi bi-play-fill', 'http'], 
        'Jellyseer': ['5055', 'bi bi-binoculars-fill', 'http'],
        'Hacktricks': ['3337', 'bi bi-bookmark-fill', 'http'],
        'Hacktricks Cloud': ['3377', 'bi bi-cloud-haze-fill', 'http'],
        'KASM': ['8141', 'bi bi-pc-display-horizontal', 'https'],
        }

    lines = []
    lines_path = os.path.join(settings.BASE_DIR, "home", "static", "text", "affirmations.txt" )
    with open(lines_path, "r") as file:
        for line in file.readlines():
            lines.append(line)


    quote = random.choice(lines) 

    return render(request, 'index.html', context={'active_users': active_users,
                                                'all_users': all_users,
                                                'services': services,
                                                'ip_addr': '100.72.58.114',
                                                'quote': quote,
                                                })
def render_sign_up(request):
    return render(request, 'sign_up.html' )

def render_wiki(request, path): 

    if path == 'gemini': 
        return render(request, 'articles/gemini.html') 
    else:
        return render(request, 'wiki.html') 


