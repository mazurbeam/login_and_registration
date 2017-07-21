from __future__ import unicode_literals
import re
from django.db import models

class UserManager(models.Manager):
    def registerValidation(self, postData):
        results = {'status': True, 'errors': []}
        user = []
        if not postData['first_name'] or len(postData['first_name']) < 3:
            results['status'] = False
            results['errors'].append('First name must be at least 3 characters long')
        if not postData['last_name'] or len(postData['last_name']) < 3:
            results['status'] = False
            results['errors'].append('Lirst name must be at least 3 characters long')
        if not postData['email'] or len(postData['email']) < 4 or not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = False
            results['errors'].append('Email is not valid')
        if not postData['password'] or len(postData['password']) < 8 or postData['password'] != postData['confirm_password']:
            results['status'] = False
            results['errors'].append('Please cofirm your password is 8 characters long and matches your confirm password')
        if results['status'] == True:
            user = User.objects.filter(email = postData['email'])
        if len(user) != 0:
            results['status'] = False
            results['errors'].append("User already exists. Please try another email")
        return results
    def loginValidation(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['email']) < 4:
            results['error'].append('Something went wrong. Please check your credentials and try again.')
        else:
            user = User.objects.filter(email = postData['email'])
            if len(user) <= 0:
                results['status'] = False
                results['error'].append('Something went wrong. Please check your credentials and try again.')
            elif len(postData['password']) < 8 or postData['password'] != user[0].password:
                results['status'] = False
                results['error'].append('Something went wrong. Please check your credentials and try again.')
            else:
                results['user'] = user[0]
        return results

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()
