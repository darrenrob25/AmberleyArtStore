from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    default_user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_customer_email = models.EmailField(max_length=254, null=True, blank=False)
    default_contact_number = models.CharField(max_length=20, null=True, blank=False)
    default_delivery_country = CountryField(blank_label='Country *', null=True, blank=False)
    default_postal_code = models.CharField(max_length=20, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=False)
    default_address_line1 = models.CharField(max_length=80, null=True, blank=False)
    default_address_line2 = models.CharField(max_length=80, null=True, blank=True)
    default_state = models.CharField(max_length=80, null=True, blank=True)

    def __Str_(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()