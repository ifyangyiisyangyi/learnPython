from django.db import models
from django.utils import timezone


class ArticleColumn(models.Model):
    """
    文章栏目的 Model
    """
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)

    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title