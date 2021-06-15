from django.db import models

# Create your models here.
class FilesUpload(models.Model):
    file = models.FileField()
#     def __str__(self):
#         return self.file

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=FilesUpload)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)
