from django.urls import path
from blog import views
from blog.views import BlogIndex

app_name = 'blog'

urlpatterns = [
    path('', BlogIndex.as_view(), name='blog'),
    # path('blog/dev-notes/', views.dev_notes, name='dev-notes'),
    path('blog/dev-notes/search', views.dev_search, name='dev-search'),
    path('blog/dev-notes/detail/<title>', views.dev_detail, name='dev-detail'),
    path('blog/dev-notes/<tag>/', views.tag_search, name='tag-search'),
    # path('test/', views.test)
]