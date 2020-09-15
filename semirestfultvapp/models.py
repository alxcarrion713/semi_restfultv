from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['t'])<2:
            errors["t"]= "Title should be at least 2 characters"
        if len(postData['nw'])<3:
            errors["nw"]= "Network should be at least 3 characters"
        if len(postData['desc'])<10:
            errors['desc']="Description should be at least 10 characters"
        return errors
  



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects= ShowManager()
