from django.shortcuts import render, redirect
from .services import *
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage


# from .editor import *


def home(request):
    email = Subscribe()
    form = SubscribeForm(request.POST, instance=email)
    if request.POST:
        if form.is_valid():
            email.save()
            return redirect('home')
        else:
            print(form.errors)

    items = get_items()
    news = get_news()
    courses = get_courses()
    teams = get_teams()
    ctx = {
        "items": items,
        "news": news,
        "courses": courses,
        "teams": teams,
        'home_page': 'active',
        'form_email': form

    }

    return render(request, 'store/index.html', ctx)


def team(request):
    teams = get_teams()
    ctx = {
        'teams': teams,
        'team_page': 'active'
    }
    return render(request, 'store/team.html', ctx)


def courses(request):
    courses = get_courses()
    p = Paginator(courses, 3)
    page_num = request.GET.get('page', 1)
    total_pages = len(courses)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    ctx = {
        'courses': courses,
        'course_page': 'active',
        'page': page,
        'page_num': page_num,
        'total_pages': total_pages
    }
    return render(request, 'store/courses.html', ctx)


def news(request):
    news = get_news()
    p = Paginator(news, 3)
    page_num = request.GET.get('page', 1)
    total_pages = len(news)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    ctx = {
        'news': news,
        'news_page': 'active',
        'page': page,
        'page_num': page_num,
        'total_pages': total_pages
    }
    return render(request, 'store/news.html', ctx)


def new_single(request, news_id):
    news = get_news()
    new = get_news_by_id(news_id=news_id)
    ctx = {
        'news': news,
        'new': new
    }
    return render(request, 'store/new.html', ctx)


# def video(request, course_id):
#     course = get_course_by_id(course_id=course_id)
#     model=Video()
#     form = VideoForm(request.POST or None, instance=model)
#     if request.method == 'GET':
#         if form.is_valid():
#             form.save()
#     ctx = {
#         'course': course,
#         'video': video,
#         'form': form
#     }
#     return render(request, 'store/video.html', ctx)


def video(request, pk, pks=2):
    user = None
    name = "Tom"
    courses = get_course_by_id(pk)
    cour_id = courses[0]['id']
    comments = get_commenter(pk, pks)
    videos = get_video_by_course_id(pk)
    model = Commenter()
    form = CommenterForm(request.POST, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    ctx = {
        "comments": comments,
        "videos": videos,
        "courses": courses,
        "user": user,
        "cour_id": cour_id,
        "name": name,
    }
    return render(request, 'store/video.html', ctx)


# def showvideo(request, pk):
#     user = 2
#     name = "Tom"
#     course = get_course_by_id(course_id=pk)
#     cour_id = course[0]['id']
#     videos = get_video_by_course_id(pk)
#     # commenter = get_commenter(pk, video_id=pks)
#     comment_limit = get_commenter_by_limit()
#     # length_comment = len(commenter)
#
#     model = Commenter()
#     form = CommenterForm(request.POST, instance=model)
#     if request.POST:
#         if form.is_valid():
#             form.save()
#
#     ctx = {
#         'name': name,
#         'user': user,
#         'course': course,
#         # "commenter": commenter,
#         # 'comment_limit': comment_limit,
#         # 'length': length_comment,
#         'cour_id': cour_id,
#         'videos': videos
#     }
#
#     return render(request, 'store/video.html', ctx)


def contact(request):
    ctx = {
        'contact_page': 'active'
    }
    return render(request, 'store/profile.html', ctx)
