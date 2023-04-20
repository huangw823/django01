from book import views
from django.urls import path

from django.urls import converters,register_converter

#
# 1.自定义正则表达式设置自定义转换器
class MyIntConverter:
    """自定义路由转换器：匹配手机号"""
    regex = '1[3-9]\d{9}' #正则表达式

    def to_python(self, value):
        return int(value) ## 将匹配结果传递到视图内部时使用

    def to_url(self, value):
        return str(value) #将匹配结果用于反向解析传值时使用

#2.注册自定义转换器
# register_converter(自定义路由转换器, '别名')
register_converter(MyIntConverter,'phone')

#3.测试path()中自定义路由转换器提取路径参数：手机号 http://127.0.0.1:8000/18500001111/

urlpatterns = [
    path('create/',views.my_create),
    path('<phone:h_name>/<w_id>/',views.my_get_url), #自定义转换器别名
    path('datas/',views.datas),
    path('post_body_form/',views.post_body_form),
    path('myjson/',views.myjson),
    path('meta/',views.meta),
    path('my_response/',views.my_response),
    path('my_json/',views.my_json),
    path('my_redirect/',views.my_redirect),
    path('set_cookie/',views.set_cookie),
    path('get_cookie/',views.get_cookie),
    path('set_session/',views.set_session),
    path('get_session/',views.get_session),
    #####################类视图
    path('login/',views.login.as_view()),
    path('loginView/',views.loginView.as_view()),

    path('zjj/',views.zjj),
]