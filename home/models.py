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
    credit_author=models.CharField(max_length=122,null=True)
    email_author=models.EmailField(max_length=254,null=True)
    content_title=models.CharField(max_length=50,null=True)
    content=models.CharField(max_length=512)
    date=models.DateField()

    def __str__(self):
        return self.content_title

class Messages(models.Model):
    encode=models.CharField(max_length=122,null=True)
    decoded_msg=models.CharField(max_length=122,null=True)
# class User(models.Model):
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name        