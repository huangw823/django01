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
    # return HttpResponse("ok")

    # render(request, template_name, context=None,             )
    # request, 请求体
    # template_name, 渲染的模板文件
    # context=None, 视图（view）与模板的数据交互
    context={"name":"雷军"}
    return render(request,'book/index.html',context=context)