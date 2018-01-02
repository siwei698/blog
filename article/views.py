# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from article.models import Tag, Category, Article, Comment, Contact

from .forms import BasicForm

# Create your views here.
class HomepageView(View):
    def get(self, request):
        return render(request,'homepage.html')
#def homepage(request):
#    return render(request, 'homepage.html')

def secondpage(request):
    return render(request, 'secondpage.html')
def articlepage(request):
    return render(request, 'articlepage.html')
#上面均为静态网页的部分，测试用

#首页
def osw_mainpage(request):
    all_tags = Tag.objects.all()
    all_article = Article.objects.all()
    recent_article = all_article[::-1][:6]
    return render(request, 'osw_mainpage.html',{
        'all_tags':all_tags,
        'recent_article': recent_article
    })

#分类导航页
def osw_articlelist(request, leixing):
    '''
    if leixing == "all":
        articlefilter = Article.objects.all()[::-1]
        mybreadcrumb = "全部文章"
    elif leixing == "net":
        #articlefilter = Article.objects.filter(category_id=4)
        articlefilter = Article.objects.filter(category__name = "计算机网络")[::-1]
        mybreadcrumb = "计算机网络"
    elif leixing == "qdkf":
        articlefilter = Article.objects.filter(category__name= "前端开发")[::-1]
        mybreadcrumb = "前端开发"
    elif leixing == "hdkf":
        articlefilter = Article.objects.filter(category__name="后端开发")[::-1]
        mybreadcrumb = "后端开发"
    elif leixing == "sf":
        articlefilter = Article.objects.filter(category__name="算法与数据结构")[::-1]
        mybreadcrumb = "算法与数据结构"
    elif leixing == "others":
        articlefilter = Article.objects.filter(category__name="其它文章")[::-1]
        mybreadcrumb = "其它文章"
        '''
    all_tags = Tag.objects.all()
    if int(leixing) == 0:
        articlefilter = Article.objects.all()[::-1]
        mybreadcrumb = "全部文章"
    elif int(leixing) in [1,2,3,4,5]:
        articlefilter = Article.objects.filter(category_id = int(leixing))[::-1]
        mybreadcrumb = Category.objects.get(id = int(leixing)).name
#下面是分页操作1、基本功能
    paginator = Paginator(articlefilter, 6)
    page = request.GET.get('page')
    try:
        article_paginator = paginator.page(page)
    except PageNotAnInteger:
        article_paginator = paginator.page(1)
    except EmptyPage:
        article_paginator = paginator.page(paginator.num_pages)
#2、页数过多时只显示指定页数
    current_page = article_paginator.number
    if paginator.num_pages > 6:
        if current_page + 5 <= paginator.num_pages:
            tmp = []
            for i in range(current_page, current_page+6):
                tmp.append(i)
            my_paginator_numbers = tmp
        else:
            tmp = []
            for i in range(paginator.num_pages - 5, paginator.num_pages + 1):
                tmp.append(i)
            my_paginator_numbers = tmp
    else:
        my_paginator_numbers = article_paginator.paginator.page_range

    return render(request, 'osw_categorypage.html', {
        #'articlefilter':articlefilter,
        'all_tags':all_tags,
        'mybreadcrumb':mybreadcrumb,
        'article_paginator':article_paginator,
        'my_paginator_numbers':my_paginator_numbers
    })

#标签分类导航页
def osw_taglist(request, biaoqian):
    '''
    if leixing == "all":
        articlefilter = Article.objects.all()[::-1]
        mybreadcrumb = "全部文章"
    elif leixing == "net":
        #articlefilter = Article.objects.filter(category_id=4)
        articlefilter = Article.objects.filter(category__name = "计算机网络")[::-1]
        mybreadcrumb = "计算机网络"
    elif leixing == "qdkf":
        articlefilter = Article.objects.filter(category__name= "前端开发")[::-1]
        mybreadcrumb = "前端开发"
    elif leixing == "hdkf":
        articlefilter = Article.objects.filter(category__name="后端开发")[::-1]
        mybreadcrumb = "后端开发"
    elif leixing == "sf":
        articlefilter = Article.objects.filter(category__name="算法与数据结构")[::-1]
        mybreadcrumb = "算法与数据结构"
    elif leixing == "others":
        articlefilter = Article.objects.filter(category__name="其它文章")[::-1]
        mybreadcrumb = "其它文章"
        '''
    all_tags = Tag.objects.all()
    mybreadcrumb = Tag.objects.get(id=int(biaoqian)).name
    articlefilter = Article.objects.filter(tags__id = int(biaoqian))[::-1]
    # 下面是分页操作1、基本功能
    paginator = Paginator(articlefilter, 6)
    page = request.GET.get('page')
    try:
        article_paginator = paginator.page(page)
    except PageNotAnInteger:
        article_paginator = paginator.page(1)
    except EmptyPage:
        article_paginator = paginator.page(paginator.num_pages)
    # 2、页数过多时只显示指定页数
    current_page = article_paginator.number
    if paginator.num_pages > 6:
        if current_page + 5 <= paginator.num_pages:
            tmp = []
            for i in range(current_page, current_page + 6):
                tmp.append(i)
            my_paginator_numbers = tmp
        else:
            tmp = []
            for i in range(paginator.num_pages - 5, paginator.num_pages + 1):
                tmp.append(i)
            my_paginator_numbers = tmp
    else:
        my_paginator_numbers = article_paginator.paginator.page_range

    return render(request, 'osw_categorypage.html', {
        # 'articlefilter':articlefilter,
        'all_tags':all_tags,
        'mybreadcrumb': mybreadcrumb,
        'article_paginator': article_paginator,
        'my_paginator_numbers': my_paginator_numbers
    })

