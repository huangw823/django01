from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requset):

    return HttpResponse('index')


from book.models import BookInfo
###############增加数据#################################

#方式一
book=BookInfo( #创建模型对象（一个对象就是一行数据）
    name="钢铁是怎样炼成的", #字段赋值
    pub_date='2000-5-15'
)
book.save() #将对象数据保存到数据库

#方法二：使用模型类的objects对象实现增删改查（方便）
BookInfo.objects.create(
    name="爱情买卖", #字段赋值
    pub_date='2000-5-15'
)

###############修改数据#################################

#方式一：根据获得表数据对象，修改属性(字段)，再重新保存到数据库
book=BookInfo.objects.get(id=6)
book.name='爬虫入门'
book.save()

#方式二：使用模型类的objects对象的表过滤实现改（方便）
#filter 过滤
BookInfo.objects.filter(id=6).updata(name='Linux')

###############删除数据#################################

#方式一：使用模型类的objects对象get().delete()删除,
# 返回影响表几条数据
BookInfo.objects.get(id=6).delete()

#方式二：使用模型类的objects对象filter().delete()删除
BookInfo.objects.filter(id=5).delete()

###############查询数据#################################

#基础条件查询
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
BookInfo.objects.get(id=1)
# all查询多个结果。
BookInfo.objects.all()
# count查询结果数量。
BookInfo.objects.count()

#过滤条件查询

# 查询编号为1的图书
BookInfo.objects.filter(id=1)
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=(1,3,5))
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
#查询编号不等于3的图书
BookInfo.objects.exclude(id=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')



###############F对象#################################
from  django.db.models import F
# 例：查询阅读量大于等于评论量的图书。
BookInfo.objects.filter(readcount__gte=F('commentcount'))
# 可以在F对象上使用算数运算。
# 例：查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)

###############并且查询#################################

#方式一：
BookInfo.objects.filter(readcount__gte=10,id__gte=2)

#方式二：
BookInfo.objects.filter(readcount__gte=10).filter(id__gte=2)

###############Q对象#################################
from django.db.models import Q
#例：查询阅读量大于20的图书，改写为Q对象如下。
BookInfo.objects.filter(Q(readcount__gte=20))
#Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或。
#例：查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(readcount__gte=20)&Q(id__lt=3))

#Q对象前可以使用~操作符，表示非not。
#例：查询编号不等于3的图书。
BookInfo.objects.filter(~Q(id=3))

###############聚合函数和排序函数#################################
#聚合函数
# 使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg平均，Count数量，Max最大，Min最小，Sum求和，被定义在django.db.models中。
from django.db.models import Max,Sum
# 例：查询图书的总阅读量。
BookInfo.objects.aggregate(Max('readcount'))
# 使用count时一般不使用aggregate()过滤器。
# 例：查询图书总数。
BookInfo.objects.count()

#排序函数
BookInfo.objects.all().order_by('readcount')

###############级联查询#################################
#1.关联查询
##1.1 一对多
book=BookInfo.objects.get(id=1) #拿到一本书
book.peopleinfo_set.all() #查看书的所有人物
##1.2 多对一
from book.models import PeopleInfo
peo=PeopleInfo.objects.get(id=1) #拿到人物
peo.book.name  #人物对象的字段book（外键）就是book表模型对象,就可以正常使用book表的模型对象的属性
##访问一对应的模型类关联对象的id语法:
peo=PeopleInfo.objects.get(id=1) #拿到人物
peo.book_id

###############关联过滤查询#################################

# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name='郭靖') #拿到郭靖在拿图书
# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')
# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)