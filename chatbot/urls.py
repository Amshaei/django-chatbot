from django.urls import path
from . import views


# Creating Endpoints
urlpatterns = [
    path('', views.chatbot, name='chatbot')
]