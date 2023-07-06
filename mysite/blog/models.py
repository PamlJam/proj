from django.db import models

class Article(models.Model):
# 文章模型
    title = models.CharField(max_length = 60)
    # 标题，最多输入 60 字符
    text = models.CharField(max_length = 100000)
    # 正文
    pub_date = models.DateTimeField('date published')
    # 发布日期