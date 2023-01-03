
from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionManager , PermissionsMixin
from django.utils import timezone
from django.contrib.gis.db import models
from django.db.models.signals import post_save
# from .permissions import PermissionsMixin
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin 
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 


# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length= 255 , unique=True , blank= True , null = True )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_mmrda = models.BooleanField(default=False)
    is_kfw = models.BooleanField(default=False)
    is_consultant = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# class report(models.Model):
#     report = models.FileField(upload_to='reports/', max_length=254)


# # # Abstarct Baseclass for EnvMonitoring for common field
# class Baseclass(models.Model):
#     choices = [('JAN-MAR 2022', 'JAN-MAR 2022'), ('APR-JUN 2022',
#                                                   'APR-JUN 2022'), ('JULY-AUG 2022', 'JULY-AUG 2022')]
#     quarter = models.CharField(
#         max_length=255, choices=choices, null=True, blank=True)
#     package_choice = [('CA-08', 'CA-08'), ('CA-09', 'CA-09'), ('CA-10', 'CA-10'),
#                       ('CA-11', 'CA-11'), ('CA-12', 'CA-12'), ('CA-54', 'CA-54')]
#     package = models.CharField(
#         max_length=255, choices=package_choice,  null=True, blank=True)
#     location = models.PointField(null=True, blank=True)
#     date = models.DateField(auto_now=True, null=True, blank=True)

#     class Meta:
#         abstract = True


# # --------------------------------------OCCUPATINOL HEALTH & SAFTEY MODEL-----------------------------------

# class occupationalHealthSafety(models.Model):
#     user = models.ForeignKey(
#         User, related_name="occupationalHealthSafety", on_delete=models.CASCADE)
#     location = models.PointField(null=True, blank=True)
#     joining_medical_check = models.BooleanField()
#     accidental_check = models.BooleanField()
#     nature_of_accident = models.CharField(
#         max_length=255, null=True, blank=True)
#     date_of_incident = models.DateField(auto_now_add=True, null=True, blank=True)
#     collective_majors = models.CharField(max_length=255, null=True, blank=True)
#     incident_reporting = models.CharField(
#         max_length=255, null=True,  blank=True)
#     type_of_incident = models.CharField(max_length=255, null=True, blank=True)
#     barricading = models.BooleanField()
#     photographs = models.ImageField(
#         upload_to='photographs/', null=True, blank=True)

#     def __str__(self) -> str:
#         return self.user.email


# # ----------------------- TRANINING MODEL ---------------------------------------------------------


