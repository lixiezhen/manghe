from django.shortcuts import render,reverse,redirect,get_object_or_404
from .models import Man_box,Woman_box,Cltman_Box,Cltwoman_Box,Comment
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from .forms import Woman_boxForm,Man_boxForm,CommentForm
import random
from django.db.models import Q
from django.utils.safestring import mark_safe
from datetime import datetime
from django.views.decorators.http import require_POST
# Create your views here.
def head(request):
    """首页"""
    return render(request, 'header.html')
def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'header.html', {'error_msg': error_msg})

    Box_list1 =Woman_box.objects.filter(Q(name__icontains=q) | Q(intro__icontains=q) | Q(photo__icontains=q) | Q(school__name__icontains=q))
    Box_list2 = Man_box.objects.filter(Q(name__icontains=q) | Q(intro__icontains=q) | Q(photo__icontains=q) | Q(school__name__icontains=q))
    return render(request, 'results.html', {'error_msg': error_msg,
                                               'Box_list1': Box_list1,'Box_list2': Box_list2})
def put(request):
    """"放置盲盒"""
    return render(request, 'put.html')
def random_list(request):
    return render(request,'random.html')
def edit_box(request):
    user = User.objects.get(username=request.user.username)
    box = Woman_box.objects.get(user=user)
    if box:
        if request.method == "POST":
            woman_box_form = Woman_boxForm(request.POST)
            if woman_box_form.is_valid():
                box_cd = woman_box_form.cleaned_data
                box.user = box_cd['user']
                box.name = box_cd['name']
                box.age = box_cd['age']
                box.gender = box_cd['gender']
                box.area = box_cd['area']
                box.qq = box_cd['qq']
                box.mobile = box_cd['mobile']
                box.email = box_cd['email']
                box.intro = box_cd['intro']
                box.save()
            return HttpResponseRedirect('/account/my-information/')
        else:
            woman_box_form = Woman_boxForm(instance=box)
            return render(request, "woman/box_edit.html", {"woman_box_form":woman_box_form,})
    box = Man_box.objects.get(user=user)
    if box:
        if request.method == "POST":
            woman_box_form = Woman_boxForm(request.POST)
            if woman_box_form.is_valid():
                box_cd = woman_box_form.cleaned_data
                box.user = box_cd['user']
                box.name = box_cd['name']
                box.age = box_cd['age']
                box.gender = box_cd['gender']
                box.area = box_cd['area']
                box.qq = box_cd['qq']
                box.mobile = box_cd['mobile']
                box.email = box_cd['email']
                box.intro = box_cd['intro']
                box.save()
            return HttpResponseRedirect('/account/my-information/')
        else:
            woman_box_form = Woman_boxForm(instance=box)
            return render(request, "woman/box_edit.html", {"woman_box_form":woman_box_form,})
def delete_box(request):
    user = User.objects.get(username=request.user.username)
    if Woman_box.objects.get(user=user):
        Woman_box.objects.filter(user=user).delete()
        return redirect('/account/my-information/')
    else:
        Man_box.objects.filter(user=user).delete()
        return redirect('/account/my-information/')
def delete_cltbox(request,box_id):
    if Cltwoman_Box.objects.get(Cltbox_id=box_id):
        Cltwoman_Box.objects.filter(Cltbox_id=box_id).delete()
        return redirect('/box/collect/')
    else:
        Cltman_Box.objects.filter(Cltbox_id=box_id).delete()
        return redirect('/box/collect/')
def collect(request):
    return render(request, 'collect.html')


def man_box(request):
    page = int(request.GET.get('page', 1))
    page_size = 10
    start = (page - 1) * page_size
    end = page * page_size
    total_count = Man_box.objects.all().count()
    total_page_count, div = divmod(total_count, page_size)
    if div:
        total_page_count += 1
    plus = 5
    if total_page_count <= 2 * plus + 1:
        start_page = 1
        end_page = total_page_count
    else:
        if page <= plus:
            start_page = 1
            end_page = 2 * plus + 1
        else:
            if (page + plus) > total_page_count:
                start_page = total_page_count - 2 * plus
                end_page = total_page_count
            else:
                start_page = page - plus
                end_page = page + plus + 1

    queryset = Man_box.objects.all()[start:end]
    page_str_list = []
    if page > 1:
        prev = '<li><a href="/box/man/?page={}">上一页</a></li>'.format(page - 1)
    else:
        prev = '<li><a href="/box/man/?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev)
    for i in range(start_page, end_page + 1):
        if i == page:
            ele = '<li class="active"><a href="/box/man/?page={}">{}</a></li>'.format(i, i)
        else:
            ele = '<li><a href="/box/man/?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(ele)
    if page < total_page_count:
        prev = '<li><a href="/box/man/?page={}">下一页</a></li>'.format(page + 1)
    else:
        prev = '<li><a href="/box/man/?page={}">下一页</a></li>'.format(total_page_count)
    page_str_list.append(prev)
    page_string = mark_safe("".join(page_str_list))
    return render(request, 'man/man.html', {'queryset': queryset,'page_string':page_string})
