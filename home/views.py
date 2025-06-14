from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import socket 
import random 
import os

# Create your views here.

def index(request):

    active_users = []
    all_users = []

    fortune = os.popen("fortune -s").read()
    uptime = os.popen("uptime -p").read()[3:]
    

    # Active users 
    tmp_users = os.popen("who | awk ' !/tmux/ && !/screen/ {print $1}' | sort | uniq").readlines()
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
        'Stump': ['10801', 'bi bi-book', 'http'],
        }

    for service, items in services.items(): 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc: 
            try:
                soc.connect(('127.0.0.1',int(items[0])))
                items.append('online')
            except socket.error:
                items.append('offline')


    lines = []
    lines_path = os.path.join(settings.BASE_DIR, "home", "static", "text", "affirmations.txt" )
    with open(lines_path, "r") as file:
        for line in file.readlines():
            lines.append(line)


    quote = random.choice(lines) 

    return render(request, 'index.html', context={
        'active_users': active_users,
        'all_users': all_users,
        'services': services,
        'ip_addr': '100.72.58.114',
        'quote': quote,
        'fortune': fortune,
        'uptime': uptime,
    })

def render_sign_up(request):
    return render(request, 'sign_up.html' )

def render_wiki(request, path=None): 

    if path == 'gemini': 
        return render(request, 'articles/gemini.html') 
    if path == 'intro_to_ssh':
        return render(request, 'articles/intro_to_ssh.html') 
    if path == 'why_use_commands':
        return render(request, 'articles/why_use_commands.html') 
    if path == 'in_the_beginning_was_the_commandline':
        return render(request, 'articles/in_the_beginning_was_the_commandline.html') 
    if path == 'intro_to_commands':
        return render(request, 'articles/basics_of_commands.html') 
    else:
        return render(request, 'wiki.html') 

def render_chat(request): 
    return render(request, 'chat.html') 
