from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import Item, Project, Comment, Genre, Part, Chapter
from django.http import Http404
from app.forms import commentForm, searchForm
from datetime import date

count_by_page = 3


def error(request):
    return HttpResponse("Тут насрал гантер, убирай:\n\n   🐧 💩")


def news(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    count = Item.objects.count();
    link = 2
    if (count <= count_by_page):
        link = 0
    return render(
        request,
        'news.html',
        {
            'title': 'Новости',
            'news': Item.objects.all().order_by('-date')[0:count_by_page],
            'link': link,
            'prev_link': 0,
        }
    )


def news_page(request, num):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    count = Item.objects.count();
    link = int(num) + 1
    if ((count + count_by_page - 1) < (int(num) + 1) * count_by_page):
        link = 0
    if (int(num) * count_by_page > count + count_by_page or int(num) <= 0):
        raise Http404
    return render(
        request,
        'news.html',
        {
            'title': 'Новости',
            'news': Item.objects.all().order_by('-date')[(int(num) - 1) * count_by_page:int(num) * count_by_page],
            'link': link,
            'prev_link': int(num) - 1,
        }
    )


def comment(request, id):
    item = Item.objects.get(pk=id)
    form_view = commentForm
    error = 0;
    if request.POST:
        form = commentForm(request.POST)
        if form.is_valid():
            comment = Comment(name=form.cleaned_data['username'])
            comment.text = form.cleaned_data['text']
            comment.date = datetime.today()
            comment.save()
            item.comments.add(comment)
            item.save()
            error = 0
            return HttpResponseRedirect('/comments/' + id + '/')
        else:
            error = 1
            form_view = commentForm(
                initial={'username': form.cleaned_data['username'], 'text': form.cleaned_data['text']})

    return render(
        request,
        'comments.html',
        {
            'title': item.title,
            'item': item,
            'form': form_view,
            'comments': item.comments.all(),
            'error': error,
        }
    )


def project(request, id):
    assert isinstance(request, HttpRequest)
    project = Project.objects.get(pk=id)
    return render(
        request,
        'project.html',
        {
            'title': 'Наши проекты',
            'project': project,
            'form': searchForm,
            'parts': project.parts.all(),
        }
    )


def projects(request):
    assert isinstance(request, HttpRequest)
    projects = Project.objects.all().filter(censor=False)
    return render(
        request,
        'projects.html',
        {
            'title': 'Наши проекты',
            'projects': projects,
            'form': searchForm,
        }
    )


def projects_search(request):
    assert isinstance(request, HttpRequest)
    form = searchForm
    genre = 'Все, кроме 18+'
    status = 'Все'
    projects = Project.objects.all().filter(censor=False)
    if ('genre' in request.GET):
        genre = request.GET['genre']
        if (genre == 'Все'):
            projects = Project.objects.all()
        elif (genre != 'Все, кроме 18+'):
            projects = projects.filter(genres__name=genre)
    if ('status' in request.GET):
        status = request.GET['status']
        if (status != 'Все'):
            projects = projects.filter(translation_status__name=status)

    form = searchForm(initial={'status': status, 'genre': genre})

    return render(
        request,
        'projects.html',
        {
            'title': 'Поиск по проектам',
            'projects': projects,
            'form': form,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        {
            'title': 'Информация о команде',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )
