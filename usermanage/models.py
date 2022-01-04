from django.db import models

# Create your models here.

# 厂商
class Factory(models.Model):
    fname = models.CharField("厂商名",max_length=40,unique=True)
    finfo = models.CharField("厂商信息",max_length=1000,null=True,blank=True) #允许为空
    faddress = models.CharField("厂商地址",max_length=500,null = True,blank=True) # 允许为空
    flogo = models.CharField("厂商logo",max_length=500,null = True,blank=True)

    class Meta:
        db_table = "FACTORY"
        verbose_name = "厂商数据表"

# 用户
class User(models.Model):
    username = models.CharField("用户名",max_length = 30,unique=True)
    password = models.CharField('密码',max_length = 40)
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    updated_time = models.DateTimeField('更新时间',auto_now=True)
    is_active = models.BooleanField('是否活跃',default=False) # 这个表示这个用户是否合法
    is_check = models.BooleanField('是否检查',default=False) # 这个表示这个用户是否检查过

    # 活跃且检查过-》有效用户
    # 不活跃且没检查过-》需要检查
    # 不活跃检查过-》检查过不合法 或者注销了用户

    # 保存生产许可证的
    createimg = models.ImageField('生产许可证',null = True,upload_to='userimgs/')

    # 厂商的外键,默认为空
    factory = models.ForeignKey(Factory,on_delete=models.CASCADE,null = True,blank=True)

    class Meta:
        db_table = "USER"
        verbose_name = "用户数据表"

    def __str__(self):
        return "username %s" % self.username