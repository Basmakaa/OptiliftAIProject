from rest_framework import serializers
from .models import PostureSession 

class PostureSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostureSession 
        fields = '__all__'
        