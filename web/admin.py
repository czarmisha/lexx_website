from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Image, Post, Application


admin.site.register(Image)
admin.site.register(Post, TranslatableAdmin)
admin.site.register(Application)
