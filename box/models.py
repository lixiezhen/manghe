from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Man_box(models.Model):
    """男生盲盒表"""
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='发表者')
    name = models.CharField(verbose_name="姓名", max_length=16)
    age = models.IntegerField(verbose_name="年龄")
    gender = models.CharField(verbose_name="性别",max_length=1, default='男',blank=True)
    school = models.ForeignKey('School',verbose_name="校名",on_delete=models.DO_NOTHING)
    area = models.CharField(verbose_name="地区", max_length=32, null=True)
    qq = models.IntegerField(verbose_name="QQ号", null=True)
    mobile = models.CharField(verbose_name="电话号码", max_length=32, null=True)
    email = models.EmailField(verbose_name="邮箱", null=True)
    intro = RichTextField(verbose_name="个人介绍", null=True)
    create_time = models.DateTimeField(verbose_name='注册时间', null=True, auto_now_add=True)
    photo = models.ImageField(verbose_name='照片', blank=True, )
    cover = models.ImageField(verbose_name='封面', blank=True, )
    def __str__(self):
        return "user:{}".format(self.user.username)
class Woman_box(models.Model):
    """女士盲盒表"""
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='发表者')
    name = models.CharField(verbose_name="姓名", max_length=16)
    age = models.IntegerField(verbose_name="年龄")
    gender = models.CharField(verbose_name="性别", max_length=1,default='女',blank=True)
    school = models.ForeignKey('School',verbose_name="校名",on_delete=models.DO_NOTHING)
    area = models.CharField(verbose_name="地区", max_length=32, null=True)
    qq = models.IntegerField(verbose_name="QQ号", null=True)
    mobile = models.CharField(verbose_name="电话号码", max_length=32, null=True)
    email = models.EmailField(verbose_name="邮箱", null=True)
    intro = RichTextField(verbose_name="个人介绍", null=True)
    create_time = models.DateTimeField(verbose_name='注册时间', null=True, auto_now_add=True)
    photo = models.ImageField(verbose_name='照片',upload_to='static/images/box', blank=True, )
    cover = models.ImageField(verbose_name='封面', blank=True, )
    def __str__(self):
        return "user:{} school:{}".format(self.user.username,self.school.name)
class Cltwoman_Box(models.Model):
    Cltbox = models.ForeignKey(Woman_box,on_delete=models.CASCADE,related_name='clt_womanbox')
    who_clt = models.ForeignKey(User, on_delete=models.CASCADE)
    clt_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
class Cltman_Box(models.Model):
    Cltbox = models.ForeignKey(Man_box,on_delete=models.CASCADE,related_name='clt_womanbox')
    who_clt = models.ForeignKey(User, on_delete=models.CASCADE)
    clt_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
class School(models.Model):
    name = models.CharField(max_length=32, verbose_name='学校')
    def __str__(self):
        return self.name


class Comment(models.Model):
    box1 = models.ForeignKey(Woman_box, on_delete=models.DO_NOTHING, related_name='评论盲盒',default=None, null=True)
    box2 = models.ForeignKey(Man_box, on_delete=models.DO_NOTHING, related_name='评论盲盒', default=None, null=True)
    body = models.TextField(verbose_name='评论内容',null=True)
    commentator = models.CharField(max_length=90)
    pre_comment = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True,
                                    verbose_name='父评论id')

    def __str__(self):
        return "Comment by {0} on {1} or {2}".format(self.commentator.username, self.box1,self.box2)