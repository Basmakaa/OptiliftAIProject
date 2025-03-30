from django.contrib import admin
from .models import PostureSession

# Register your models here.
@admin.register(PostureSession)
class PostureSessionAdmin(admin.ModelAdmin):
    list_display =("user_id", "exercise_type", "timestamp","posture_score","feedback")
