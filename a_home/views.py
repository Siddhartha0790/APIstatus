from django.shortcuts import render,redirect
import requests
from .models import myAPI
import json
def home_view(request):
    
    allurls = myAPI.objects.filter(owner = request.user)

    return render(request, 'home.html', {'allurls': allurls})


def createapi(request):
    if request.method == 'POST':
        api_url = request.POST.get('api')
        content = request.POST.get('text')
        
        newapi = myAPI()
        newapi.apiurl = api_url
        newapi.post_data = content
        newapi.owner = request.user
        newapi.save()
       
        return redirect('home')
    return render(request, 'a_home/create.html')

def api_view(request,api):
    api_url = api
    response = requests.get(api_url)
    
    
def apidetail(request,pk):
    
    myurl = myAPI.objects.get(id=pk)
    response = requests.get(myurl.apiurl).json()
    formatted_json = json.dumps(response, indent=2)
    if(response is None):
        formatted_json = ""
    return render(request , 'a_home/apidetail.html' , {'myurl' : myurl , 'response' : formatted_json })