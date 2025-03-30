from django.db import models

# Create your models here.
class PostureSession(models.Model) :
    user_id = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    posture_score = models.FloatField()
    feedback = models.TextField()

