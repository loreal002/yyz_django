from django.db import models

# Create your models here.
#发布会表
 # 发布会标题
  # 参加人数
 # 状态
  # 地址
 # 发布会时间
 # 创建时间（自动获取当前时间）
class Event(models.Model):
    name = models.CharField(max_length=100) #发布会标题
    limit = models.IntegerField()  #发布会人数
    status = models.BooleanField() # 发布会状态
    address = models.CharField(max_length=200)  #地址
    start_time = models.DateTimeField('event time') #发布会时间
    create_time = models.DateTimeField(auto_now=True)# 自动获取当前时间

    def __str__(self):
        return self.name


# 关联发布会 id
class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)  #关联发布会id
    realname = models.CharField(max_length=64) # 姓名
    phone = models.CharField(max_length=16) # 手机号
    email = models.EmailField() # 邮箱
    sign = models.BooleanField() # 签到状态
    create_time = models.DateTimeField(auto_now=True) # 创建时间（自动获取当前时间）

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname

# class Reporter(models.Model):
#     full_name = models.CharField(max_length=70)
#
#     def __str__(self):
#         return self.full_name
#
# class Article(models.Model):
#     pub_date = models.DateField()
#     headline = models.CharField(max_length=200)
#     content = models.TextField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.headline
#
# class Type(models.Model):
#     id = models.AutoField(primary_key=True)
#     type_name = models.CharField(max_length=20)
#
#
# class Product(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     weight = models.CharField(max_length=20)
#     size = models.CharField(max_length=20)
#     type = models.ForeignKey(Type)


#Guest.objects.create(realname='andy',phone=13611001101,email='andy@mail.com',sign=False,event_id=3)


