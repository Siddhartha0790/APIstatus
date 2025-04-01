from celery import shared_task
from .models import myAPI
import requests


@shared_task
def check_status(id):
   print('function runningg')
   api = myAPI.objects.get(id=id)
 
    
  
   response = requests.get(api.apiurl)
   print(response.status_code)
   if(response.status_code == 200):
      api.status = True
      api.save()
   else:
      api.status = False
      api.save()
            

@shared_task
def check_status_for_all_users():
    allapi = myAPI.objects.all()
    for api1 in allapi:
        check_status.delay(api1.id)  # Correctly pass user ID
    return "Scheduled status checks for all users"