from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from user.forms import LoginForm, RegForm, ProfileForm
from product.models import Basket


def log(request):
    if request.method == 'POST':
        frm = LoginForm(data=request.POST)
        if frm.is_valid():
            usern = request.POST['username']
            passwd = request.POST['password']
            userr = auth.authenticate(username=usern, password=passwd)
            if userr and userr.is_active:
                auth.login(request, userr)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(frm.errors)
    else:
        frm = LoginForm()
    con = {'frm': frm}
    return render(request, 'user/login.html', con)


def reg(request):
    if request.method == 'POST':
        form = RegForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сәтті тіркелдіңіз!')
            return HttpResponseRedirect(reverse('user:log'))
        else:
            print(form.errors)
    else:
        form = RegForm()
    con = {'form': form}
    return render(request, 'user/register.html', con)


@login_required
def prof(request):
    user = request.user
    if request.method == 'POST':
        frm = ProfileForm(data=request.POST, files=request.FILES, instance=user)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect(reverse('user:prof'))
    else:
        frm = ProfileForm(instance=user)
    baskets = Basket.objects.filter(user=user)
    total_quant = 0
    total_sum = 0
    for basket in baskets:
        total_quant += basket.quant
        total_sum += basket.sum()
    con = {'frm': frm, 'title': 'ХҚТУ - Жеке Кабинет',
           'baskets': baskets,
           'total_quantity': total_quant,
           'total_sum': total_sum,
           }
    return render(request, 'user/profile.html', con)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
