from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from bilibili import models
import time


# Create your views here.
def movielist(request):
    request.encoding = 'utf-8'
    keyword = request.GET.get('keyword')

    all_movies = models.Movie.objects.all()
    count = all_movies.count()
    t0 = time.time()
    searchtime = 0

    if keyword:
        if len(keyword) > 50:
            info = "输入内容请保持50字符以内，请输入其他关键词"
            return render(request, 'movielist.html', {'info': info})
        movie_list = models.Movie.objects.all().filter(moviename__icontains=keyword) | models.Movie.objects.all().filter(moviedescription__icontains=keyword)
        all_movies = movie_list
        count = movie_list.count()
        searchtime = round(time.time() - t0, 3)
    else:
        keyword = ""

    if all_movies:
        paginator = Paginator(all_movies, 20)
        page = request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)
        return render(request, 'movielist.html', {'movies': movies, 'keyword': keyword, 'count': count, 'time': searchtime})
    else:
        info = "共 0 条结果，请输入其他关键词"
        return render(request, 'movielist.html', {'info': info})



def userlist(request):
    request.encoding = 'utf-8'
    keyword = request.GET.get('keyword')

    all_users = models.User.objects.all()
    count = all_users.count()
    t0 = time.time()
    searchtime = 0

    if keyword:
        user_list = models.User.objects.all().filter(username__icontains=keyword) | models.User.objects.all().filter(userdescription__icontains=keyword)
        all_users = user_list
        count = user_list.count()
        searchtime = round(time.time() - t0, 3)
    else:
        keyword = ""

    if all_users:
        paginator = Paginator(all_users, 20)
        page = request.GET.get('page')
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'userlist.html', {'users': users, 'keyword': keyword, 'count': count, 'time': searchtime})
    else:
        info = "共 0 条结果，请输入其他关键词"
        return render(request, 'userlist.html', {'info': info})


def movie(request, movieID):
    movie = models.Movie.objects.get(pk=movieID)
    userID = models.User.objects.get(username=movie.username).pk
    return render(request, 'moviedetail.html', {'movie': movie, 'userID': userID})


def user(request, userID):
    user = models.User.objects.get(pk=userID)
    movies = []
    for movieID in user.movies.all():
        movies.append(models.Movie.objects.get(pk=movieID.pk))
    return render(request, 'userdetail.html', {'user': user, 'movies': movies})
