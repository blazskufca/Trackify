from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .tracker_logic import BigBangTracker, AmazonDeTracker, EnaATracker, FuntechTracker
from babel.numbers import format_currency
from . import forms
import json
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def is_auth(request, search):
    instance = get_object_or_404(models.TrackedProducts, link=search)
    if request.user.is_authenticated:
        userProfile = models.Profile.objects.get(user=request.user)
        userProfile.items.add(instance)
        userProfile.save()
    return instance


def home(request):
    if request.method == 'GET':
        last_three = models.TrackedProducts.objects.order_by('-date')[:3]
        if request.user.is_authenticated:
            profile = models.Profile.objects.get(user=request.user)
            context = {'form': forms.SearchForm(),
                       'recently': last_three,
                       'tracked': profile.items.all()[:3],
                       }
        else:
            context = {'form': forms.SearchForm(),
                       'recently': last_three,
                       }

        return render(request, 'tracker/index.html', context)

    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            if not models.TrackedProducts.objects.filter(link=search).exists() \
                    and (search[:23] == 'https://www.bigbang.si/'):
                BigBangTracker().scrape(search)
                return redirect('product_details', is_auth(request, search).pk)

            elif not models.TrackedProducts.objects.filter(link=search).exists() \
                    and (search[:22] == 'https://www.amazon.de/'):
                AmazonDeTracker().scrape(search)
                return redirect('product_details', is_auth(request, search).pk)

            elif not models.TrackedProducts.objects.filter(link=search).exists() \
                    and (search[:21] == "https://www.enaa.com/"):
                EnaATracker().scrape(search)
                return redirect('product_details', is_auth(request, search).pk)

            elif not models.TrackedProducts.objects.filter(link=search).exists() \
                    and (search[:23] == "https://www.funtech.si/"):
                FuntechTracker().scrape(search)
                return redirect('product_details', is_auth(request, search).pk)

            elif models.TrackedProducts.objects.filter(link=search).exists():
                return redirect('product_details', is_auth(request, search).pk)

            else:
                if request.user.is_authenticated:
                    profile = models.Profile.objects.get(user=request.user)
                    context = {
                        'err': 'You tried to do something which is not allowed.\n'
                               'Only links from www.enaa.com, www.funtech.si, bigbang.si, and amazon.de are supported '
                               'right now!',
                        'recently': models.TrackedProducts.objects.order_by('-date')[:3],
                        'form': forms.SearchForm(),
                        'tracked': profile.items.all()[:3],

                    }
                else:
                    context = {
                        'err': 'You tried to do something which is not allowed.\n'
                               'Only links from www.enaa.com, www.funtech.si, bigbang.si, and amazon.de are supported '
                               'right now!',
                        'recently': models.TrackedProducts.objects.order_by('-date')[:3],
                        'form': forms.SearchForm(),
                    }
                return render(request, 'tracker/index.html', context)
        else:
            if request.user.is_authenticated:
                context = {'form': form,
                           'recently': models.TrackedProducts.objects.order_by('-date')[:3],
                           }
            else:
                context = {'form': form, 'recently': models.TrackedProducts.objects.order_by('-date')[:3], }
            return render(request, 'tracker/index.html', context)


def product_details(request, pk):
    instance = get_object_or_404(models.TrackedProducts, pk=pk)
    dates = json.loads(instance.priceHistory)
    return render(request,
                  'tracker/product_details.html',
                  context={'instance': instance,
                           'price': format_currency(instance.price,
                                                    'EUR',
                                                    locale='sl_SI'),
                           'chart_dates': list(dates.keys()),
                           'chart_values': list(dates.values())})


def about(request):
    return render(request, 'tracker/About.html')


def all_tracked(request):
    paginator = Paginator(models.TrackedProducts.objects.all(), 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'tracker/all.html', context)


@login_required(login_url='login')
def my_tracked(request):
    profile = models.Profile.objects.get(user=request.user)
    paginator = Paginator(profile.items.all(), 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'tracker/My_tracked.html', context)


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = forms.RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
