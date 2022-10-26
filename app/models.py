from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, phone_number, full_name, email, date_of_birth, place, password=None):
        print(phone_number)
        if not email:
            raise ValueError('User must have an email address ')

        if not full_name:
            raise ValueError('User must have an full name')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            place=place,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password, phone_number, date_of_birth, place):
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            password=password,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            place=place,
        )
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    full_name = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    phone_number=models.CharField(('mobile number'), max_length=10,unique=True)
    place = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'place', 'full_name', 'phone_number']

    objects = MyAccountManager()

    def _str_(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, add_labels):
        return True


class UserFollow(models.Model):
    user_id = models.ForeignKey(Account, related_name="following",on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(Account, related_name="followers",on_delete=models.CASCADE)
