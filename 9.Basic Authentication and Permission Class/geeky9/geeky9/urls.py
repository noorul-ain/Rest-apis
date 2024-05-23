

from django.contrib import admin
from django.urls import path, include
from app1 import views 
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentReadOnlyModelViewSet with Router 
router.register('students', views.StudentModelViewSet, basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]