def woman_box(request):
    page = int(request.GET.get('page', 1))
    page_size = 10
    start = (page - 1) * page_size
    end = page * page_size
    total_count = Woman_box.objects.all().count()
    total_page_count, div = divmod(total_count, page_size)
    if div:
        total_page_count += 1
    plus = 5
    if total_page_count <= 2 * plus + 1:
        start_page = 1
        end_page = total_page_count
    else:
        if page <= plus:
            start_page = 1
            end_page = 2 * plus + 1
        else:
            if (page + plus) > total_page_count:
                start_page = total_page_count - 2 * plus
                end_page = total_page_count
            else:
                start_page = page - plus
                end_page = page + plus + 1

    queryset = Woman_box.objects.all()[start:end]
    page_str_list = []
    if page > 1:
        prev = '<li><a href="/box/woman/?page={}">上一页</a></li>'.format(page - 1)
    else:
        prev = '<li><a href="/box/woman/?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev)
    for i in range(start_page, end_page + 1):
        if i == page:
            ele = '<li class="active"><a href="/box/man/?page={}">{}</a></li>'.format(i, i)
        else:
            ele = '<li><a href="/box/woman/?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(ele)
    if page < total_page_count:
        prev = '<li><a href="/box/woman/?page={}">下一页</a></li>'.format(page + 1)
    else:
        prev = '<li><a href="/box/woman/?page={}">下一页</a></li>'.format(total_page_count)
    page_str_list.append(prev)
    page_string = mark_safe("".join(page_str_list))
    return render(request, 'woman/woman.html', {'queryset': queryset,'page_string':page_string})


def woman_intro(request,box_id):
    #user = User.objects.get(username=request.user.username)
    #box_id = request.POST('woman_box_id')
    box = Woman_box.objects.get(id=box_id)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.box1 = box
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,"woman/detail.html",{'box': box,
                                               "comment_form": comment_form })
def woman_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        woman_box = Woman_box.objects.get(user=request.user.id)
        woman_box.photo = img
        woman_box.save()
        return HttpResponse("1")
    else:
        return render(request, 'woman/imagecrop.html',)
def woman_random(request):
    last = Woman_box.objects.all().count() - 1
    random_num = random.randint(0, last)
    box = Woman_box.objects.get(id=random_num)
    return render(request, 'woman/detail.html', {'box': box})
def woman_put(request):
    if request.method == "GET":
        form = Woman_boxForm
        return render(request, 'woman/put.html', {"form": form})
    form = Woman_boxForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('box:woman')
    return render(request, 'woman/put.html', {"form": form})
def collect_woman_box(request,*args, **kwargs):
    current_user = request.user
    pk_box = get_object_or_404(Woman_box,id=int(kwargs['pk']))
    new_clt_box = Cltwoman_Box()
    new_clt_box.who_clt = current_user
    new_clt_box.Cltbox = pk_box
    new_clt_box.author = pk_box.user
    new_clt_box.save()
    pk_box.save()
    return HttpResponseRedirect(reverse('box:woman_intro', args=(int(kwargs['pk']),)))
def woman_collection(request):
    current_user = request.user
    all_clt_box = Cltwoman_Box.objects.filter(who_clt=current_user)
    return render(request, 'show-womanclt.html', {'all_clt_box': all_clt_box})


def man_intro(request,box_id):
    box = Man_box.objects.get(id=box_id)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.box1 = box
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "woman/detail.html", {'box': box,
                                                 "comment_form": comment_form})
def man_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        man_box = Man_box.objects.get(user=request.user.id)
        man_box.photo = img
        man_box.save()
        return HttpResponse("1")
    else:
        return render(request, 'man/imagecrop.html',)
def man_random(request):
    last = Man_box.objects.all().count() - 1
    random_num = random.randint(0, last)
    box = Man_box.objects.get(id=random_num)
    return render(request, 'man/detail.html', {'box': box})
def man_put(request):
    if request.method == "GET":
        form = Man_boxForm
        return render(request, 'man/put.html', {"form": form})
    form = Man_boxForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('box:man')
    return render(request, 'man/put.html', {"form": form})
def collect_man_box(request,*args, **kwargs):
    current_user = request.user
    pk_box = get_object_or_404(Man_box,id=int(kwargs['pk']))
    new_clt_box = Cltman_Box()
    new_clt_box.who_clt = current_user
    new_clt_box.Cltbox = pk_box
    new_clt_box.author = pk_box.user
    new_clt_box.save()
    pk_box.save()
    return HttpResponseRedirect(reverse('box:man_intro', args=(int(kwargs['pk']),)))
def man_collection(request):
    current_user = request.user
    all_clt_box = Cltman_Box.objects.filter(who_clt=current_user)
    return render(request, 'show-manclt.html', {'all_clt_box': all_clt_box})


def comment_control(request):
    if request.user.username:
        comment_content = request.POST.get('comment_content')
        box1_id = request.POST.get('box1_id')
        box2_id = request.POST.get('box2_id')
        pid = request.POST.get('pid')
        author_id = request.user.id  # 获取当前用户的ID

        Comment.objects.create(comment_content=comment_content, pre_comment_id=pid, box1_id=box1_id,box2_id=box2_id,
                               comment_author_id=author_id)

        box = list(
            Comment.objects.values('id', 'comment_content', 'pre_comment_id', 'box1_id','box2_id','comment_author_id',
                                   'comment_time'))

        return JsonResponse(box, safe=False)
    else:
        return redirect('/account/login/')
