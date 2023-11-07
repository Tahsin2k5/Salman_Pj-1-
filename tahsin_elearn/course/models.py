from django.db import models
from elearn.models import Categories
class courses(models.Model):
    id = models.AutoField(primary_key=True)
    cat_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    
    description = models.TextField()
    fee = models.IntegerField()
    discount = models.IntegerField()
    module = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to ="images/")
# Create your models here.
