from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import random, string
from django.conf import settings
from .models import *


def homepage(request):
    return render(request, 'shortener/home.html')


def redirect_original(request, short_code):
    obj = get_object_or_404(Urls, short_code=short_code)
    return HttpResponseRedirect(obj.url_input)


def code_generator(length=6, chars=string.ascii_lowercase + string.digits):
    new_code = ''.join(random.choice(chars) for _ in range(length))
    q = Urls.objects.filter(short_code=new_code).exists()
    if q:
        return code_generator(length=length)
    return new_code


def shorten_url(request):
    error = False
    short_code = code_generator()

    if len(request.POST['url']) == 0:
        error = True

    if error:
        return render(request, 'shortener/home.html', {'invalid_form': 'Enter URL!', 'fields': request.POST})

    r = Urls(
            url_input=request.POST['url'],
            short_code=short_code)
    r.save()

    new_url = settings.SITE_URL + "/" + short_code
    return render(request, 'shortener/success.html', {'new_url': new_url, 'fields': request.POST})
