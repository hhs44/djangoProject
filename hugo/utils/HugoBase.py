import os

from settings import HUGO_PATH


class HugoBase(object):
    def __init__(self, blog_name):
        self.hugo_path = HUGO_PATH
        self.blog_name = blog_name

    def create_post(self):
        cmd = "hugo new post/%s/index.md" % self.blog_name
        os.chdir(self.hugo_path)
        os.system(cmd)
