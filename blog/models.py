from django.db import models


class blogpost(models.Model):
    title = models.CharField(max_length=100, default='2019-07-13')
    pub_date = models.DateField(default='2019-07-13')
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.text[:100]
    def __str__(self):
        return self.title  #This is what Django looks to call it


# Create your models here.
