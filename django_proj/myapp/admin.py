from django.contrib import admin
from .models import UserDiagnosis

@admin.register(UserDiagnosis)
class UserDiagnosisAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "diagnosis", "predicted_category", "model_choice", "created_at")

