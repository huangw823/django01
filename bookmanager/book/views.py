from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest
#定义一个视图函数
"""
视图函数有两个要求：
1.第一个参数必须是请求体就是from django.http import HttpRequest的对象
2.第二个就是必须要返回响应，必须要return
"""
def index(request): #request参数就是浏览器的请求体
    """返回一个ok"""
    return HttpResponse("ok")