from django.urls import path
from blog import views


app_name = 'project'

urlpatterns = [
    path('', views.about, name='project'),
]
