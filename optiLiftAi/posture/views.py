from django.shortcuts import render
from rest_framework import viewsets
from .models import PostureSession 
from .serializers import PostureSessionSerializer


from rest_framework.response import Response 
from rest_framework.decorators import api_view
import cv2
import numpy as np
from .pose_analysis import analyze_pose

# Create your views here.

class PostureSessionViewSet(viewsets.ModelViewSet) :
    queryset = PostureSession.objects.all()
    serializer_class = PostureSessionSerializer 


@api_view(['POST'])
def analyze_posture(request):
    image_file = request.FILES['image']
    np_img = np.frombuffer(image_file.read(), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    landmarks = analyze_pose(img)

    if landmarks:
        
        
        feedback = "Keep your back straight!" if landmarks else "Adjust your posture"
        return Response({'landmarks': str(landmarks), 'feedback': feedback})
    return Response({'error': 'No posture detected'}, status=400)


