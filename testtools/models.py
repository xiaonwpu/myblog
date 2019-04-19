# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.jpg', max_length=200, verbose_name='头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='qq')
    phone = models.CharField(max_length=10, unique=True, blank=True, null=True, verbose_name='电话号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username


# class Gameinterface(models.Model):
#     url = models.CharField(max_length=50, verbose_name='URL')
#     method = models.CharField(max_length=10, verbose_name='方法')
#     time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')
#     exp = models.CharField(max_length=999,verbose_name='接口描述')
#     User = models.ForeignKey(User, verbose_name='用户')
#
#     class Meta:
#         verbose_name = '接口文档'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.method
#
#
# class article(models.Model):
#     title = models.CharField(max_length=50, verbose_name='文章标题')
#     desc = models.CharField(max_length=100, verbose_name='文章描述')
#     content = models.TextField(verbose_name='文章内容')
#     data_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
#     click_counts = models.IntegerField(default=0, verbose_name='点击次数')
#     is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
#
#     class Meta:
#         verbose_name = '技术文章'
#         verbose_name_plural = verbose_name
#         ordering = ['-data_time']
#
#     def __str__(self):
#         return self.title
# 文章分类
class Category(models.Model):
    name = models.CharField('博客分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐位
class Tui(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=70)
    excerpt = models.TextField(verbose_name='摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 使用外键关联标签表与标签是多对多关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    body = UEditorField('内容', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    """
    文章作者，这里User是从django.contrib.auth.models导入的。
    这里我们通过 ForeignKey 把文章和 User 关联了起来。
    """
    views = models.PositiveIntegerField(verbose_name='阅读量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)

    created_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title


# Banner
class Banner(models.Model):
    text_info = models.CharField(verbose_name='标题', max_length=50, default='')
    img = models.ImageField(verbose_name='轮播图', upload_to='banner/')
    link_url = models.URLField(verbose_name='图片链接', max_length=100)
    is_active = models.BooleanField(verbose_name='是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 友情链接
class Link(models.Model):
    name = models.CharField(verbose_name='链接名称', max_length=20)
    linkurl = models.URLField(verbose_name='网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'

