from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello, World")

def joy(request):
    context2 = {
        'name': 'joy',
        'img_src': 'https://i.pinimg.com/736x/f9/2b/2d/f92b2d6b4330a47ff441d6db33e86136.jpg'
    }
    #
    return render(request, 'self_redvelvet/member.html',context = context2)

def seulgi(request):
    context3 = {
        'name': 'seulgi',
        'img_src': 'https://thumbnews.nateimg.co.kr/view610///news.nateimg.co.kr/orgImg/sd/2022/03/15/112339512.1.jpg'
    }
    return render(request, 'self_redvelvet/member.html', context=context3)