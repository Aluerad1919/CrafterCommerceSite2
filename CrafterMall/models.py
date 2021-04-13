from django.db import models
import re
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

class Craft(models.Model):
    seller = models.ForeignKey(Users, related_name="crafter", on_delete = models.CASCADE)
    item_title = models.CharField(max_length=45)
    description = models.TextField()
    craft_type = models.CharField(max_length=45)
    craft_image = models.ImageField(null=True, blank=True, upload_to='user_images/')
    # descriptionTag tags to be searched by
    created_date = models.DateField()
    num = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
