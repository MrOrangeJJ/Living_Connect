from django.db import models

# Create your models here.
class AuthorizedEmail(models.Model):
    email = models.EmailField(unique=True)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return self.email