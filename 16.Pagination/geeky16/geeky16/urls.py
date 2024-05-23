from django.contrib import admin
from django.urls import path
from app1.views import StudentList  # Ensure the import is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentList.as_view()),  # Use StudentList view
]

