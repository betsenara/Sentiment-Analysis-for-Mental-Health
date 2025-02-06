from django.db import models

class UserDiagnosis(models.Model):
    text = models.TextField()  # The user's input text
    diagnosis = models.CharField(max_length=50)  # The diagnosis label
    predicted_category = models.CharField(max_length=100, null=True, blank=True)  # Stores the predicted category
    model_choice = models.CharField(max_length=10, null=True, blank=True)  # Stores which model was used
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Diagnosis: {self.diagnosis} | Predicted: {self.predicted_category} | Model: {self.model_choice} | Text: {self.text[:50]}"
        

