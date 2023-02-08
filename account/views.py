from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, UserInfoForm, UserForm
from .models import UserInfo
from django.contrib.auth.models import User
from django.urls import reverse
from box.models import Woman_box,Man_box
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse('Welcome You.')
            else:
                return HttpResponse('Sorry')
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,"account/login.html",{'form':login_form})


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid().is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            return HttpResponse("抱歉，注册失败")
    else:
        user_form = RegistrationForm()
        return render(request, "account/register.html", {"form": user_form, })

@login_required(login_url='/account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, "account/myself.html", {"user":user, "userinfo":userinfo,})
def my_box(request):
    user = User.objects.get(username=request.user.username)
    box = Woman_box.objects.get(user=user)
    if box:
        return render(request, "account/detail.html",{"box":box})
    box = Man_box.objects.get(user=request.user.username)
    if box:
        return render(request, "account/detail.html",{"box":box})




@login_required(login_url='/account/login/')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid()  * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            user.email = user_cd['email']
            user.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        user_form = UserForm(instance=request.user)
        return render(request, "account/myself_edit.html", {"user_form":user_form,})

@login_required(login_url='/account/login/')
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, 'account/imagecrop.html',)
