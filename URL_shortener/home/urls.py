from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_form', views.index_form, name='index_form'),
]
