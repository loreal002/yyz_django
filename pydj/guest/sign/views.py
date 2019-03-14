from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from sign.models import  Event,Guest
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import auth
# Create your views here.
def index(request):
    #return HttpResponse("hello,django")
    data = {'name':'tom','age':22}
    return render(request,'index.html')

def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user) #登录
            request.session['user'] = username
            response = HttpResponseRedirect("/event_manage/")

            return response
        else:
            return render(request,"index.html",{"error":"用户名或密码错误"})
    else:
        return render(request,"index.html")


@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','')#读取浏览器cookies
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username,'events':event_list})


@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name)
    #event_list = Event.objects.get(name=search_name)
    return render(request, "event_manage.html", {"user": username,
"events":event_list})

@login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list=Guest.objects.all()
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,
"guests": contacts})

# @login_required
# def guest_search_name(request):
#     username = request.session.get('user','')
#     realname = request.GET.get('realname')
#     event_list = Guest.objects.filter(name__contains=realname)
#     return render(request, "event_manage.html", {"user": username,
# "events": event_list})

# @login_required
# def guest_manage_add(request):
#     event = request.POST.get('event')
#     email = request.POST.get('email')
#     sign = request.POST.get('sign')
#     phone = request.POST.get('phone')
#     create_time = request.POST.get('create_time')
#     realname = request.POST.get('realname')
#     print(request.POST)
#      # 数据库添加操作
#     Guest.objects.create(event=event,email=email,sign=sign,phone=phone,create_time=create_time,realname=realname)
#     return HttpResponseRedirect("/guest_manage/")
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})


@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone','')
    result = Guest.objects.filter(phone = phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
        'hint': 'phone error.'})
    result = Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
        'hint': 'event id or phone error.'})
    result = Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,
        'hint': "user has sign in."})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event,
        'hint':'sign in success!',
        'guest': result})
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response
