import os
from django.db import models
from django.db.models.signals import post_save, pre_save
from .utils.importee import file_inputer
import threading
import json

# Create your models here.


class Document(models.Model):
      description = models.CharField(max_length=255, blank = True)
      document = models.FileField(upload_to='documents/%Y-%m-%d/')      
      uploaded_at = models.DateTimeField(auto_now_add=True)
      def filename(self):
         return os.path.basename(self.document.name)
      def __str__(self):
         return f"{os.path.basename(self.document.name)} with id {self.pk}"

def save_post(sender, instance, **kwargs):
    process_document(instance.pk)
    #proc = threading.Thread(target=process_document, args=(instance.pk,))
    #proc.start()

class Validate(models.Model):
    document = models.OneToOneField(Document,related_name='validate', on_delete=models.CASCADE, primary_key=True)
    names_list = models.TextField()
    csv_list = models.TextField()
    def __str__(self):
        return f"{os.path.basename(self.document.document.name)} with id {self.pk}"

def process_document(document_id):
    document = Document.objects.get(pk=document_id)
    filepath = document.document.path
    names, csv_list = file_inputer(filepath)
    names_json =json.dumps(names)
    csv_json_list = json.dumps(csv_list)
    Validate.objects.create(document=document, 
                            names_list = names_json,
                            csv_list = csv_json_list) 


post_save.connect(save_post, sender=Document, weak=False)    