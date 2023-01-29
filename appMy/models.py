from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Brand(models.Model):
    title = models.CharField(("Marka"), max_length=50)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.title
class Comment(models.Model):
    product = models.ForeignKey("appMy.Product", verbose_name=("Yorum Yapılan Ürün"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=("Yorum Yapan Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"))
    date_now = models.DateTimeField(("Yorum Yapılma Zamanı"), auto_now_add=True)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    brand = models.ForeignKey(Brand, verbose_name=("Ürün Markası"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Ürün Kategorisi"), on_delete=models.CASCADE)
    title = models.CharField(("Ürün Başlık"), max_length=50)
    text = models.TextField(("Ürün Özellikleri"))
    price = models.FloatField(("Ürün Fiyatı"))
    image = models.FileField(("Ürün Fotoğrafı"), upload_to='', max_length=100, null=True)

    def __str__(self):
        return self.title
