from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="images", null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



