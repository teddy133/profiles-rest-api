from django.contrib import admin
from .models import UserProfile, profileFeedItem
admin.site.register(UserProfile)
admin.site.redister(profileFeedItem)


# Register your models here.
