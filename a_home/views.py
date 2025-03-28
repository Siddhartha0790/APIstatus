from django.shortcuts import render,redirect
import requests
from .models import myAPI
def home_view(request):
    
    allurls = myAPI.objects.all()
    print(allurls)
    return render(request, 'home.html', {'allurls': allurls})


def createapi(request):
    if request.method == 'POST':
        api_url = request.POST.get('api')
        content = request.POST.get('text')
        
        newapi = myAPI()
        newapi.apiurl = api_url
        newapi.post_data = content
        newapi.save()
       
        return redirect('home')
    return render(request, 'a_home/create.html')

def api_view(request,api):
    api_url = api
    response = requests.get(api_url)