from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from store.models import Commenter, Course,Team,Video,News,Subscribe,Items
from store.forms import *
from . import servises


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    course = servises.get_courses_count()
    news_count = servises.get_news_count()
    teams_count = servises.get_teams_count()
    print("AAAA", teams_count)
    commenter_count = servises.get_commenter_count()

    ctx = {
        "course": course,
        "news_count":  news_count,
        "teams_count": teams_count,
        "commenter_count": commenter_count,

    }
    return render(request, 'dashboard/index.html',ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')


@login_required_decorator
def courses_list(request):
    courses = servises.get_courses()
    ctx = {
        "courses": courses
    }
    return render(request, 'dashboard/course/list.html', ctx)


@login_required_decorator
def courses_create(request):
    model = Course()
    form = CourseForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('courses_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/course/form.html', ctx)


@login_required_decorator
def courses_edit(request, courses_id):
    model = Course.objects.get(id=courses_id)
    form = CourseForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('courses_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/course/form.html', ctx)

@login_required_decorator
def courses_delete(request, courses_id):
    model = Course.objects.get(id=courses_id)
    model.delete()
    return redirect("courses_list")


@login_required_decorator
def commenter_list(request):
    commenter = servises.get_commenter()
    ctx = {
        "commenter": commenter
    }
    return render(request, 'dashboard/commenter/list.html', ctx)


@login_required_decorator
def commenter_create(request):
    model = Commenter()
    form = CommenterForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('commenter_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/commenter/form.html', ctx)

@login_required_decorator
def commenter_edit(request, commenter_id):
    model = Commenter.objects.get(id=commenter_id)
    form = CommenterForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('commenter_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/commenter/form.html', ctx)

@login_required_decorator
def commenter_delete(request, commenter_id):
    model = Commenter.objects.get(id=commenter_id)
    model.delete()
    return redirect("commenter_list")


@login_required_decorator
def items_list(request):
    items = servises.get_items()
    ctx = {
        "items": items
    }
    return render(request, 'dashboard/items/list.html', ctx)


@login_required_decorator
def items_create(request):
    model = Items()
    form = ItemsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('items_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/items/form.html', ctx)

@login_required_decorator
def items_edit(request, item_id):
    model = Items.objects.get(id=item_id)
    form = ItemsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('items_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/items/form.html', ctx)

@login_required_decorator
def items_delete(request, item_id):
    model = Items.objects.get(id=item_id)
    model.delete()
    return redirect("items_list")


@login_required_decorator
def video_list(request):
    videos = servises.get_videos()
    print(videos)
    ctx = {
        "videos": videos
    }
    return render(request, 'dashboard/video/list.html', ctx)


@login_required_decorator
def video_create(request):
    model = Video()
    form = VideoForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('video_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/video/form.html', ctx)

@login_required_decorator
def video_edit(request, video_id):
    model = Video.objects.get(id=video_id)
    form = VideoForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('video_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/video/form.html', ctx)

@login_required_decorator
def video_delete(request, video_id):
    model = Video.objects.get(id=video_id)
    model.delete()
    return redirect("video_list")

@login_required_decorator
def teams_list(request):
    teams = servises.get_teams()
    print(teams)
    ctx = {
        "teams": teams
    }
    return render(request, 'dashboard/team/list.html', ctx)


@login_required_decorator
def teams_create(request):
    model = Team()
    form = TeamForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('teams_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/team/form.html', ctx)


@login_required_decorator
def teams_edit(request, teams_id):
    model = Team.objects.get(id=teams_id)
    form = TeamForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('teams_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/team/form.html', ctx)

@login_required_decorator
def teams_delete(request, teams_id):
    model = Team.objects.get(id=teams_id)
    model.delete()
    return redirect("teams_list")


@login_required_decorator
def news_list(request):
    news = servises.get_news()
    ctx = {
        "news": news
    }
    return render(request, 'dashboard/news/list.html', ctx)

@login_required_decorator
def news_create(request):
    model = News()
    form = NewsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news/form.html', ctx)

@login_required_decorator
def news_edit(request, news_id):
    model = News.objects.get(id=news_id)
    form = NewsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news/form.html', ctx)

@login_required_decorator
def news_delete(request, news_id):
    model = News.objects.get(id=news_id)
    model.delete()
    return redirect("news_list")

