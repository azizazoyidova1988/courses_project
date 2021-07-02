from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team/', views.team, name="team"),
    path('courses/', views.courses, name="courses"),
    # path('courses/<int:courses_id>/course-details/', views.course_details, name="course_details"),
    path('news/', views.news, name="news"),
    path('contact/', views.contact, name="contact"),
]