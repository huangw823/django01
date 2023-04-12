from django.db import models

# Create your models here.

class BookInfo(models.Model): #模型类对应表
    """书籍类"""
    name=models.CharField(max_length=32,verbose_name='数据名',unique=True)
    pub_date=models.DateField(verbose_name='发布日期',null=True)
    readcount=models.IntegerField(verbose_name='阅读量',default=0)
    commentcount=models.IntegerField(verbose_name='评论数',default=0)
    is_delete=models.BooleanField(default=False,verbose_name='是否下架')

    def __str__(self):
        return self.name
    class Meta:
        db_table='bookInfo' #指定数据表名，不用django默认的表名设置
        verbose_name='书籍管理' #站点admin使用

class PeopleInfo(models.Model):
    """人物表"""
    name=models.CharField(verbose_name='人物名',max_length=10,unique=True)
    GENDER_CHOICES=(
        (1,'男'),
        (2,'女')
    )
    gender=models.SmallIntegerField(choices=GENDER_CHOICES,verbose_name='性别')
    description=models.CharField(max_length=300,verbose_name='描述信息',null=True)
    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除')
    book =models.ForeignKey(BookInfo,models.CASCADE,verbose_name='书籍') #外键

    def __str__(self):
        return self.name

    class Meta:
        db_table='peopleInfo'
        verbose_name='人物'
