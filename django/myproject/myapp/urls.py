from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index')  # '' = root URL, index.name = rendering an HTML. HTTP response,JSON response
   #  path('/download',views.index,name='index')
]