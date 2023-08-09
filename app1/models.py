from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,null=True,blank=True)
    email = models.CharField(max_length=122,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    date = models.DateField(null=True,blank=True,auto_now_add=True)

    def __str__(self):
        return self.name