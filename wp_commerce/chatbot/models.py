from django.db import models


class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    flow = models.CharField(max_length=100,blank=True)
    wa_id = models.CharField(blank=False,unique=True,max_length=17)
    wa_name = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    catalog_id = models.CharField(max_length=100,blank=True)
    curr = models.CharField(max_length=100,blank=True)
    item_price = models.CharField(max_length=100,blank=True)
    product_id = models.CharField(max_length=100,blank=True)
    quantity = models.CharField(max_length=100,blank=True)
    wa_id = models.CharField(max_length=18,blank=False)
    msg_id = models.CharField(max_length=110,unique=True)
    msg = models.TextField(default="")
    interactive_id = models.CharField(max_length=150,default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    msg_type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    mime_type = models.CharField(max_length=30,default="")
    media_id = models.CharField(max_length=60,default="")
    img_path = models.CharField(max_length=60,default="") 