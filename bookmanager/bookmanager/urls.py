"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from book import views
from django.conf.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('url地址/', 根据url地址响应指定的视图函数（填写函数名）),
    # path('index/', views.index),

    #当url过多不利于我们管理，
    #我们可以将每个子应用的url归每个子应用的urls.py文件管理
    #我们只需要在主项目中的urls.py文件中include每一个子应用的urls.py文件袋路径
    #path('子应用主url（随意取）', include('子应用的urls.py文件路径')),
    path('', include('book.urls')),
    path('echart/', include('smart_chart.echart.urls')),
    path('', RedirectView.as_view(url='echart/index/')),  # 首页,可自定义路由
]
