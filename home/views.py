from django.shortcuts import render
from django.http import HttpResponse
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
        'Dnote': ['3000', 'bi bi-journal'], 
        'Jellyfin': ['8096', 'bi bi-play-fill'], 
        'Jellyseer': ['5055', 'bi bi-binoculars-fill'],
        'Hacktricks': ['3337', 'bi bi-bookmark-fill'],
        'Hacktricks Cloud': ['3377', 'bi bi-cloud-haze-fill'],
        'KASM': ['8141', 'bi bi-pc-display-horizontal'],
        }

    lines = [ "All that is gold does not glitter",
             "Not all those who wander are lost",
             "The old that is strong does not wither",
             "Deep roots are not reached by the frost",
             "From the ashes a fire shall be woken",
             "A light from the shadows shall spring",
             "Renewed shall be made what was once broken",
             "The crownless shall once again be king" ]

    quote = random.choice(lines) 

    return render(request, 'index.html', context={'active_users': active_users,
                                                'all_users': all_users,
                                                'services': services,
                                                'ip_addr': 'svu',
                                                'quote': quote,
                                                })
def render_sign_up(request):
    return render(request, 'sign_up.html' )


