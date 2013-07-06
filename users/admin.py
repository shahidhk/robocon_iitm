from django.contrib import admin
from users.models import UserProfile, Team

admin.site.register(UserProfile)
admin.site.register(Team)
