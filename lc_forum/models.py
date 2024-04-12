from django.db import models
from django.contrib.auth.models import User
from machina.apps.forum.models import Forum  # 导入具体的 Forum 模型

class ForumAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)  # 使用具体的 Forum 模型
    can_access = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'forum')
