from django.utils.deprecation import MiddlewareMixin

class myTest(MiddlewareMixin):
    """测试中间件"""
    def process_request(self,request):
        """请求前中间件"""
        print('111111111请求前中间件')

    def process_response(self,request,response):
        """响应后中间件"""
        print('1111111111响应后中间件')

        return response
    from book import views

    def process_view(self,request,view_func,view_args,view_kwargs):
        """视图前中间件"""
        """
            :param request: 浏览器发来的 request 请求对象
            :param view_func: 将要执行的视图函数的名字
            :param view_args: 将要执行的视图函数的位置参数
            :param view_kwargs: 将要执行的视图函数的关键字参数
            :return:
        """
        print('111111111视图前中间件')
