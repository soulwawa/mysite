from django.urls import path, re_path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('project/<title>', views.project_detail, name='project-detail'),
    path('dev-notes/', views.dev_notes, name='dev-notes'),
    path('dev-notes/search', views.dev_search, name='dev-search'),
    path('dev-notes/detail/<title>', views.dev_detail, name='dev-detail'),
    path('dev-notes/<tag>/', views.tag_search, name='tag-search'),
    # path('test/', views.test)
]