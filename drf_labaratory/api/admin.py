from django.contrib import admin
from .models import Tour, Exscursion, Profile, Country, User

# Register your models here.
admin.site.register(Tour)
admin.site.register(Exscursion)
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(User)
