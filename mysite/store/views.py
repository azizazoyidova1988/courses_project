from django.shortcuts import render, redirect
from .services import *
from .models import *
from .forms import *


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
    ctx = {
        'course_page': 'active'
    }
    return render(request, 'store/courses.html', ctx)


def news(request):
    ctx = {
        'news_page': 'active'
    }
    return render(request, 'store/news.html', ctx)


def contact(request):
    ctx = {
        'contact_page': 'active'
    }
    return render(request, 'store/profile.html', ctx)
