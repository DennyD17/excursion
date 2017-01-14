from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import ReviewForm, RegistrationToEventForm
from . import models
from excursion import settings


def start_page(request):
    about = models.About.objects.all()[0]
    try:
        message = models.ImportantNote.objects.all()[0]
    except IndexError:
        return render(request, 'ex/main_page.html', {'about': about})
    return render(request, 'ex/main_page.html', {'message': message, 'about': about})


def excursions(request, slug=None):
    list_of_excursions = models.Excursion.objects.all()
    if slug is None:
        try:
            start_value = models.Excursion.objects.all()[0]
        except IndexError:
            return render(request, 'ex/excursions.html', {'Error_message': 'Извините, тут пока ничего нет'})
        else:
            return render(request, 'ex/excursions.html', {'list_of_excursions': list_of_excursions,
                                                          'first': start_value})
    else:
        start_value = get_object_or_404(models.Excursion, slug=slug)
        return render(request, 'ex/excursions.html', {'list_of_excursions': list_of_excursions, 'first': start_value,
                                                      'slug': slug})


def reg(request):
    if request.method == 'POST':
        form = RegistrationToEventForm(request.POST)
        if form.is_valid():
            form.save()
            mailto = form.cleaned_data.get('email')
            mes = form.cleaned_data.get('name') + \
                ', доброго времени суток! \nПоздравляю, вы успешно записаны на экскурсию ' + \
                str(form.cleaned_data.get('event'))
            send_mail('Запись на экскурсию', mes, settings.EMAIL_HOST_USER, ['Denis.Avramenko1705@gmail.com', mailto])
            return HttpResponseRedirect(reverse('ex:registration'))
    else:
        form = RegistrationToEventForm(initial={'event': request.GET.get('id', None)})
    people = models.PeopleReg.objects.all()
    return render(request, 'ex/registration.html', {'form': form, 'people': people,
                                                    'contacts': models.Contacts.objects.all()[0]})


def add_review(request):
    all_reviews = models.Reviews.objects.all().order_by('-date')
    paginator = Paginator(all_reviews, 5)
    try:
        reviews = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ex:reviews'))
    else:
        form = ReviewForm()
    return render(request, 'ex/reviews.html', {'form': form, 'reviews': reviews})


def blog(request):
    sorting = False
    posts = models.Blog.objects.all().order_by('-date_added')
    if request.GET.get('sort_by'):
        sorting = True
        if request.GET.get('sort_by') == 'likes':
            posts = models.Blog.objects.all().order_by('-likes')
    likes = []
    for post in posts:
        if str(post.id) in request.COOKIES:
            likes.append(int(post.id))
    paginator = Paginator(posts, 5)
    try:
        posts_paginated = paginator.page(request.GET.get('page'))
    except EmptyPage:
        posts_paginated = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts_paginated = paginator.page(1)
    return render(request, 'ex/blog.html', {'posts': posts_paginated, 'favorite': likes, 'sorted': sorting})


def post_view(request, pk):
    post = get_object_or_404(models.Blog, id=pk)
    if str(pk) in request.COOKIES:
        liked = True
    else:
        liked = False
    return render(request, 'ex/post.html', {'post': post, 'liked': liked})


def like_post(request):
    post_id = None
    if request.method == 'GET':
        post_id = request.GET.get('post_id')
    likes = 0
    response = HttpResponse(likes)
    if post_id:
        post = models.Blog.objects.get(id=int(post_id))
        if post:
            if post_id in request.COOKIES:
                post.likes -= 1
                post.save()
                likes = post.likes
                response = HttpResponse(likes)
                response.delete_cookie(post_id)
            else:
                post.likes += 1
                post.save()
                likes = post.likes
                response = HttpResponse(likes)
                response.set_cookie(post_id, 'adw')
    return response
