# -*- coding :utf-8  -*-
# !/usr/bin/python3
from django.shortcuts import render
from .models import Article, Category, Tag, Link, User, Banner, Tui
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import base64

# Create your views here.


def index(request):
    return render(request, "index.html", locals())


def about(request):
    return render(request,'about.html', locals())


def index(request):
    #对Article进行声明并实例化，然后生成对象allarticle
    allarticle = Article.objects.all().order_by('-id')[0:6]
    list = Article.objects.all()
    remen = Article.objects.filter(tui__id=1)[:6]
    tui = Article.objects.filter(tui__id=1)[:3]

    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    #把查询到的对象，封装到上下文
    context = {
        'allarticle': allarticle,
        'remen': remen,
        'tui':tui
    }
    #把上传文传到模板页面index.html里
    return render(request, 'index.html', context)


#列表页
def list(request,lid):
    pass


#内容页
def show(request,sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 导航上的分类
    tags = Tag.objects.all()  # 右侧所有标签
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())


#标签页
def tag(request, tag):
    pass


# 搜索页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)  # 获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())

# def search(request):
#     return render(request,'search.html', locals())
#
#
# def result(request):
#     key = request.GET['base64']
#     if not key:
#         message = u'请输入搜索内容'
#         return render(request, 'result.html',{'message': message})
#     else:
#         decodestr1 = base64.b64decode(key)
#         decodestr2 = decodestr1.decode()
#         message = u'base64解码结果:' + decodestr2
#         return render(request, 'result.html', {'message': message})
