# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField("分类名", max_length=30)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField("标签名", max_length=16)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    """
    文章
    """
    title = models.CharField("标题", max_length=32)
    author = models.CharField("作者", max_length=16)
    abstract = models.TextField("文章简介", null=True)
    #content = models.TextField("文章内容", null=True)
    #下面的config_name好像没有起作用
    content = RichTextUploadingField("文章内容", config_name="default_ckeditor" ,null=True)
    created = models.DateTimeField("创建时间", auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    clicked = models.IntegerField("点击量", default=0)
    picture = models.ImageField("图片", upload_to='upload_img/%Y/%m', default='upload_img/orange.jpg')

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    """
    评论
    """
    article = models.ForeignKey(Article, verbose_name="文章")
    name = models.CharField("称呼", max_length=16)
    email = models.EmailField("邮箱")
    content = models.CharField("评论内容", max_length=140)
    created = models.DateTimeField("评论时间", auto_now_add=True)

    def __unicode__(self):
        return self.content

class Contact(models.Model):
    """
    联系我
    """
    name = models.CharField("称呼", max_length=16)
    email = models.EmailField("邮箱")
    content = models.CharField("留言", max_length=140)
    created = models.DateTimeField("提交时间", auto_now_add=True)

