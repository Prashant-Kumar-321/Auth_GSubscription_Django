from django.shortcuts import render
from django.http import HttpResponse

from a_user_authentication.utilities.extracting_github_user_info import get_user_data 

def home(request): 
    # try: 
    #     get_user_data(request.user)
    # except: 
    #     pass
    return render(request, 'a_user_authentication/index.html')

def dashboard(request): 
    return render(request, 'a_user_authentication/dashboard.html')