from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('devlog/', views.devlog, name='devlog'),
    path('devlog/search', views.dev_search, name='dev-search'),
    path('devlog/<tag>/', views.tag_search, name='tag-search')
]