from django.db import models
# Create your models here.

# class Contact(models.Model):
#     name=models.CharField(max_length=122)
#     phone=models.IntegerField()
#     email=models.EmailField()
#     desc=models.TextField()
#     date=models.DateField()

#     def __str__(self):
#         return self.name

class Submissons(models.Model):
    name_author=models.CharField(max_length=122)
    credit_author=models.CharField(max_length=122)
    email_author=models.EmailField(max_length=254)
    content=models.CharField(max_length=512)
    date=models.DateField()

    def __str__(self):
        return self.name_author