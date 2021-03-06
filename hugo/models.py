import os
import re

from django.db import models
# Create your models here.
from mdeditor.fields import MDTextField

from hugo.utils.settings import POST_PATH, ABOUT_PATH, ABOUT_TOP, IMAGE_PATH, POST_PAGE_PATH, INDEX_IMAGE_PATH


class Base(models.Model):
    title = models.CharField("标题", max_length=255, default="")
    description = models.CharField("简介", max_length=255, blank=True, default="")
    date = models.DateTimeField("时间", default="")
    image = models.ImageField("封面", blank=True, default="")
    tags = models.CharField("标签", max_length=255, blank=True, default="")
    categories = models.CharField("分类", max_length=255, blank=True, default="")
    series = models.CharField("series", max_length=255, blank=True, default='"Themes Guide"')
    aliases = models.CharField("aliases", max_length=255, blank=True, default='"migrate-from-jekyl"')
    other = models.CharField("其他", max_length=255, blank=True, default="")
    content = MDTextField("正文", default="", blank=True)

    class Meta:
        abstract = True


class Blog(Base):

    def __str__(self):
        return self.title

    def cover(self, field):
        tmp = ""
        for i in field.split(","):
            tmp += '"' + i + '",'
        return tmp

    def save(self, *args, **kwargs):
        categories = self.cover(self.categories)
        tags = self.cover(self.tags)
        content = self.content
        if not os.path.exists(POST_PATH + "\\" + self.title):
            os.makedirs(POST_PATH + "\\" + self.title)
        if self.image:
            os.system("xcopy /y %s %s" % (INDEX_IMAGE_PATH + "\\" + str(self.image), POST_PATH + '\\"' + self.title + '"'))
        image_re = r'![\[].*?[]][(](.*?)[)]'
        ls = re.findall(image_re, self.content, re.M)
        for i in ls:
            image_name = i.split("\\")[-1]
            print(i, image_name)
            os.system("xcopy /y %s %s" % (IMAGE_PATH + "\\" + image_name, POST_PATH + '\\"' + self.title + '"'))
            content = content.replace(i, image_name)
        with open("%s\\%s\\index.md" % (POST_PATH, self.title), mode="w", encoding='utf-8') as f:
            f.write('+++\ntitle="%s"\n' % self.title)
            f.write('description="%s"\n' % self.description)
            f.write('date="%s"\n' % self.date)
            f.write('image="%s"\n' % self.image)
            f.write('tags=[%s]\n' % tags)
            f.write('categories=[%s]\n' % categories)
            f.write('series=[%s]\n' % self.series)
            f.write('aliases=[%s]\n' % self.aliases)
            f.write("+++\n")
            f.write(content)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "博客列表"


class About(Base):
    md_date = models.DateTimeField("修改日期", auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        content = self.content
        if self.image:
            os.system("xcopy /y %s %s" % (INDEX_IMAGE_PATH + "\\" + str(self.image), POST_PATH + '\\"' + self.title + '"'))
        aliases = ""
        for i in self.aliases.split(","):
            aliases += " - %s\n" % i
        image_re = r'![\[].*?[]][(](.*?)[)]'
        ls = re.findall(image_re, self.content, re.M)
        for i in ls:
            image_name = i.split("\\")[-1]
            os.system("xcopy /y %s %s" % (IMAGE_PATH + "\\" + image_name, POST_PAGE_PATH + "\\'" + self.title + "'"))
            content = content.replace(i, image_name)
        with open(ABOUT_PATH, mode="w", encoding='utf-8') as f:
            f.write(ABOUT_TOP % (
                self.title, self.description, self.date, aliases, self.md_date))
            f.write(content)
        super(About, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "关于"
