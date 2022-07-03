from django.db import models

# Create your models here.
class Todo(models.Model):
    Added_date=models.DateField(auto_now=True)
    due=models.DateField(null=True)
    item=models.CharField(max_length=200)
    #reated=models.DateTimeField
    class Meta:
        verbose_name_plural='Todo'
    def __str__(self):
        return  self.item
