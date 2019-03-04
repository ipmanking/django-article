#coding;utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length = 32,verbose_name = "文章标题")
    author = models.CharField(max_length = 32,verbose_name = "文章作者")
    time = models.DateField(verbose_name = "发表日期")
    content = RichTextUploadingField(verbose_name = "文章内容")
    destription = RichTextUploadingField(verbose_name = "文章描述")
    picture = models.ImageField(upload_to = "images",verbose_name = "文章图片")

# Create your models here.
