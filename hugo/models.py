import os

from django.db import models
# Create your models here.
from mdeditor.fields import MDTextField

from hugo.utils.settings import POST_PATH, ABOUT_PATH, ABOUT_TOP


class Base(models.Model):
    title = models.CharField("标题", max_length=255, default="")
    description = models.CharField("简介", max_length=255, blank=True, default="")
    date = models.DateTimeField("时间", default="")
    image = models.CharField("封面", max_length=255, blank=True, default="")
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

    def save(self, *args, **kwargs):
        if not os.path.exists(POST_PATH + "/" + self.title):
            os.makedirs(POST_PATH + "/" + self.title)
        with open("%s/%s/index.md" % (POST_PATH, self.title), mode="w", encoding='utf-8') as f:
            f.write('+++\ntitle="%s"\n' % self.title)
            f.write('description="%s"\n' % self.description)
            f.write('date="%s"\n' % self.date)
            f.write('image="%s"\n' % self.image)
            f.write('tags=[%s]\n' % self.tags)
            f.write('categories=[%s]\n' % self.categories)
            f.write('series=[%s]\n' % self.series)
            f.write('aliases=[%s]\n' % self.aliases)
            f.write("+++\n")
            f.write(self.content)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "博客列表"


class About(Base):
    md_date = models.DateTimeField("修改日期", auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        aliases = ""
        for i in self.aliases.split(","):
            aliases += " - %s\n" % i
        with open(ABOUT_PATH, mode="w", encoding='utf-8') as f:
            f.write(ABOUT_TOP % (
                self.title, self.description, self.date, aliases, self.md_date))
            f.write(self.content)
        super(About, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "关于"
