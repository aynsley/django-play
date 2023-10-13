from django.urls import path
from . import views

app_name = 'blog'

# The home page does not need to be in portfolio, specifically. It could be any app

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]