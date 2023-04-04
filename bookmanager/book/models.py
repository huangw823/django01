from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """书籍模型类"""
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    """人物列表信息的模型类"""
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
