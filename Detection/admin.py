from django.contrib import admin
from .models import App
from .models import User
from .models import review

# Register your models here.
admin.site.register(App)
admin.site.register(User)
admin.site.register(review)

