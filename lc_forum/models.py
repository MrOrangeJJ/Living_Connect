from django.db import models
from django.contrib.auth.models import User
from machina.apps.forum.models import Forum

class ForumAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    can_access = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'forum')
