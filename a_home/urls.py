from django.urls import path
from a_home.views import *

urlpatterns = [
    path('', home_view, name="home"),  
    path('create/', createapi, name="create"), 
    path('detail/<int:pk>/', apidetail, name="detail"), 
 
]
