from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team/', views.team, name="team"),
    path('courses/', views.courses, name="courses"),
    path('news/', views.news, name="news"),
    path('news/<int:news_id>/new/', views.new_single, name="new_single"),
    path('video/<int:pk>/<int:pks>', views.video, name="video"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/',include('dashboard.urls'))
]