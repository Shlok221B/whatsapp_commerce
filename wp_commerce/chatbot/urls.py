from django.urls import path
from chatbot import views


urlpatterns = [
        path('webhook',views.webhook,name="webhook" ),
                                                            #Request will be send to webhook function in views.py    
]