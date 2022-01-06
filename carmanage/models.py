from django.db import models
from usermanage.models import Factory
# Create your models here.

# 车型
class Series(models.Model):
    #车型名字可以重复,
    sname = models.CharField("车型名称",max_length=300)
    sprice = models.DecimalField("指导价格",max_digits=10,decimal_places=2,default=0.0)
    stype = models.CharField("车型类型", max_length=100,null = True,blank = True)
    is_active = models.BooleanField("是否活跃",default=True)
    sinfo = models.TextField("车型信息",null=True,blank = True) #先放个link
    created_time = models.DateTimeField('登记时间', auto_now_add=True)
    simage = models.CharField("车型图片",max_length=100,null = True,blank=True) # 放车型图片的link
    # 外键厂商
    factory = models.ForeignKey(Factory,on_delete=models.CASCADE) # 必须有厂商

    class Meta:
        db_table = "SERIES"
        verbose_name = "车型数据表"

class Sale(models.Model):
    number = models.IntegerField("销售数量",default=0)
    # 保存的时候用str来转换
    # str = '2020-03'
    # d1 = datetime.datetime.strtime(str,'%Y-%m')
    # d1 = d1.date() # 转为date类型
    date = models.DateField("销售月份")#

    # 外键车型
    series = models.ForeignKey(Series,on_delete=models.CASCADE)

    class Meta:
        db_table = "SALES"
        verbose_name = "销量数据表"