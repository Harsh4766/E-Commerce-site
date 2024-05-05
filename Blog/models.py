from django.db import models

# Create your models here.

class blogposttt(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    head1=models.CharField(max_length=50)
    chead1=models.CharField(max_length=500)
    head2=models.CharField(max_length=50)
    chead2=models.CharField(max_length=500)
    head3=models.CharField(max_length=50)
    chead3=models.CharField(max_length=500)
    publish_date=models.DateField()
    thumbnail=models.ImageField(upload_to="Blog/images",default="")


    def __str__(self) -> str:
        return self.title
