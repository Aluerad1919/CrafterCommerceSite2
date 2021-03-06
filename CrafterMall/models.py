from django.db import models
import re
from taggit.managers import TaggableManager

from django.db.models.fields import CharField
class Darth_Valid(models.Manager):
    def count_Vald(self, postData):
        errors = {}
        if len(postData['email_input']) < 4:
            errors['email_input'] = 'Non-valid email length'
        if len(Users.objects.filter(email=postData['email_input'])) > 0:
            errors['email_input'] = 'An account with that email already exists.'
        if len(Users.objects.filter(user_name=postData['username_input'])) > 0:
            errors['username_input'] = 'That User Name already exists.'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_input']):
            errors['email_input'] = "Invalid email address!"
        if len(postData['username_input']) < 8:
            errors['first_name_input'] = 'User name must be more than 8 characters long'
        if len(postData['pw_input']) < 8:
            errors['pw_input'] = 'Password must be 8 at least characters.'
        if postData['pw_input'] != postData['confirm_input']:
            errors['pw_input'] = 'Passwords do not match.'
        return errors

class Users(models.Model):
    user_name = models.CharField(max_length=12)
    email = models.CharField( max_length=254)
    password = models.CharField(max_length=50)
    has_store = models.BooleanField(default=False)
    store_name = models.CharField(max_length=45, default='None')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Darth_Valid()

class Address(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    street_Add = models.CharField(max_length=75)
    unit_num = models.CharField(max_length=10, default="N/A")
    city = models.CharField(max_length=30, default="CodingTonVille")
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    user_address = models.ForeignKey(Users, related_name="user", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Keytags(models.Model):
#     craft_word = models.CharField(max_length=20)
#     keyword = models.ManyToManyField(Craft, related_name='tag')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Textile_Craft(models.Model):
    craft_name = models.CharField(max_length=45, default = ' ')
    description = models.TextField()
    craft_image = models.ImageField(null=True, blank=True, upload_to='img/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # tags = TaggableManager() <--future content with search engine
    seller = models.ForeignKey(Users, related_name="tailor", on_delete = models.CASCADE)
    in_stock_num = models.IntegerField(default=0)
    on_order = models.BooleanField(default=False)
    material = models.CharField(max_length=45,default='Textile_Craft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Leather_Craft(models.Model):
    craft_name = models.CharField(max_length=45, default = ' ')
    description = models.TextField()
    craft_image = models.ImageField(null=True, blank=True, upload_to='img/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # tags = TaggableManager() <--future content with search engine
    seller = models.ForeignKey(Users, related_name="leatherworker", on_delete = models.CASCADE)
    in_stock_num = models.IntegerField(default=0)
    on_order = models.BooleanField(default=False)
    material = models.CharField(max_length=45,default='Leather_Craft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Metal_Craft(models.Model):
    craft_name = models.CharField(max_length=45, default = ' ')
    description = models.TextField()
    craft_image = models.ImageField(null=True, blank=True, upload_to='img/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # tags = TaggableManager() <--future content with search engine
    seller = models.ForeignKey(Users, related_name="smith", on_delete = models.CASCADE)
    in_stock_num = models.IntegerField(default=0)
    on_order = models.BooleanField(default=False)
    material = models.CharField(max_length=45,default='Metal_Craft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wood_Craft(models.Model):
    craft_name = models.CharField(max_length=45, default = ' ')
    description = models.TextField()
    craft_image = models.ImageField(null=True, blank=True, upload_to='img/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # tags = TaggableManager() <--future content with search engine
    seller = models.ForeignKey(Users, related_name="carpenter", on_delete = models.CASCADE)
    in_stock_num = models.IntegerField(default=0)
    on_order = models.BooleanField(default=False)
    material = models.CharField(max_length=45,default='Wood_Craft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Jewelry_Craft(models.Model):
    craft_name = models.CharField(max_length=45, default = ' ')
    description = models.TextField()
    craft_image = models.ImageField(null=True, blank=True, upload_to='img/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # tags = TaggableManager() <--future content with search engine
    seller = models.ForeignKey(Users, related_name="jeweler", on_delete = models.CASCADE)
    in_stock_num = models.IntegerField(default=0)
    on_order = models.BooleanField(default=False)
    material = models.CharField(max_length=45,default='Jewelry_Craft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Digital_Craft(models.Model):
    craft_name = models.CharField(max_length=45, default = ' ')
    description = models.TextField()
    craft_image = models.ImageField(null=True, blank=True, upload_to='img/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # tags = TaggableManager() <--future content with search engine
    seller = models.ForeignKey(Users, related_name="artist", on_delete = models.CASCADE)
    in_stock_num = models.IntegerField(default=0)
    on_order = models.BooleanField(default=False)
    material = models.CharField(max_length=45,default='Digital_Craft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)