from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def my_create(request):

    return HttpResponse('create')

def my_get_url(request,h_name,w_id):

    print(h_name,w_id)
    return HttpResponse('转换器')

def datas(request):
    print(request.GET)
    print(request.GET.getlist('b'))
    print(request.GET['b'])

    return HttpResponse('datas')

def post_body_form(request):
    print(request.POST)

    return HttpResponse('post_body_form')


def myjson(request):
    import json
    mybody=request.body #获得原始二进制请求体（json）
    print(mybody)
    my_dict=json.loads(mybody) #转化为字典
    print(my_dict)
    return HttpResponse('myjson')

def meta(request):

    return HttpResponse(request.META)

def my_response(request):
    #HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    resp=HttpResponse('哈哈哈哈')
    resp['huangwei']=666 #添加自己格外设置的参数
    resp.status_code=400 #设置状态吗

    return resp

def my_json(request):
    """返回json数据"""
    from django.http import JsonResponse

    #JsonResponse(data(默认字典数据), safe=True（如果想传列表，改为False）)
    mydict={'name':'huang','age':18}

    # return JsonResponse(mydict) #传入字典

    mylist=[
        {'name':'huang','age':12},
        {'name':'wei','age':54}
    ]
    return  JsonResponse(mylist,safe=False) #传入列表

def my_redirect(request):
    """重定向"""
    # return redirect('/create')

    return redirect('https://www.baidu.com')

def set_cookie(request):
    """设置cookie"""

    resp=HttpResponse('set_cookie') #拿到响应体对象
    # HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)  #cookie以键值对保存
    resp.set_cookie('name',request.GET['name'],max_age=60*60)

    return resp
def get_cookie(request):
    """拿到cookie"""
    cok=request.COOKIES
    # print(cok)
    # print(cok['name'])

    res=HttpResponse('拿到cookie\t' + cok.get('name','无name'))
    res.delete_cookie('name') #删除

    return res

def set_session(request):
    """设置session"""
    name=request.GET.get('name')
    request.session['name']=name
    request.session['password']='123'
    return HttpResponse('设置session')

def get_session(request):
    """获得session"""

    name=request.session.get('name')
    request.session.clear() #删除值部分(我们设置的那些被删除)
    # request.session.flush() #删除整条session
    # del request.session['password'] #删除session指定内容

    return HttpResponse(name)

#############类视图####################
from django.views import View
class login(View):

    def get(self,request):
        """处理get请求"""

        return HttpResponse("get请求")

    def post(self,request):
        """处理post请求"""
        return HttpResponse("post请求")

###########类视图的多继承重写dispatch###
from django.contrib.auth.mixins import LoginRequiredMixin
class loginView(LoginRequiredMixin,View):

    def get(self,request):
        return HttpResponse('登录成功')

def zjj(request):
    """中间件"""
    print('视图被调用')

    return HttpResponse('中间件')









