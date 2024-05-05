from django.db import models

class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=50)
    date=models.DateField()
    image=models.ImageField(upload_to="Shop/images",default="")

    def __str__(self):
        return self.product_name

class contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    query=models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class order(models.Model):
    itemsjson=models.CharField(max_length=5000,default="")
    order_id=models.AutoField(primary_key=True)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    phone=models.IntegerField()

    def __str__(self):
        return self.name
    
class updateorder(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=500)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."