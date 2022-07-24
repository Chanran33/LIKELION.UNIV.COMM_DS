from django.db import models

# Create your models here.
class Account(models.Model):
    user_email = models.CharField(max_length = 200, null=True)
    user_name = models.CharField(max_length = 100, default='', null=True)
    github_name = models.CharField(max_length = 200, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_readme = models.TextField(null=True, default=' ')
    
    def __str__(self):
        return self.user_name