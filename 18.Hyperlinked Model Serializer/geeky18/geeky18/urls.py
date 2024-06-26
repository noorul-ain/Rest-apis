


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import StudentViewModelViewSet

# Create a router object
router = DefaultRouter()

# Register SingerViewSet with the router
router.register(r'', StudentViewModelViewSet, basename='singer')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URLs generated by the router
    path('', include(router.urls)),
]
