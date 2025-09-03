from django.db import models

class person(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class book(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  stock = models.IntegerField()
  pic = models.TextField()
  description = models.TextField()
class User(models.Model):
  name=models.CharField(max_length=20)
  email=models.CharField(max_length=30)
  password =models.CharField(max_length=20)
  is_admin=models.BooleanField(default=False)

class BorrowedBook(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  book = models.ForeignKey(book, on_delete=models.CASCADE)
  borrow_date = models.DateField(auto_now_add=True)
  due_date = models.DateField()