#文章详情页
def osw_article(request, article_id):
    all_tags = Tag.objects.all()
    myarticle = Article.objects.get(id = article_id)
    leixing = Category.objects.get(id = myarticle.category_id)
    myarticle.clicked = myarticle.clicked + 1
    myarticle.save()
    max_id = len(Article.objects.all())
    if myarticle.id == 1:
        previous_id = max_id
        next_id = myarticle.id + 1
    elif myarticle.id == max_id:
        next_id = 1
        previous_id = myarticle.id - 1
    else:
        next_id = myarticle.id + 1
        previous_id = myarticle.id - 1
    nextarticle = Article.objects.get(id = next_id)
    previousarticle = Article.objects.get(id = previous_id)
    return render(request, 'osw_articlepage.html',{
        'all_tags':all_tags,
        'myarticle':myarticle,
        'leixing':leixing,
        'nextarticle':nextarticle,
        'previousarticle':previousarticle
    })

#表单（主页）
def Contact_function(request):
    if request.method =='POST':
        contact_form = BasicForm(request.POST)
        if contact_form.is_valid():
            user_name = request.POST.get("username", "")
            mail_box = request.POST.get("mailbox", "")
            me_ssage = request.POST.get("message", "")
            contact_message = Contact()
            contact_message.name = user_name
            contact_message.email = mail_box
            contact_message.content = me_ssage
            contact_message.save()
            return HttpResponseRedirect('/#contact-me')
        else:
            return HttpResponseRedirect('/#contact-me')

#表单二（文章页）
def Comment_function(request, article_id):
    if request.method =='POST':
        comment_form = BasicForm(request.POST)
        if comment_form.is_valid():
            comment_article = Article.objects.get(id = int(article_id))
            user_name = request.POST.get("username", "")
            mail_box = request.POST.get("mailbox", "")
            me_ssage = request.POST.get("message", "")
            comment_message = Comment()
            comment_message.article = comment_article
            comment_message.name = user_name
            comment_message.email = mail_box
            comment_message.content = me_ssage
            comment_message.save()
            return HttpResponseRedirect('/article/'+article_id+'#contact-me')
        else:
            return HttpResponseRedirect('/article/'+article_id+'#contact-me')

#站内搜索
def Search_function(request):
    all_articles = Article.objects.all()
    search_keywords = request.GET.get('keywords', "")
    search_articles = []
    if search_keywords:
        all_articles = all_articles.filter(Q(title__icontains=search_keywords)
                                           |Q(abstract__icontains=search_keywords)
                                           |Q(content__icontains=search_keywords)
                                           |Q(category__name__icontains=search_keywords)
                                           |Q(tags__name__icontains=search_keywords))
        for item in all_articles:
            if item not in search_articles:
                search_articles.append(item)

    # 下面是分页操作1、基本功能
    paginator = Paginator(search_articles, 10)
    page = request.GET.get('page')
    try:
        article_paginator = paginator.page(page)
    except PageNotAnInteger:
        article_paginator = paginator.page(1)
    except EmptyPage:
        article_paginator = paginator.page(paginator.num_pages)
    # 2、页数过多时只显示指定页数
    current_page = article_paginator.number
    if paginator.num_pages > 6:
        if current_page + 5 <= paginator.num_pages:
            tmp = []
            for i in range(current_page, current_page + 6):
                tmp.append(i)
                my_paginator_numbers = tmp
        else:
            tmp = []
        for i in range(paginator.num_pages - 5, paginator.num_pages + 1):
            tmp.append(i)
        my_paginator_numbers = tmp
    else:
        my_paginator_numbers = article_paginator.paginator.page_range
    return render(request, 'osw_search.html',{
       # 'search_articles':search_articles,
        'article_paginator': article_paginator,
        'my_paginator_numbers': my_paginator_numbers,
        'search_keywords':search_keywords
    })

#学习资源导航
def osw_resources(request):
    return render(request, "osw_resources.html")

#在线案例导航
def osw_onlinetest(request):
    return render(request, "osw_onlinetest.html")
