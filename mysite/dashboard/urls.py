from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('commenter/list/', views.commenter_list, name="commenter_list"),
    path('commenter/add/', views.commenter_create, name="commenter_add"),
    path('commenter/<int:commenter_id>/edit/', views.commenter_edit, name="commenter_edit"),
    path('commenter/<int:commenter_id>/delete/', views.commenter_delete, name="commenter_delete"),

    path('course/list/', views.courses_list, name="courses_list"),
    path('course/add/', views.courses_create, name="courses_add"),
    path('course/<int:courses_id>/edit/', views.courses_edit, name="courses_edit"),
    path('course/<int:courses_id>/delete/', views.courses_delete,name="courses_delete"),

    path('news/list/', views.news_list, name="news_list"),
    path('news/add/', views.news_create, name="news_add"),
    path('news/<int:news_id>/edit/', views.news_edit, name="news_edit"),
    path('news/<int:news_id>/delete/', views.news_delete, name="news_delete"),

    path('team/list/', views.teams_list, name="teams_list"),
    path('team/add/', views.teams_create, name="teams_add"),
    path('team/<int:teams_id>/edit/', views.teams_edit, name="teams_edit"),
    path('team/<int:teams_id>/delete/', views.teams_delete, name="teams_delete"),

    path('items/list/', views.items_list, name="items_list"),
    path('items/add/', views.items_create, name="items_add"),
    path('items/<int:item_id>/edit/', views.items_edit, name="items_edit"),
    path('items/<int:item_id>/delete/', views.items_delete, name="items_delete"),

    path('video/list/', views.video_list, name="video_list"),
    path('video/add/', views.video_create, name="videos_add"),
    path('video/<int:video_id>/edit/', views.video_edit, name="video_edit"),
    path('video/<int:video_id>/delete/', views.video_delete, name="video_delete"),
   ]