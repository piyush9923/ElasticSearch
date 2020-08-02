from django.contrib import admin
from .models import Feedback_Form

# Register your models here.
class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rate', 'check', 'feed')

admin.site.register(Feedback_Form, FeedAdmin)