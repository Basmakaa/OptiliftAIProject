from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posture.views import PostureSessionViewSet, analyze_posture  # <- fix typo: 'analyse' → 'analyze'

router = DefaultRouter()
router.register(r'sessions', PostureSessionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),                 # e.g. /api/sessions/
    path('api/analyze/', analyze_posture, name='analyze-posture'),  # e.g. /api/analyze/
]