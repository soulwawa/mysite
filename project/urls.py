from django.urls import path
from project.views import ProjectView

from blog import views


app_name = 'project'

urlpatterns = [
    path('', ProjectView.as_view(), name='project'),
]
